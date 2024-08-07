from django.forms import ModelForm
from.models import Transaction, Client, Product


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
