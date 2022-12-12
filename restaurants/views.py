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

#p
# Create your views here.
def show_json(request):
    restaurants = Restaurant.objects.all()
    return HttpResponse(serializers.serialize('json', restaurants))

def review_json(request, pk):
    reviews = Reviews.objects.filter(resto__pk=pk)
    return HttpResponse(serializers.serialize('json', reviews))

def show_restaurants(request, *args, **kwargs):	
    restaurants = Restaurant.objects.all()
    pk = kwargs.get('pk')
    reviews = Reviews.objects.filter(resto__pk=pk)
    context = {
        'list': restaurants,
        'reviews': reviews,
    }
    return render(request, "restaurant.html", context)

@login_required(login_url='/login/')
def create_review(request):
    if request.method == 'POST':
        review = request.POST.get('review')
        pk_resto = request.POST.get('pk_resto')
        print(review)

        a = Restaurant.objects.filter(pk=pk_resto)
        a = a.first()

        # bikin objek review
        # resto = request.resto
        new_reviews = Reviews(resto=a, review=review)
        new_reviews.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
