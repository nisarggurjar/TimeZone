from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

def Home(request):
    return render(request, 'index.html')

def Login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username = un, password = pwd)

        if user:
            login(request, user)
            return  redirect('home')
        else:
            print('Authentication failed')
    return render(request, 'login.html')