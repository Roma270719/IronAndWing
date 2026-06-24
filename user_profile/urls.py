from django.urls import path
from .views import user_profile_index

urlpatterns = [
    path('', user_profile_index, name='user_profile_index'),
]