from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from .models import Author, Publisher, Book, BookReview, BookFavorite

# Create your views here.

def get_author(request):
    author_data = Author.objects.all()
    context = {'data': author_data}
    return

def get_author_json(request):
    author_data = Author.objects.all()
    context = {'data': author_data}
    return HttpResponse(serializers.serialize("json", author_data), content_type="application/json")

def get_author_by_id(request, id):
    author_data = Author.objects.filter(id=id)
    context = {'data': author_data}
    return

def get_author_by_id_json(request, id):
    author_data = Author.objects.filter(id=id)
    context = {'data': author_data}
    return HttpResponse(serializers.serialize("json", author_data), content_type="application/json")

def get_publisher(request):
    publisher_data = Publisher.objects.all()
    context = {'data': publisher_data}
    return

def get_publisher_json(request):
    publisher_data = Publisher.objects.all()
    context = {'data': publisher_data}
    return HttpResponse(serializers.serialize("json", publisher_data), content_type="application/json")

def get_publisher_by_id(request, id):
    publisher_data = Publisher.objects.filter(id=id)
    context = {'data': publisher_data}
    return

def get_publisher_by_id_json(request, id):
    publisher_data = Publisher.objects.filter(id=id)
    context = {'data': publisher_data}
    return HttpResponse(serializers.serialize("json", publisher_data), content_type="application/json")

def get_book(request):
    book_data = Book.objects.all()
    context = {'data': book_data}
    return

def get_book_json(request):
    book_data = Book.objects.all()
    context = {'data': book_data}
    return HttpResponse(serializers.serialize("json", book_data), content_type="application/json")

def get_book_by_id(request, id):
    book_data = Book.objects.filter(id=id)
    context = {'data': book_data}
    return

def get_book_by_id_json(request, id):
    book_data = Book.objects.filter(id=id)
    context = {'data': book_data}
    return HttpResponse(serializers.serialize("json", book_data), content_type="application/json")

def get_book_review(request):
    book_review_data = BookReview.objects.all()
    context = {'data': book_review_data}
    return

def get_book_review_json(request):
    book_review_data = BookReview.objects.all()
    context = {'data': book_review_data}
    return HttpResponse(serializers.serialize("json", book_review_data), content_type="application/json")

def get_book_review_id(request, id):
    book_review_data = BookReview.objects.filter(id=id)
    context = {'data': book_review_data}
    return   

def get_book_review_id_json(request, id):
    book_review_data = BookReview.objects.filter(id=id)
    context = {'data': book_review_data}
    return HttpResponse(serializers.serialize("json", book_review_data), content_type="application/json")  