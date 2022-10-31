from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from restaurants.models import Restaurant
from restaurants.models import Reviews


# Create your views here.
def show_json(request):
    restaurants = Restaurant.objects.all()
    return HttpResponse(serializers.serialize('json', restaurants))

def review_json(request):
    reviews = Reviews.objects.all()
    return HttpResponse(serializers.serialize('json', reviews))

def show_restaurants(request):	
    restaurants = Restaurant.objects.all()
    reviews = Reviews.objects.all()
    context = {
        'list': restaurants,
        'reviews': reviews,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "restaurant.html", context)

def create_review(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        resto = request.resto
        new_reviews = Reviews(resto=resto, review=review)
        new_reviews.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
