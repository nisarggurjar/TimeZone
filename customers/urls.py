from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('AddToCart/<int:Wid>', addToCart, name='addcart'),
    path('cart/', Cart, name='cart')
]
