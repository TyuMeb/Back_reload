# Generated by Django 4.1.7 on 2023-05-18 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_productmodel_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена предмета'),
        ),
    ]
