from django.contrib.auth.models import AbstractUser, Group
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='E-mail')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='Custom user permissions',
        help_text='Specific permissions for this user.',
    )

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        verbose_name='Custom user groups',
        help_text='The groups this user belongs to.',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
