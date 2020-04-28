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
    path('', views.login, name='login'),
    path('admin_login_check/', views.admin_login_check, name='admin_login_check'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),

    # State
    path('admin_state/', views.admin_state, name='admin_state'),
    path('add_states/', views.add_states, name='add_states'),
    path('insert_states/', views.insert_states, name='insert_states'),
    path('view_states/', views.view_states, name='view_states'),
    path('update_state/', views.update_state, name='update_state'),
    path('update_state_data/', views.update_state_data, name='update_state_data'),
    path('delete_state/', views.delete_state, name='delete_state'),

    # City
    path('admin_city/', views.admin_city, name='admin_city'),
    path('insert_city/', views.insert_city, name='insert_city'),
    path('view_city/', views.view_city, name='view_city'),
    path('update_city/', views.update_city, name='update_city'),
    path('update_city_data/', views.update_city_data, name='update_city_data'),
    path('delete_city/',views.delete_city,name ='delete_city'),



    #Area Operations
    path('area_operations/',views.area_operations,name = 'area_operations'),
    path('insert_area/',views.insert_area,name = 'insert_area'),
    path('view_area',views.view_area,name = 'view_area'),
    path('update_area/',views.update_area,name = 'update_area'),
    path('update_area_data/',views.update_area_data,name = "update_area_data"),
    path('delte_area/',views.delete_area , name = 'delete_area'),


    #admint_restaurant_type Operations
    #path('admin_restaurant_type/',views.AdminRestaurantType.as_view(),name = 'admin_restaurant_type'),
    path('insert_restaurant/',views.AdminRestaurantType.as_view(),name = 'insert_restaurant'),
    path('update/<int:pk>',views.Update.as_view(),name = 'update'),
    path('delete/<int:pk>',views.Dlete.as_view(),name = 'delete'),


    #Restaurant Status
    path('restaurant_status/',views.RestaurantStatus.as_view(),name = 'restaurant_status'),
    path('pending_restaurant_status/',views.PendingRestaurantStatus.as_view(),name = 'pending_restaurant_status'),
    path('restaurant_status_approve/',views.restaurant_status_approve , name = 'restaurant_status_approve'),
    path('restaurant_status_cancel/', views.restaurant_status_cancel, name='restaurant_status_cancel'),
    path('view_approved_status/',views.ViewApprovedStatus.as_view(),name = 'view_approved_status'),
    path('view_cancel_status/', views.ViewCancelStatus.as_view(), name='view_cancel_status'),

]
