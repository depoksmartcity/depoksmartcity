# Generated by Django 4.1.2 on 2022-10-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0002_restaurant_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="review",
            field=models.TextField(default="No reviews have been added"),
        ),
    ]