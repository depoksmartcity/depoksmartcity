from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField



# Create your models here.
class Restaurant(models.Model):
    name = models.TextField()
    lokasi = models.TextField()
    desc = models.TextField()
    img = models.URLField(default='')
    # rev = ArrayField(models.TextField())

class Reviews(models.Model):
    resto = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
