from _ast import mod

from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    dt_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description
    
class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.name
     
class Product(models.Model):
    name = models.CharField(max_length=100)
    ref = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return self.name
