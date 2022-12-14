from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage:index')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def login_flutter(request):
    print("MASUK DISINI")
    data = json.loads(request.body)
    username = data['username']
    password = data['password']

    if request.method == 'POST':
        user = authenticate(username=username, password=password)
        temp = User.objects.get(username=username)
        print(temp.id)
        print("AUTENTHICATE")
        print(username)
        print(password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": True,
                "username": request.user.username,
                "id": temp.id,
                "message": "Successfully Logged In!"
            }, status=200)

        else:
             return JsonResponse({
                "status": False,
                "message": "Failed to Login!"
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, your username/password may be wrong."
        }, status=401)

@csrf_exempt
def logout_flutter(request):
    logout(request)
    return JsonResponse({
            "status": True,
            "message": "Berhasil"
        }, status=200)

def logout_user(request):
    logout(request)
    return redirect('homepage:login')

@csrf_exempt
def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('homepage:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def register_flutter(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    confirm_pass = data['confirm_password']
    print(username)
    print(password)
    print(confirm_pass)

    if (password == confirm_pass):
        try:
        #Cek jika username atau email sudah terdaftar
            user = User.objects.get(username=username)
            print(user)
            return JsonResponse({'status':'register gagal'})
        except (User.DoesNotExist):
        #Jika username belum terdaftar
            user = User.objects.create_user(username=username, password=password)
            return JsonResponse({'status':'register berhasil', 'username':username, 'password':password})
