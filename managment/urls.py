from django.urls import path
from .views import *

urlpatterns = [
    path('ContactUs/', ContactUs, name='contact'),
    path('About/', About, name='about'),
    path('shop/', Shop, name='shop'),
    path('editCategories/', EditCategories, name='editCat'),
    path('editWatches/', EditWatches, name='editWatch'),
    path('managePayment/', ManagePayment, name='managePayment'),
    path('editCategory/<int:cid>/', EditCategory, name='ecat'),
]