from django import forms
from .models import Product, Client


class ClientForm(forms.Form):
    name = forms.CharField(max_length=50, label='Имя')
    email = forms.EmailField()
    phone = forms.CharField(max_length=12, label='Телефон')
    address = forms.CharField(max_length=15, label='Адрес')


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Наименование')
    price = forms.DecimalField(max_digits=8, decimal_places=2, label='Цена')
    quantity = forms.IntegerField(label='Количество')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Описание')
    image = forms.ImageField(label='Изображение')


def create_products_tuple():
    prod_list = []
    for product in Product.objects.all():
        prod_list.append((product.id, product.name))
    product_tuple = tuple(prod_list)
    return product_tuple


def create_clients_tuple():
    client_list = []
    for client in Client.objects.all():
        client_list.append((client.id, client.name))
    client_tuple = tuple(client_list)
    return client_tuple


class OrderForm(forms.Form):
    client_tuple = create_clients_tuple()
    customer = forms.ChoiceField(choices=client_tuple, label='Клиент')
    products_tuple = create_products_tuple()
    products = forms.MultipleChoiceField(choices=products_tuple, widget=forms.CheckboxSelectMultiple, label='Продукты')
