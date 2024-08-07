from django.contrib import admin
from .models import Category
from .models import Transaction, Client



# Register your models here.
admin.site.register(Category)
admin.site.register(Transaction)
admin.site.register(Client)
