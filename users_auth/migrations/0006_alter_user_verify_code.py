# Generated by Django 5.0 on 2024-02-03 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0005_alter_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.CharField(default='013345', max_length=6, verbose_name='Код вeрификации'),
        ),
    ]
