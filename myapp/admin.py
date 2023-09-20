from django.contrib import admin
from .models import Category, Product, Client, Order

@admin.action(description='Сбросить в ноль')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['-category', '-quantity']
    list_filter = ['added_date', 'price']
    search_fields = ['name']
    search_help_text = ['name']
    actions = [reset_quantity]

    # для одного продукта
    fields = ['name', 'category', 'price', 'quantity', 'description', 'added_date', 'image']
    readonly_fields = ['added_date']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
admin.site.register(Order, OrderAdmin)

