from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from perpustakaan.forms import reviewForm
from .models import Author, BookHistory, Publisher, Book, BookReview
import datetime

# Create your views here.
def get_author_by_id_json(request, id):
    author_data = Author.objects.filter(id=id)
    context = {'data': author_data}
    return HttpResponse(serializers.serialize("json", author_data), content_type="application/json")

def get_publisher_by_id_json(request, id):
    publisher_data = Publisher.objects.filter(id=id)
    context = {'data': publisher_data}
    return HttpResponse(serializers.serialize("json", publisher_data), content_type="application/json")

def get_book(request):
    book_data = Book.objects.all()
    context = {'data': book_data}
    return render(request, "home.html", context)

def get_book_json(request):
    book_data = Book.objects.all()
    context = {'data': book_data}
    return HttpResponse(serializers.serialize("json", book_data), content_type="application/json")

def get_book_by_id(request, id):
    book_data = Book.objects.get(id=id)
    author_id = book_data.author.id
    publisher_id = book_data.publisher.id
    context = {'data': book_data,
                'id': id,
                'author_id': author_id,
                'publisher_id': publisher_id}
    return render(request, "book_id.html", context)

def get_book_by_id_json(request, id):
    book_data = Book.objects.filter(id=id)
    context = {'data': book_data}
    return HttpResponse(serializers.serialize("json", book_data), content_type="application/json")

def get_book_review_id_json(request, id):
    book = Book.objects.get(id=id)
    book_review_data = BookReview.objects.filter(book=book)
    context = {'data': book_review_data}
    return HttpResponse(serializers.serialize("json", book_review_data), content_type="application/json")

def get_book_history_active_id_json(request, id):
    book = Book.objects.get(id=id)
    book_history_data = BookHistory.objects.filter(book=book, user=request.user, is_active=True)
    return HttpResponse(serializers.serialize("json", book_history_data), content_type="application/json")

def get_book_history_done_id_json(request, id):   
    book = Book.objects.get(id=id)
    book_history_data = BookHistory.objects.filter(book=book, user=request.user, is_active=False)
    return HttpResponse(serializers.serialize("json", book_history_data), content_type="application/json")

@login_required(login_url='/login/')     
def borrow(request, id):
    user = request.user
    
    book = Book.objects.get(id=id)
    book.stock -= 1
    book.borrowed_times += 1
    
    if (book.stock == 0):
        book.is_available = False
    
    book.save()
    
    book_history = BookHistory.objects.create(user=user, book=book, borrow_date=datetime.datetime.now())
    book_history.save()
    return redirect('perpustakaan:get_book')

@login_required(login_url='/login/')     
def borrow_json(request, id):
    user = request.user
    
    book = Book.objects.get(id=id)
    book.stock -= 1
    book.borrowed_times += 1
    
    if (book.stock == 0):
        book.is_available = False
    
    book.save()
    
    book_history = BookHistory.objects.create(user=user, book=book, borrow_date=datetime.datetime.now())
    book_history.save()
    return HttpResponse(serializers.serialize("json", [book_history]), content_type="application/json")



@login_required(login_url='/login/')
def return_book(request, id):
    user = request.user
    
    book = Book.objects.get(id=id)
    book.stock += 1
    
    if (book.stock == 1):
        book.is_available = True
        
    book.save()   
        
    book_history = BookHistory.objects.filter(user=user, book=book, is_active=True)[0]
    book_history.is_active = False
    book_history.return_date = datetime.datetime.now()
    
    book_history.save()
    return redirect('perpustakaan:get_book')

@login_required(login_url='/login/')
def return_book_json(request, id):
    user = request.user
    
    book = Book.objects.get(id=id)
    book.stock += 1
    
    if (book.stock == 1):
        book.is_available = True
        
    book.save()   
        
    book_history = BookHistory.objects.filter(user=user, book=book, is_active=True)[0]
    book_history.is_active = False
    book_history.return_date = datetime.datetime.now()
    
    book_history.save()
    return HttpResponse(serializers.serialize("json", [book_history]), content_type="application/json")

@login_required(login_url='/login/')
def review(request, id):
    data = reviewForm(request.POST)
    
    if data.is_valid():
        user = request.user
        book = Book.objects.get(id=id)
        review = data.cleaned_data["review"]
        rate = data.cleaned_data["rate"]
        book_review = BookReview.objects.create(user=user, book=book, rate=rate, review=review)
        book_review.save()
        
        total_rate = book.rate * book.review_times
        total_rate += rate
        book.review_times += 1
        book.rate = total_rate/book.review_times
        book.save()
    return redirect('perpustakaan:get_book_by_id', id)

@login_required(login_url='/login/')
def review_json(request, id):
    if request.method == "POST":
        data = reviewForm(request.POST)
        
        if data.is_valid():
            user = request.user
            book = Book.objects.get(id=id)
            review = data.cleaned_data["review"]
            rate = data.cleaned_data["rate"]
            book_review = BookReview.objects.create(user=user, book=book, rate=rate, review=review)
            book_review.save()
            
            total_rate = book.rate * book.review_times
            total_rate += rate
            book.review_times += 1
            book.rate = total_rate/book.review_times
            book.save()
            return HttpResponse(serializers.serialize("json", [book_review]), content_type="application/json")
        return JsonResponse({"status": "Invalid input"}, status=400)
    else:
        response = JsonResponse({"status": "Invalid method"}, status=405)
        response['Allow'] = 'POST'
        return response

