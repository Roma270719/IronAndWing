from itertools import product
from django.urls import path
from .views import catalog_index, product_detail, add_to_cart, checkout_view

urlpatterns = [
    path('', catalog_index, name='catalog_index'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/checkout/', checkout_view, name='checkout'),
]