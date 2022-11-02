from email.policy import default
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import os

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Book(models.Model):                                            
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    synopsis = models.TextField()
    pages = models.IntegerField(validators=[MinValueValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    edition = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    publication_date = models.DateField()
    photo = models.ImageField(default='')
    stock = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    borrowed_times = models.IntegerField(default=0)
    review_times = models.IntegerField(default=0)
    

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()

class BookHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)