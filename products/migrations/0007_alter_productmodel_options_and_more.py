# Generated by Django 4.1.7 on 2023-05-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_productmodel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productmodel",
            options={
                "verbose_name": "Заказ - Описание предмета из мебели",
                "verbose_name_plural": "Заказ - Описание предмета из мебели",
            },
        ),
        migrations.AlterField(
            model_name="productmodel",
            name="product_description",
            field=models.CharField(max_length=350, null=True, verbose_name="описание"),
        ),
    ]
