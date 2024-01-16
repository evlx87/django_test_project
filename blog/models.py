from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок')
    slug = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Slug')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Содержимое')
    image = models.ImageField(
        upload_to='product/',
        blank=True,
        null=True,
        verbose_name='Изображение(превью)')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано')
    views_count = models.IntegerField(
        default=0,
        verbose_name='просмотров')

    def __str__(self):
        return f'{self.title}, {self.slug}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
