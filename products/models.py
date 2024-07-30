from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    available_stock = models.IntegerField(default=0)
   


