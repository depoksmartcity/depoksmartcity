from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime

from kesehatan.models import *

def show_main(request):
    context = {}
    return render(request, "main.html", context)

def show_healthFacility(request):
    context={}
    return render(request, "health-facility.html", context)

@login_required(login_url='/login/')
def show_healthFacility_json(request):
    facility = HealthFacility.objects.all()
    return HttpResponse(serializers.serialize('json', facility), content_type='application/json')

@login_required(login_url='/login/')
def registrasi(request):
    context={}

    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        mother_name = request.POST.get("motherName")
        email = request.POST.get("email")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        address = request.POST.get("address")
        new_patient = Patient(user = request.user, first_name=first_name, last_name=last_name, mother_name=mother_name, email=email, gender=gender, age=age, address=address)
        new_patient.save()

        return redirect("kesehatan:create-appointment")
    
    return render(request, "registrasi.html", context)

@login_required(login_url='/login/')
def create_appointment(request):
    context={}

    if Patient.objects.get(user=request.user) == None:
        return redirect("kesehatan:registrasi")

    else:
        if request.method == "POST":
            appointed_by = Patient.objects.get(user=request.user)
            facility =  HealthFacility.objects.get(name=request.POST.get("facility"))
            date = request.POST.get("date")
            time = request.POST.get("time")
            new_appointment = Appointment(appointed_by=appointed_by, facility=facility, date=date, timeslot=time)
            new_appointment.save()

            return redirect("kesehatan:show_main")
        
        return render(request, "create-appointment.html", context)

@login_required(login_url='/login/')
def show_appointment_json(request):
    appointment = Appointment.objects.filter(appointed_by = Patient.objects.get(user=request.user))
    return HttpResponse(serializers.serialize('json', appointment), content_type='application/json')