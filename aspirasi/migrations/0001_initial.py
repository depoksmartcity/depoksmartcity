<<<<<<< HEAD:perpustakaan/migrations/0001_initial.py
# Generated by Django 4.1.2 on 2022-10-26 15:48

from django.conf import settings
import django.core.validators
=======
# Generated by Django 4.1.2 on 2022-10-28 20:11

from django.conf import settings
>>>>>>> 20cca0dcf0a46c8bc1fa9424f3d724a97f2058d4:aspirasi/migrations/0001_initial.py
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD:perpustakaan/migrations/0001_initial.py
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(blank=True, max_length=25, null=True)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True)),
                ('pages', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('edition', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('publication_date', models.DateField()),
                ('photo', models.ImageField(upload_to='img')),
                ('stock', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('is_available', models.BooleanField(default=False)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('borrowed_times', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=75)),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookFavorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perpustakaan.publisher'),
        ),
=======
            name='Aspirasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('aspirasi', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
>>>>>>> 20cca0dcf0a46c8bc1fa9424f3d724a97f2058d4:aspirasi/migrations/0001_initial.py
    ]
