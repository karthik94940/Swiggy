from django.db import models



class AdminLoginModel(models.Model):
    user_name = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=16)
