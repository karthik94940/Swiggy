from django.shortcuts import render ,redirect
from django.views.generic import CreateView,ListView
from restaurant.forms import *
# Create your views here.
from restaurant.models import RestaurantRegistrationModel
from django.contrib.messages.views import SuccessMessageMixin

import random
def restaurant_home(request):
    return render(request,"restaurant/restaurant_home.html")




class RestaurantRegistration(SuccessMessageMixin,CreateView):
    template_name = 'restaurant/restaurant_registration.html'
    model = RestaurantRegistrationModel
    success_url = '/restaurant/restaurant_registration/'
    form_class = RestaurantRegistrationForm
    success_message = "Restaurant Registerd successfull"


def restaurant_login(request):

    return render(request,'restaurant/restaurant_login.html')

def restauratn_login_check(request):
    cno = request.POST["cno"]
    passwd = request.POST['passwd']

    try:
        res = RestaurantRegistrationModel.objects.get(restaurant_contact_no=cno , restaurant_password=passwd)
        if res.restaurant_status == "approved":
            global otp
            otp = random.randrange(100000,999999)
            numbers = res.restaurant_contact_no
            import requests

            url = "https://www.fast2sms.com/dev/bulk"

            querystring = {"authorization": "Mel3yAapE7uV6isxqUJXfI4PY1WbZoKROGhmHkDFnLBwS5vt02w7XiK1l3dEW6hcLgDFRbvMHmrJyY90", "sender_id": "FSTSMS", "message": "your Otp is " + str(otp),
                           "language": "english", "route": "p", "numbers": "7093303994"}

            headers = {
                'cache-control': "no-cache"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)



            return render(request,"restaurant/restaurant_login_check.html",)
        elif res.restaurant_status == "Pending":
            message = "Hello Restaurant  " + res.restaurant_name + "  Your restaurant still pending contact customer care"
            return render(request,"restaurant/restaurant_login.html",{"message":message})
        else:
            message = "Hello Restaurant " + res.restaurant_name + "  Your restaurant is canceled contact customer care"
            return render(request, "restaurant/restaurant_login.html", {"message": message})


    except RestaurantRegistrationModel.DoesNotExist:
       return render(request,"restaurant/restaurant_login.html",{"message": "Invalid User"})


def otp_verified(request):
    otp1 = otp
    otpv = request.POST['otpv']
    if int(otpv) == otp1:

        return render(request , "restaurant/otp_verified.html")
    else:
        return redirect('restaurant_login')
