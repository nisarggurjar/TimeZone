from django.db import models
from managment.models import Watch
from django.contrib.auth.models import User

class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE, blank=True, null=True)
    qty = models.IntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return self.user.username +' ---- '+self.watch.title
