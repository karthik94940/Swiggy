"""swiggy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path

from restaurant import views

urlpatterns = [
    path('',views.restaurant_home,name = 'restaurant_home'),
    path('restaurant_registration/',views.RestaurantRegistration.as_view(),name = 'restaurant_registration'),
    path('restaurant_login/',views.restaurant_login , name = 'restaurant_login'),
    path('restauratn_login_check/',views.restauratn_login_check,name = 'restauratn_login_check'),
    path('otp_verified/',views.otp_verified,name = 'otp_verified')
]
