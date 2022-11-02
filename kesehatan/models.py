from django.db import models
from django.contrib.auth.models import User

Appointment_Timeslot = (
        ('08:00 - 08:30', '08:00 - 08:30'),
        ('08:30 - 09:00', '08:30 - 09:00'),
        ('09:00 - 09:30', '09:00 - 09:30'),
        ('09:30 - 10.00', '09:30 - 10.00'),
        ('10:00 - 10:30', '10:00 - 10:30'),
        ('10:30 - 11:00', '10:30 - 11:00'),
        ('11:00 - 11:30', '11:00 - 11:30'),
        ('11:30 - 12.00', '11:30 - 12.00'))

class HealthFacility(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    address_url = models.URLField(blank=True)
    kecamatan = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length=15)
    capacity_timeslot = models.IntegerField()

    def __str__(self):
        return f'{self.name}'

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=40, choices=(('Laki-laki','Laki-laki'),('Perempuan','Perempuan'),('Lainnya','Lainnya')))
    age = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name[0].upper()}.'
    
class Appointment(models.Model):
    appointed_by = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointed_by_name = models.CharField(max_length=80)
    facility = models.ForeignKey(HealthFacility, on_delete=models.CASCADE)
    facility_name = models.CharField(max_length=50)
    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.CharField(max_length=20, choices=Appointment_Timeslot)

    def __str__(self):
        return f'{self.appointed_by} - {self.facility} - ( {self.date}, {self.timeslot} )'