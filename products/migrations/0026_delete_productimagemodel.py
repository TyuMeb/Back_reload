# Generated by Django 4.1.7 on 2023-05-20 21:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0025_delete_kitmodel"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ProductImageModel",
        ),
    ]
