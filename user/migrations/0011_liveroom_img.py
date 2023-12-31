# Generated by Django 4.2.5 on 2023-11-17 11:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import user.models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0010_alter_user_model_model_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="LiveRoom_img",
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
                ("host_id", models.CharField(max_length=20)),
                (
                    "video_img",
                    models.FileField(upload_to=user.models.user_directory_path),
                ),
                ("time", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.liveroom"
                    ),
                ),
            ],
        ),
    ]
