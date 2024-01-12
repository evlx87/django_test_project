"""Модуль для очистки и заполнения базы данных тестовыми товарами и категориями"""
import json
import os

from django.core.management import BaseCommand
from catalog.models import Product, Category
from config import settings


def load_from_json(file_name):
    """
    Загружает данные из JSON-файла.

    :param file_name: имя файла без расширения
    :return: данные из файла в формате словаря
    """
    with open(os.path.join(settings.JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    """Django команда для очистки и заполнения базы данных тестовыми товарами и категориями."""

    def handle(self, *args, **options):
        """
        Обработчик команды.

        Очищает базу данных от существующих категорий и товаров,
        загружает новые категории и товары из JSON-файлов.
        """
        categories = load_from_json('categories')

        Category.objects.all().delete()
        [Category.objects.create(**category) for category in categories]

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            product["category"] = Category.objects.get(title=product["category"])
            Product.objects.create(**product)
