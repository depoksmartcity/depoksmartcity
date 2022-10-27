from random import choices
from django.db import models
from django.contrib.auth.models import User

TIMESLOT_LIST = (
        ('08:00 - 08:15', '08:00 - 08:15'),
        ('08:15 - 08:30', '08:15 - 08:30'),
        ('08:30 - 08:45', '08:30 - 08:45'),
        ('08:45 - 09.00', '08:45 - 09.00'),
        ('09:00 - 09:15', '09:00 - 09:15'),
        ('09:15 - 09:30', '09:15 - 09:30'),
        ('09:30 - 09:45', '09:30 - 09:45'),
        ('09:45 - 10.00', '09:45 - 10.00'),
        ('10:00 - 10:15', '10:00 - 10:15'),
        ('10:15 - 10:30', '10:15 - 10:30'),
        ('10:30 - 10:45', '10:30 - 10:45'),
        ('10:45 - 11.00', '10:45 - 11.00'),
        ('11:00 - 11:15', '11:00 - 11:15'),
        ('11:15 - 11:30', '11:15 - 11:30'),
        ('11:30 - 11:45', '11:30 - 11:45'),
        ('11:45 - 12.00', '11:45 - 12.00'),
    )

# Create your models here.
class Kelurahan(models.Model): # TODO: belum makemigrations and migrate
    name = models.CharField(max_length=255)
    kecamatan = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class RequestKTP(models.Model): # TODO: benerin lg fields nya
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    requested_at = models.DateField(auto_now_add=True) 

    provinsi = "Jawa Barat"
    kota = "Depok"
    kecamatan = models.CharField(max_length=255)
    kelurahan = models.CharField(max_length=255)
    permohonan = models.CharField(max_length=255) 

    nama_lengkap = models.CharField(max_length=255)
    nomor_kk = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)

    rt = models.CharField(max_length=255)
    rw = models.CharField(max_length=255)
    kode_pos = models.CharField(max_length=255)

    nomor_hp = models.CharField(max_length=15)

    schedule_date = models.DateField()
    schedule_time = models.CharField(max_length=255, choices=TIMESLOT_LIST)

    def __str__(self):
        return self.schedule_date + ' at ' + self.schedule_time

# class Appointment(models.Model):
#     kelurahan = models.ForeignKey(Kelurahan, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(help_text="YYYY-MM-DD")
#     timeslot = models.IntegerField(choices=TIMESLOT_LIST)

#     def __str__(self):
#         return '{} {}'.format(self.date, self.time)

#     @property
#     def time(self):
#         return self.TIMESLOT_LIST[self.timeslot][1]


# class Doctor(models.Model):
#     """Stores info about doctor"""

#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     middle_name = models.CharField(max_length=20)
#     specialty = models.CharField(max_length=20)

#     def __str__(self):
#         return '{} {}'.format(self.specialty, self.short_name)

#     @property
#     def short_name(self):
#         return '{} {}.{}.'.format(self.last_name.title(), self.first_name[0].upper(), self.middle_name[0].upper())