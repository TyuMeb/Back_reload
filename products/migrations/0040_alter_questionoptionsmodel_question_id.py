# Generated by Django 4.1.7 on 2023-05-26 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0039_remove_questionoptionsmodel_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionoptionsmodel",
            name="question_id",
            field=models.ForeignKey(
                limit_choices_to={"category_id": 4},
                on_delete=django.db.models.deletion.CASCADE,
                to="products.questionsproductsmodel",
            ),
        ),
    ]
