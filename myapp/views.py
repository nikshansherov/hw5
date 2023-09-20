from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, timedelta
from .forms import *
from .models import *
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'myapp/index.html')


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            product = Product(name=name, price=price, quantity=quantity, description=description,
                              image=image, added_date=date.today())
            product.save()
            form = ProductForm()
    else:
        form = ProductForm()
    return render(request, 'myapp/product_add.html', {'form': form})


def product_selection(request):
    products = Product.objects.all()
    return render(request, "myapp/product_selection.html", {"products": products})


def product_change(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST" and "FILES":
        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.quantity = request.POST.get("quantity")
        product.description = request.POST.get("description")
        product.image = request.FILES.get("image")
        fs = FileSystemStorage()
        product.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "myapp/product_change.html", {"product": product})


def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect("/")


def client_add(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            client = Client(name=name, email=email, phone=phone, address=address, registration_date=date.today())
            client.save()
            form = ClientForm()
    else:
        form = ClientForm()
    return render(request, 'myapp/client_add.html', {'form': form})


def client_selection(request):
    clients = Client.objects.all()
    return render(request, "myapp/client_selection.html", {"clients": clients})

def client_orders(request, id):
    # if request.method == "POST" and "FILES":
    client = Client.objects.get(id=id)
    orders = Order.objects.all()
    return render(request, "myapp/client_orders.html", {"client": client, "orders": orders})

def client_change(request, id):
    client = Client.objects.get(id=id)
    if request.method == "POST":
        client.name = request.POST.get("name")
        client.email = request.POST.get("email")
        client.phone = request.POST.get("phone")
        client.address = request.POST.get("address")
        client.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "myapp/client_change.html", {"client": client})


def client_delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()
    return HttpResponseRedirect("/")


def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            selected_castomer = form.cleaned_data['customer']
            selected_products = form.cleaned_data['products']
            castomer = Client.objects.get(pk=int(selected_castomer))
            order = Order(customer=castomer, date_ordered=date.today())
            order.save()
            sum = 0
            prod_list = []
            for i in selected_products:
                order.products.add(int(i))
                prod = Product.objects.get(pk=int(i))
                sum += prod.price
            order.total_price = sum
            order.save()
            return HttpResponseRedirect("/")
    else:
        form = OrderForm()
    return render(request, 'myapp/order_add.html', {'form': form})


def order_change(request, id):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        order = Order.objects.get(id=id)
        if form.is_valid():
            castomer = Client.objects.get(pk=order.customer.id)
            selected_castomer = form.cleaned_data['customer']
            selected_products = form.cleaned_data['products']
            castomer = Client.objects.get(pk=int(selected_castomer))
            order = Order(pk=id, customer=castomer, date_ordered=date.today())
            order.products.clear()
            order.save()
            sum = 0
            for i in selected_products:
                prod = Product.objects.get(pk=int(i))
                order.products.add(prod)
                sum += prod.price
            order.total_price = sum
            return HttpResponseRedirect("/")
    else:
        form = OrderForm()
        order = Order.objects.get(id=id)
    return render(request, 'myapp/order_change.html', {'form': form, 'order': order})


def order_selection(request):
    orders = Order.objects.all()
    return render(request, "myapp/order_selection.html", {"orders": orders})


def order_delete(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return HttpResponseRedirect("/")


def client_orders_period(request, client_id, period):
    time = date.today() - timedelta(days=period)
    cont = {}
    for order in Order.objects.all():
        if order.date_ordered >= time:
            if order.customer.id == client_id:
                client_name = order.customer.name
                product_list = []
                for product in order.products.all():
                    if product.name not in product_list:
                        product_list.append(product.name)
    context = {'product_list': product_list, 'client': client_name, 'period': period}
    return render(request, 'myapp/client_orders_period.html', context)
