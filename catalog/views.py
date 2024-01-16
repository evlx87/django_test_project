from django.views.generic import TemplateView, ListView
from catalog.models import Product


class IndexView(TemplateView):
    """
    Представление, отображающее главную страницу.

    Атрибуты:
    - template_name (str): Название шаблона для отображения представления.

    Методы:
    - get_context_data(self, **kwargs): Получает контекстные данные для отображения представления.
    """

    template_name = 'index.html'

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

    template_name = 'contacts.html'

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
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Товары'
        context['objects_list'] = Product.objects.all()
        return context
