# Generated by Django 4.1.7 on 2023-05-19 17:07

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_productmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.nameFile),
        ),
    ]








