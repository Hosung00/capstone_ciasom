# Generated by Django 4.2.5 on 2023-11-13 14:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0009_user_model_model_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_model",
            name="model_name",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]