# Generated by Django 4.1.7 on 2023-05-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "products",
            "0004_alter_cardmodel_options_alter_categorymodel_options_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="categorymodel",
            name="card_id",
            field=models.ManyToManyField(to="products.cardmodel"),
        ),
    ]
