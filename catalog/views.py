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
    Представление, отображающее список продуктов.

    Атрибуты:
    - template_name (str): Название шаблона для отображения представления.
    - queryset (QuerySet): Запрос для получения списка продуктов.
    - context_object_name (str): Имя переменной контекста для списка объектов.
    - paginate_by (int): Количество продуктов на странице.
    - ordering (str): Порядок сортировки продуктов в списке.
    - model (Model): Класс модели продуктов.
    - context (dict): Дополнительные контекстные данные для отображения представления.

    Методы:
    - get_context_data(self, **kwargs): Получает контекстные данные для отображения представления.
    """

    template_name = 'product.html'
    queryset = Product.objects.all()
    context_object_name = 'objects_list'
    paginate_by = 10
    model = Product
    context = {
        'page_title': 'Товары'
    }
