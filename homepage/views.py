from django.shortcuts import render, redirect
from django.contrib import messages
from homepage.models import Profile


def index(request):
    return render(request, 'index.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            profile= Profile.objects.create()
            profile.user=user
            profile.save()
            messages.success(request, 'Account has been successfully created!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)