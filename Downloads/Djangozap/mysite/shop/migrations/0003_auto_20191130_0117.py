# Generated by Django 2.2.7 on 2019-11-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191130_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение товара'),
        ),
    ]