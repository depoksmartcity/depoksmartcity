# Generated by Django 4.1.2 on 2022-10-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="img",
            field=models.ImageField(default="", upload_to=""),
        ),
    ]
