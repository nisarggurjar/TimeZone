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
    errorP = True
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
            usr = authenticate(username = un, password = pwd1)
            login(request, usr)
            return redirect('home')
    return render(request, 'signup.html')