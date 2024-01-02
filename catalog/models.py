from django.db import models

NULLABLE = {'blank': True, 'null': True}
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(
        upload_to='products/',
        verbose_name='изображение',
        **NULLABLE)
    category = models.ForeignKey(
        'catalog.Category',
        on_delete=models.CASCADE,
        verbose_name='категория',
        **NULLABLE)
    price = models.IntegerField(verbose_name='цена за покупку')
    created = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='дата создания',
        **NULLABLE)
    changed = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='дата последнего изменения',
        **NULLABLE)

    def __str__(self):
        return f'{self.title}: {self.description} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(**NULLABLE)
    ordering = ('title',)

    def __str__(self):
        return f'{self.title}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
