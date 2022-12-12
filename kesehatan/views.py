from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from kesehatan.models import *

def show_main(request):
    context = {}
    return render(request, "main.html", context)

def show_healthFacility(request):
    context={}
    return render(request, "health-facility.html", context)

def show_healthFacility_json(request):
    facility = HealthFacility.objects.all()
    return HttpResponse(serializers.serialize('json', facility), content_type='application/json')

@login_required(login_url='/login/')
def show_registered_patient_page(request):
    context={}
    return render(request, "registered-patient.html", context)

@login_required(login_url='/login/')
def registrasi(request):
    context={}
    try:
        Patient.objects.get(user=request.user)
        return redirect("kesehatan:registered-patient")

    except Patient.DoesNotExist:
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

    try:
        Patient.objects.get(user=request.user)
        if request.method == "POST":
            appointed_by = Patient.objects.get(user=request.user)
            appointed_by_name = str(appointed_by)
            facility =  HealthFacility.objects.get(name=request.POST.get("facility"))
            facility_name = facility.name
            date = request.POST.get("date")
            time = request.POST.get("time")
            new_appointment = Appointment(appointed_by=appointed_by, appointed_by_name = appointed_by_name, facility=facility, facility_name = facility_name, date=date, timeslot=time)
            new_appointment.save()

            return redirect("kesehatan:show_main")
        
    except Patient.DoesNotExist:
        return redirect("kesehatan:registrasi")

    return render(request, "create-appointment.html", context)

@login_required(login_url='/login/')
def show_appointment_json(request):
    try:
        appointment = Appointment.objects.filter(appointed_by = Patient.objects.get(user=request.user))
        return HttpResponse(serializers.serialize('json', appointment), content_type='application/json')
        
    except Patient.DoesNotExist:
        return redirect("kesehatan:registrasi")

@login_required(login_url='/login/')
def delete_appointment(request, id):
    deleted_appointment = Appointment.objects.get(pk=id)
    deleted_appointment.delete()
    return HttpResponseRedirect(reverse("kesehatan:show_main"))

@csrf_exempt
def delete_appointment_flutter(request, id):
    data = json.loads(request.body)
    appointmentId = data['appointmentId']
    deleted_appointment = Appointment.objects.get(pk=int(appointmentId))
    deleted_appointment.delete()
    return JsonResponse({"status": "Success"}, status=204, safe=False)
    
@csrf_exempt
def get_appointment_flutter_json_by_userId(request, id):
    user = User.objects.get(pk= id)
    patient = Patient.objects.get(user = user)
    data = Appointment.objects.filter(appointed_by=patient)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def get_patient_flutter_by_userId(request, id):
    try:
        patient = Patient.objects.filter(user = id)
        return HttpResponse(serializers.serialize('json', patient), content_type='application/json')
    
    except Patient.DoesNotExist:
        return HttpResponse(serializers.serialize('json', []), content_type='application/json')

@csrf_exempt
def add_patient_flutter(request):
    data = json.loads(request.body)
    user = User.objects.get(id = int(data['user']))
    
    try:
        Patient.objects.get(user=user)
        return JsonResponse({"status": "Failed"}, status=409, safe=False)
    
    except Patient.DoesNotExist:
        new_patient = Patient.objects.create(
                user = user,
                first_name = data['first_name'],
                last_name = data['last_name'],
                mother_name = data['mother_name'],
                email = data['email'],
                gender = data['gender'],
                age = int(data['age']),
                address = data['address'])
        new_patient.save()
        print("success")
        return JsonResponse({"status": "Success"}, status=201, safe=False)

@csrf_exempt
def add_appointment_flutter(request):
    data = json.loads(request.body)
    user = User.objects.get(id = int(data['user']))
    
    try:
        Patient.objects.get(user=user)        
        appointed_by = Patient.objects.get(user=user)
        appointed_by_name = str(appointed_by)
        facility =  HealthFacility.objects.get(name=data['facility'])
        facility_name = facility.name
        date = data['date']
        timeslot = data['timeslot']
        new_appointment = Appointment(appointed_by=appointed_by, appointed_by_name = appointed_by_name, facility=facility, facility_name = facility_name, date=date, timeslot=timeslot)
        new_appointment.save()

        return JsonResponse({"status": "Success"}, status=201, safe=False)
        
    except Patient.DoesNotExist:
        return JsonResponse({"status": "Failed"}, status=409, safe=False)
