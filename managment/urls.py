from django.urls import path
from .views import *

urlpatterns = [
    path('ContactUs/', ContactUs, name='contact'),
    path('About/', About, name='about'),
]