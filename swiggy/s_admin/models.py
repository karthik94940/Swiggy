from django.db import models


# Login Admin Model
class AdminLoginModel(models.Model):
    user_name = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=16)



# Swiggy Admin State Table

class AdminStateModel(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=30,unique=True)



