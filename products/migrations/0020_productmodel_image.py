# Generated by Django 4.1.7 on 2023-05-19 16:40

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_productmodel_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.nameFile),
        ),
    ]



