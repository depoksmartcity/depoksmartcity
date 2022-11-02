from django.db import models
from django.contrib.auth.models import User

class Aspirasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    aspirasi = models.TextField()


