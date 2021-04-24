from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)


class Watch(models.Model):
    title = models.CharField(max_length=30, null = True, blank=True)
    dis = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    img1 = models.FileField(null=True, blank=True)
    img2 = models.FileField(null=True, blank=True)
    img3 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.title
