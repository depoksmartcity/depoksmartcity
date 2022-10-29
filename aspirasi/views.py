from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import aspirasi
from aspirasi.forms import AspirasiForm
from aspirasi.models import Aspirasi
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import redirect

# @login_required(login_url='/homepage/login/')
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

def add_aspirasi_ajax(request):
    if request.method == "POST":
        form = AspirasiForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(username=request.user.username)
            obj.save()
            return HttpResponse(b"CREATED", status=201)
            
    return HttpResponseNotFound()
