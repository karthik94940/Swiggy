from django.db import models
from s_admin.models import *

# Create your models here.

class RestaurantRegistrationModel(models.Model):
    restaurant_id = models.AutoField(primary_key = True)
    restaurant_name = models.CharField(max_length=30)
    restaurant_contact_no = models.IntegerField(unique=True)
    restaurant_Email = models.EmailField()
    restaurant_area = models.ForeignKey(AdminAreaModel,on_delete=models.CASCADE)
    restaurant_type = models.ForeignKey(AdminRestaurantTypeModel , on_delete=models.CASCADE)