# Generated by Django 5.1.2 on 2024-11-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("expenses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.CharField(
                choices=[
                    ("food", "Food"),
                    ("transport", "Transport"),
                    ("entertainment", "Entertainment"),
                    ("utilities", "Utilities"),
                ],
                max_length=100,
            ),
        ),
    ]
