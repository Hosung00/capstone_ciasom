# Generated by Django 4.2.5 on 2023-11-12 11:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_remove_user_id_alter_user_user_id_user_register"),
    ]

    operations = [
        migrations.AddField(
            model_name="user_register",
            name="time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
