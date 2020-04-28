from django import forms
from restaurant.models import *

# for Exclued field restaurant Registration

class RestaurantRegistrationForm(forms.ModelForm):
    restaurant_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = RestaurantRegistrationModel
        exclude = ('restaurant_id','restaurant_status')