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

# Create your views here.
def show_json(request):
    restaurants = Restaurant.objects.all()
    return HttpResponse(serializers.serialize('json', restaurants))

def show_restaurants(request):	
    restaurants = Restaurant.objects.all()
    context = {
        'list': restaurants,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "restaurant.html", context)

# def create_review(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         lokasi = request.POST.get('lokasi')
#         rating = request.POST.get('rating')
#         new_restaurant = Restaurant(name=name, lokasi=lokasi, rating=rating)
#         new_task.save()

#         return HttpResponse(b"CREATED", status=201)

#     return HttpResponseNotFound()
