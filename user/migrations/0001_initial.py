# Generated by Django 4.2.5 on 2023-11-11 23:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField(max_length=20, unique=True)),
                ("user_email", models.EmailField(max_length=254, unique=True)),
                ("user_password", models.CharField(max_length=20)),
                ("user_nickname", models.CharField(max_length=20, unique=True)),
                (
                    "user_img",
                    models.FileField(
                        default="user_info/default_file.jpg", upload_to="user_info/"
                    ),
                ),
                ("user_validate", models.BooleanField(default=False)),
            ],
        ),
    ]
