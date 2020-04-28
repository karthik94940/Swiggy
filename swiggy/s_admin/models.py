from django.db import models


# Login Admin Model
class AdminLoginModel(models.Model):
    user_name = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=16)



# Swiggy Admin State Table

class AdminStateModel(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.state_name

# Admin City Table
class AdminCityTable(models.Model):
    city_id = models.AutoField(primary_key = True)
    city_name = models.CharField(max_length=30,unique=True)
    state = models.ForeignKey(AdminStateModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name
    
#Admin Area Models for Area Operations
class AdminAreaModel(models.Model):
    area_id = models.AutoField(primary_key = True)
    area_name = models.CharField(max_length=30,unique=True)

    city = models.ForeignKey(AdminCityTable,on_delete=models.CASCADE)
    def __str__(self):
        return self.area_name

#Admin Restaurant type Model

class AdminRestaurantTypeModel(models.Model):
    restaurant_type_id = models.AutoField(primary_key = True)
    restaurant_type_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.restaurant_type_name





