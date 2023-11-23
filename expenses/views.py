import logging

from django.shortcuts import render, redirect
from .models import Transaction
import datetime
from .forms import TransactionForm

def home(request):
    date = {}
    date['transactions'] = ['t1', 't2', 't3']
    date['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'expenses/home.html', date)

def listing(request): #read data from the databases
    data = {}
    data['transactions'] = Transaction.objects.all()
    return render(request, 'expenses/listing.html', data)

def new_transaction(request): #create a new rown on databases
    data = {}
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listing')

    data['form'] = form
    return render(request, 'expenses/form.html', data)

def update(request, pk): #update data on the database
    data = {}
    transaction = Transaction.objects.get(pk =pk)
    form = TransactionForm(request.POST or None, instance=transaction)

    if form.is_valid():
        form.save()
        return redirect('url_listing')

    data['form'] = form
    data['transaction'] = transaction
    return render(request, 'expenses/form.html', data)

def delete(request, pk):
    logging.info('In')
    transaction = Transaction.objects.get(pk =pk)
    transaction.delete()
    logging.info('In')
    return redirect('url_listing')
