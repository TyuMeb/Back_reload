# Generated by Django 4.1.7 on 2023-05-19 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_remove_productmodel_image_productimagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagemodel',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='products.productmodel'),
        ),
    ]