from email.policy import default
from turtle import mode
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    first_name = models.CharField()
    middle_name = models.CharField(null=True, blank=True)
    last_name = models.CharField()
    email = models.EmailField()

class Publisher(models.Model):
    name = models.CharField()
    address = models.CharField()
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

class Book(models.Model):
    title = models.CharField()
    isbn = models.CharField(max_length=13, null=True, blank=True)
    pages = models.IntegerField(validators=[MinValueValidator(1)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    edition = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    publication_date = models.DateField()
    photo = models.ImageField(upload_to=None)
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    is_available = models.BooleanField(default=False)
    rate = models.DecimalField(max_digit=3, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(5)])
    borrowed_times = models.IntegerField(default=0)

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review = models.TextField()

class BookFavorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)