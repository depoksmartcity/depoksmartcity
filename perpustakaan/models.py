from email.policy import default
from turtle import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField()

class Publisher(models.Model):
    name = models.CharField()

class Book(models.Model):
    name = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=None)
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=False)
    rate = models.DecimalField(max_digit=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    borrowed_times = models.IntegerField(default=0)

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()

class BookFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)