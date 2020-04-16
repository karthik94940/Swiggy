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

from s_admin import views

urlpatterns = [
    path('',views.login,name = 'login'),
    path('admin_login_check/',views.admin_login_check,name = 'admin_login_check'),
    path('admin_home/',views.admin_home,name = 'admin_home'),
    path('admin_logout/',views.admin_logout,name = 'admin_logout'),


    #State
    path('admin_state/',views.admin_state,name = 'admin_state'),
]
