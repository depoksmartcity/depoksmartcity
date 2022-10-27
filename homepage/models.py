from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', primary_key=True)
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()