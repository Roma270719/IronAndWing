from django.urls import path
from .views import custom_order_index


urlpatterns = [
    path('', custom_order_index, name='custom_order_index'),
]