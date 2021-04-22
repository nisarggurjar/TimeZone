from django.contrib import admin
from django.urls import path, include
from customers.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('management/', include('managment.urls')),
    path('', Home, name = 'home')
]

