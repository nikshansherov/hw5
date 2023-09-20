from django.db import models
from datetime import date


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=200)
    registration_date = models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    description = models.TextField(default='', blank=True)
    added_date = models.DateField(auto_now_add=True)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)
