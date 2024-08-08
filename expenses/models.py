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
    
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    products = models.ManyToManyField(Product, through='InvoiceProduct')

    def __str__(self):
        return self.invoice_number
    
class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} for {self.invoice.invoice_number}"
    


