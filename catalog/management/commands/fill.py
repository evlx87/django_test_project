"""Модуль для очистки и заполнения базы данных тестовыми товарами и категориями"""
from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    """
    Команда для очистки и заполнения базы данных тестовыми товарами и категориями.

    Методы
    -------
    handle(self, *args, **options)
        Очищает таблицы Product и Category, создает новые записи категорий и товаров.
    """

    def handle(self, *args, **options):
        """
        Очищает таблицы Product и Category, создает новые записи категорий и товаров.
        """
        # Очистка таблиц Product и Category
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создание новых записей категорий
        category_list = [
            {"title": "vegetables", "description": "plants", },
            {"title": "meat", "description": "animals", },
            {"title": "chocolate", "description": "sweet food", },
        ]
        category_to_create = [Category(**item) for item in category_list]
        Category.objects.bulk_create(category_to_create)

        # Создание новых записей товаров
        product_list = [
            {"title": "cucumber", "category_id": 25, "price": "150"},
            {"title": "pork", "category_id": 26, "price": "200"},
            {"title": "twix", "category_id": 27, "price": "60"},
        ]
        product_to_create = [Product(**item) for item in product_list]
        Product.objects.bulk_create(product_to_create)
