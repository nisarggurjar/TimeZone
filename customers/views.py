from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from managment.models import Watch

def Home(request):
    watches = Watch.objects.all()
    d = {'watches':watches}
    return render(request, 'index.html', d)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    error = False
    if request.method == 'POST':
        un = request.POST['username']
        pwd = request.POST['password']
        print(request.POST)
        user = authenticate(username = un, password = pwd)
        if user:
            login(request, user)
            error = False
            return redirect('home')
        else:
            error = True
    return render(request, 'login.html', {'error': error})

def Logout(request):
    logout(request)
    return redirect('home')