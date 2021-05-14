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

def EditCategories(request):
    if not request.user.is_staff:
        return redirect('home')
    if 'delete' in request.POST:
        Category.objects.filter(id = request.POST['delete']).delete()
    if 'add' in request.POST:
        Category.objects.create(name = request.POST['CategoryName'])
    Cat = Category.objects.all()
    d = {'Cat':Cat}
    return render(request, 'editCat.html', d)

def EditCategory(request, cid):
    cat = Category.objects.filter(id=cid).first()
    if request.method == 'POST':
        cat.name = request.POST['categoryName']
        cat.save()
    return render(request, 'editCategory.html', {'cat':cat})

def EditWatches(request):
    watches =Watch.objects.all()
    if 'delete' in request.POST:
        Watch.objects.filter(id = request.POST['delete']).delete()
    return render(request, 'EditWatch.html', {'watches':watches})

def ManagePayment(request):
    pass


    