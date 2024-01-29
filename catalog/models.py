from django.db import models


# Create your models here.
class BaseModel(models.Model):
    """
    Абстрактная модель, предоставляющая поля для отслеживания даты создания
    и последнего изменения объекта.
    """
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания')
    changed = models.DateTimeField(
        auto_now=True,
        verbose_name='дата последнего изменения')

    class Meta:
        abstract = True


class Category(models.Model):
    """
    Модель категории товаров.
    """
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    ordering = ('title',)

    def __str__(self):
        return f'{self.title}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(BaseModel):
    """
    Модель продукта.
    """
    title = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(
        verbose_name='описание', blank=True, null=True)
    preview = models.ImageField(
        upload_to='products/',
        verbose_name='изображение',
        blank=True,
        null=True)
    category = models.ForeignKey(
        'catalog.Category',
        on_delete=models.CASCADE,
        verbose_name='категория',
        blank=True,
        null=True)
    price = models.IntegerField(verbose_name='цена за покупку')

    def __str__(self):
        return f'{self.title}: {self.description} - {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    VERSION_CHOICES = ((True, 'активная'), (False, 'не активная'))

    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    version_number = models.IntegerField(
        default=1, blank=True, verbose_name='Номер версии')
    version_name = models.CharField(
        max_length=250, verbose_name='Название версии')
    is_current = models.BooleanField(
        choices=VERSION_CHOICES,
        verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('version_number',)  # сортировка по номеру версии
