import logging

from django.shortcuts import render, redirect
from .forms import InvoiceForm, InvoiceProductFormset
from .models import Transaction, Client, Product
import datetime
from .forms import TransactionForm, ClientForm, ProductForm, InvoiceForm

def home(request):
    date = {}
    date['transactions'] = ['t1', 't2', 't3']
    date['now'] = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    return render(request, 'expenses/home.html', date)

def listing(request): #read data from the databases
    data = {}
    data['transactions'] = Transaction.objects.all()
    data['clients'] = Client.objects.all()
    data['products'] = Product.objects.all()
    return render(request, 'expenses/listing.html', data)

def new_transaction(request): #create a new row on databases
    data = {}
    form = TransactionForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listing')

    data['form'] = form
    return render(request, 'expenses/form.html', data)

def create_new_client(request): #create a new row on databases
    data = {}
    form = ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listing')

    data['form'] = form
    return render(request, 'expenses/client_form.html', data)

def create_new_product(request): #create a new row on databases
    data = {}
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listing')

    data['form'] = form
    return render(request, 'expenses/product_form.html', data)

def create_new_invoice(request): #create a new row on databases
    data = {}
    form = InvoiceForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listing')

    data['form'] = form
    return render(request, 'expenses/invoice_form.html', data)


def create_new_invoice(request):
    print(request.POST)
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        product_formset = InvoiceProductFormset(request.POST, prefix='product_formset')
        print("printing product_formset:")
        print(product_formset)

        if form.is_valid() and product_formset.is_valid():
            invoice = form.save()
            for inline_form in product_formset:
                if inline_form.cleaned_data:
                    product = inline_form.save(commit=False)
                    product.invoice = invoice  # Assuming 'invoice' is the foreign key in 'Product' pointing to 'Invoice'
                    product.save()
            return redirect('url_listing')
    else:
        form = InvoiceForm()
        product_formset = InvoiceProductFormset(prefix='product_formset')

    return render(request, 'expenses/invoice_form.html', {'form': form, 'product_formset': product_formset})




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
