from django.shortcuts import render
from django.http import HttpResponse

def ContactUs(request):
    return render(request, 'contact.html')

def About(request):
    return render(request, 'about.html')