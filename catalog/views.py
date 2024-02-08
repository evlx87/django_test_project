import re

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModeratorProductForm
from catalog.models import Product, Version


class IndexView(TemplateView):
    """
    Представление, отображающее главную страницу.

    Атрибуты:
    - template_name (str): Название шаблона для отображения представления.

    Методы:
    - get_context_data(self, **kwargs): Получает контекстные данные для отображения представления.
    """

    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        """
        Получает контекстные данные для отображения представления.

        Аргументы:
        - **kwargs: Дополнительные именованные аргументы.

        Возвращает:
        - dict: Словарь, содержащий контекстные данные.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная'
        context['objects_list'] = Product.objects.all()
        return context


class ContactsView(TemplateView):
    """
    Представление, отображающее страницу контактов.

    Атрибуты:
    - template_name (str): Название шаблона для отображения представления.

    Методы:
    - post(self, request, *args, **kwargs): Обрабатывает POST-запрос для отправки формы контактов.
    - get_context_data(self, **kwargs): Получает контекстные данные для отображения представления.
    """

    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запрос для отправки формы контактов.

        Аргументы:
        - request (HttpRequest): Объект HTTP-запроса.
        - *args: Дополнительные позиционные аргументы.
        - **kwargs: Дополнительные именованные аргументы.

        Возвращает:
        - HttpResponse: HTTP-ответ после обработки POST-запроса.
        """
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        """
        Получает контекстные данные для отображения представления.

        Аргументы:
        - **kwargs: Дополнительные именованные аргументы.

        Возвращает:
        - dict: Словарь, содержащий контекстные данные.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Контакты'
        return context


class ProductView(ListView):
    """
    Этот класс представляет собой представление для отображения списка продуктов.

    Атрибуты:
        template_name (str): Имя шаблона, используемого для отображения представления.
        model (class): Класс модели, представляющий данные для отображения.

    Методы:
        get_context_data(self, **kwargs): Переопределяет метод в родительском классе для предоставления дополнительных данных контекста для отображения.
    """
    template_name = 'catalog/product.html'
    model = Product

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Товары'
        context['objects_list'] = Product.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        if self.request.user.is_authenticated and not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user).order_by('-time_create')
        elif not self.request.user.is_authenticated:
            queryset = queryset.filter(is_published=True).order_by('-time_update')
        return queryset


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    model = Product


def is_valid_version(version):
    """Функция для проверки номера версии продукта"""
    pattern = r'^\d{1,2}\.\d{1,2}\.\d{1,2}$'
    return re.match(pattern, version) is not None


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_form_class(self):
        if not self.request.user.is_superuser and self.request.user.has_perm('catalog.set_published'):
            return ModeratorProductForm
        return ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение товара'
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
            if self.request.method == 'POST':
                context['formset'] = VersionFormset(self.request.POST, instance=self.object)
            else:
                context['formset'] = VersionFormset(instance=self.object)
        return context

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        if self.request.user == self.object.owner or self.request.user.is_superuser:
            if formset.is_valid():
                actual_version_count = 0
                for f in formset:
                    num = f.cleaned_data.get('number')
                    if num and not is_valid_version(num):
                        form.add_error(None, "Версия должна быть формата Х.Х.Х или ХХ.ХХ.ХХ")
                        return self.form_invalid(form=form)

                    if f.cleaned_data.get('is_actual'):
                        actual_version_count += 1
                        if actual_version_count > 1:
                            form.add_error(None, "Вы можете выбрать только одну активную версию")
                            return self.form_invalid(form=form)

                formset.save()
        return super().form_valid(form)

    def handle_no_permission(self):
        raise Http404('У вас нет прав для изменения этого товара')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')
    permission_required = 'catalog.product-delete'
