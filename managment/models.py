from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Watch(models.Model):
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=30, null = True, blank=True)
    dis = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    img1 = models.FileField(null=True, blank=True)
    img2 = models.FileField(null=True, blank=True)
    img3 = models.FileField(null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Payment_ids(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ids = models.CharField(max_length=100, blank=True, null=True)