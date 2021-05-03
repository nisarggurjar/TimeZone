from django.shortcuts import render
from django.http import HttpResponse
from .models import *
def ContactUs(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')

def Shop(request):
    categories = Category.objects.all()
    watches = Watch.objects.filter(available=True)

    d = {"categories":categories, "watches":watches}
    return render(request, 'shop.html',d)