# Generated by Django 4.1.2 on 2022-10-27 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perpustakaan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review_times',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='synopsis',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='BookHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
