# Generated by Django 4.1.7 on 2023-05-18 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0015_alter_productmodel_product_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="product_description",
            field=models.CharField(max_length=350, verbose_name="описание"),
        ),
        migrations.AlterField(
            model_name="productmodel",
            name="product_price",
            field=models.IntegerField(verbose_name="цена предмета"),
        ),
        migrations.AlterField(
            model_name="productmodel",
            name="product_size",
            field=models.CharField(
                max_length=20, verbose_name="размеры высота x ширина x длина"
            ),
        ),
        migrations.AlterField(
            model_name="productmodel",
            name="product_units",
            field=models.IntegerField(verbose_name="количество предметов в шт."),
        ),
    ]
