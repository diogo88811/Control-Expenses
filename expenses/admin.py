from django.contrib import admin
from .models import Category
from .models import Transaction, Client, Product, Invoice, InvoiceProduct



# Register your models here.
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(InvoiceProduct)