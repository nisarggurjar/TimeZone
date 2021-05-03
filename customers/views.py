from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from managment.models import Watch
from .models import AddToCart

def Home(request):
    watches = Watch.objects.all()
    latest_watch = watches[0:3]
    d = {'watches':watches, 'latest_watch':latest_watch}
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

def addToCart(request, Wid):
    wth = Watch.objects.filter(id = Wid).first()
    usr = request.user
    AddToCart.objects.create(user = usr, watch = wth, qty = 1)
    return redirect('home')

def Cart(request):
    products = AddToCart.objects.filter(user = request.user)
    total = 0
    for product in products:
        total = total + product.watch.price
        
    d = {"total":total, "products":products}
    return render(request, 'cart.html', d)




