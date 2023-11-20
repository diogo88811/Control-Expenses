from django.shortcuts import render
from .models import Transaction
import datetime

def home(request):
    date = {}
    date['transactions'] = ['t1', 't2', 't3']
    date['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'expenses/home.html', date)

def listing(request):
    data = {}
    data['transactions'] = Transaction.objects.all()
    return render(request, 'expenses/listing.html', data)
