from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Author, Publisher, Book, BookReview, BookFavorite

# Create your views here.

def get_all_author(request):
    author_data = Author.objects.all()
    context = {'data': author_data}
    return

def get_all_author_json(request):
    author_data = Author.objects.all()
    context = {'data': author_data}
    return

