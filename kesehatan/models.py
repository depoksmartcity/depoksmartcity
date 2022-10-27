from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(null=True, blank=True, max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    status = models.BooleanField()
    sub_district = models.CharField(max_length = 50)

class Puskesmas(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    status = models.BooleanField()
    sub_district = models.CharField(max_length = 50) 