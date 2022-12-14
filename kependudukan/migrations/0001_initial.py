# Generated by Django 4.1 on 2022-10-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('kecamatan', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestKTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_at', models.DateField(auto_now_add=True)),
                ('kecamatan', models.CharField(max_length=255)),
                ('kelurahan', models.CharField(max_length=255)),
                ('permohonan', models.CharField(max_length=255)),
                ('nama_lengkap', models.CharField(max_length=255)),
                ('nomor_kk', models.CharField(max_length=255)),
                ('nik', models.CharField(max_length=255)),
                ('alamat', models.CharField(max_length=255)),
                ('rt', models.CharField(max_length=255)),
                ('rw', models.CharField(max_length=255)),
                ('kode_pos', models.CharField(max_length=255)),
                ('nomor_hp', models.CharField(max_length=15)),
                ('schedule_date', models.DateField()),
                ('schedule_time', models.TimeField()),
            ],
        ),
    ]
