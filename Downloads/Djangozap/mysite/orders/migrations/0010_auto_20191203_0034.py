# Generated by Django 2.2.7 on 2019-12-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20191130_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлен'),
        ),
    ]
