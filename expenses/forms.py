from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from.models import Transaction, Client, Product, Invoice, InvoiceProduct


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'description', 'value', 'category', 'observations']

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'id']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'ref']

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'client', 'date']

InvoiceProductFormset = inlineformset_factory(Invoice, InvoiceProduct, fields=('product', 'quantity', 'price',), extra=1, can_delete=False)