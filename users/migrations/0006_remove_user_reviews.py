# Generated by Django 4.1.2 on 2022-10-13 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_reviews"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="reviews",
        ),
    ]
