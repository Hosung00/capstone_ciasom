# Generated by Django 4.2.5 on 2023-11-13 12:14

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0007_user_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_model",
            name="user_model",
            field=models.FileField(upload_to=user.models.user_model_directory_path),
        ),
    ]
