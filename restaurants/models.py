from email.policy import default
from pyexpat import model
from django.db import models
from requests import delete

# Create your models here.
class Restaurant(models.Model):
    name = models.TextField()
    lokasi = models.TextField()
    rating = models.TextField()
    img = models.ImageField(default='')

class Reviews(models.Model):
    resto = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.TextField(default='No reviews have been added')
