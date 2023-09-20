from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client_add/', views.client_add, name='client_add'),
    path('product_add/', views.product_add, name='product_add'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    path('client_delete/<int:id>', views.client_delete, name='client_delete'),
    path('product_selection/', views.product_selection, name='product_selection'),
    path('product_change/<int:id>', views.product_change, name='product_change'),
    path('client_change/<int:id>', views.client_change, name='client_change'),
    path('client_selection/', views.client_selection, name='client_selection'),
    path('client_orders/<int:id>', views.client_orders, name='client_orders'),
    path('order_add/', views.order_add, name='order_add'),
    path('order_selection/', views.order_selection, name='order_selection'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),
    path('order_change/<int:id>', views.order_change, name='order_change'),
    path('client_orders_period/<int:client_id>/<int:period>',
         views.client_orders_period, name='client_orders_period'),
]
