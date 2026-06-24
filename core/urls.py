"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main.views import main_index
from account import views as account_views
from django.contrib.auth import views as auth_views
from user_profile import views as profile_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', main_index, name='main_index'),
    path('catalog/', include('catalog.urls')),
    path('custom_order/', include('custom_order.urls')),
    path('main/', include('main.urls')),
    path('accounts/login/', account_views.login_view, name='login'),
    path('accounts/register/', account_views.register_view, name='register'),
    path('accounts/profile/', profile_views.profile_view, name='profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='main_index'), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)