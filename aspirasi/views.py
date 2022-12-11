from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import aspirasi
from aspirasi.forms import AspirasiForm
from aspirasi.models import Aspirasi
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import redirect
import json
from django.views.decorators.csrf import csrf_exempt

def show_aspirasi(request):
    data_aspirasi = Aspirasi.objects.all()
    form = AspirasiForm()
    context = {
        'data_aspirasi': data_aspirasi,
        'form' : form,
    }
    return render(request, "aspirasi.html", context)

def show_json(request):
    data_aspirasi = Aspirasi.objects.all()
    return HttpResponse(serializers.serialize("json", data_aspirasi))

@login_required(login_url='/login/')
def show_aspirasi_pendatang(request):
    data_aspirasi = Aspirasi.objects.all()
    context = {
        'data_aspirasi': data_aspirasi,
    }
    return render(request, "aspirasi.html", context)


def add_aspirasi_ajax(request):
    if request.method == "POST":
        form = AspirasiForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(username=request.user.username)
            obj.save()
            return HttpResponse(b"CREATED", status=201)
            
    return HttpResponseNotFound()

def show_json_user(request):
    data_aspirasi_user = Aspirasi.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_aspirasi_user))

@login_required(login_url='/login/')
def show_aspirasi_user(request):
    data_aspirasi_user = Aspirasi.objects.filter(user=request.user)
    context = {
        'data_aspirasi_user': data_aspirasi_user,
    }
    return render(request, "aspirasiUser.html", context)

@csrf_exempt
def add_aspirasi_flutter(request):
    data = json.loads(request.body)
    aspirasi = data['aspirasi']
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        aspirasi = Aspirasi(aspirasi=aspirasi, user=user)
        aspirasi.save()
        return JsonResponse({
                "status": True,
                "message": "Successfull!"
            }, status=200)
    return JsonResponse({
            "status": False,
            "message": "Failed!"
    }, status=502)







