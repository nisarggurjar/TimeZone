from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from managment.models import Watch
from .models import AddToCart
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from managment.models import Payment_ids
import requests
import json

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
    if not request.user.is_authenticated:
        return redirect('login')
    wth = Watch.objects.filter(id = Wid).first()
    usr = request.user
    AddToCart.objects.create(user = usr, watch = wth, qty = 1)
    return redirect('home')

def Cart(request):
    if request.method == 'POST':
        _qty = request.POST['_qty']
        _id = request.POST['id']
        s = AddToCart.objects.filter(id=_id).update(qty = _qty)
        print("Updated", s)
        return redirect('cart')
    if request.user.is_authenticated:
        products = AddToCart.objects.filter(user = request.user)
        total = 0
        for product in products:
            total = total + product.watch.price
        d = {"total":total, "products":products}
        return render(request, 'cart.html', d)
    else:
        return redirect('home')



def SignUp(request):
    errorUN = False
    errorP = False
    if request.method == 'POST':
        n = request.POST['name']
        un = request.POST['username']
        e = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']

        check = User.objects.filter(username= un)
        if check:
            errorUN = True
        elif pwd1 != pwd2:
            errorP = True
        else:
            User.objects.create_user(username = un, password = pwd1, email = e, first_name = n, is_staff = False)
            sub = "Registered with TimeZone"
            data = {'name':n, 'email':e, 'username':un}
            from_email = settings.EMAIL_HOST_USER
            html = get_template('mail.html').render(data)
            msg = EmailMultiAlternatives(sub, '', from_email, [e])
            msg.attach_alternative(html, 'text/html')
            msg.send()
            usr = authenticate(username = un, password = pwd1)
            login(request, usr)
            return redirect('home')
    return render(request, 'signup.html', {'errorP': errorP, 'errorUN':errorUN})

headers = {
    'X-Api-Key': 'api',
    'X-Api-Token': 'api-token'
}

def Payment(request):
    products = AddToCart.objects.filter(user = request.user)
    total = 0
    for product in products:
        total = total + product.watch.price

    mob = ''
    
