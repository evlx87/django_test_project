# Generated by Django 5.0 on 2024-02-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0002_remove_user_username_user_is_verified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='235028', max_length=6, verbose_name='Код вeрификации'),
        ),
    ]
