from django.contrib import admin
from django.urls import path, include
from customers.views import Home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('management/', include('managment.urls')),
    path('', Home, name = 'home')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

