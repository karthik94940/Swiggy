from django.shortcuts import render
from django.views.generic import CreateView,ListView
from restaurant.forms import *
# Create your views here.
from restaurant.models import RestaurantRegistrationModel


def restaurant_home(request):
    return render(request,"restaurant/restaurant_home.html")




class RestaurantRegistration(CreateView):
    template_name = 'restaurant/restaurant_registration.html'
    model = RestaurantRegistrationModel
    success_url = '/restaurant_registration/'
    form_class = RestaurantRegistrationForm

