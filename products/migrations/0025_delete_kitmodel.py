# Generated by Django 4.1.7 on 2023-05-20 20:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0024_alter_productimagemodel_product_id"),
    ]

    operations = [
        migrations.DeleteModel(
            name="KitModel",
        ),
    ]
