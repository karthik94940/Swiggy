from django import forms
from restaurant.models import *

# for Exclued field restaurant Registration

class RestaurantRegistrationForm(forms.ModelForm):
    class Meta:
        model = RestaurantRegistrationModel
        exclude = ('restaurant_id',)