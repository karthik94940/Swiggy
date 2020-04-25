from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView

from s_admin.forms import *
from s_admin.models import *
# Create your views here.



# admin Login
def login(request):
    return render(request,"s_admin/login.html")

# Login Check
def admin_login_check(request):
    user_name = request.POST.get('user_name')
    password = request.POST.get('password')
    try:
        AdminLoginModel.objects.get(user_name=user_name, password=password)
        request.session['status'] = True
        return redirect('admin_home')

    except AdminLoginModel.DoesNotExist:
        messages.error(request,"Invalid User name and password")
        return redirect('login')

# Admin Home
def admin_home(request):
    return render(request, "s_admin/home.html")

# Admin Logout
def admin_logout(request):
    request.session['status'] = False
    return redirect('login')

#Sdmin State Page
def admin_state(request):
    return render(request,'s_admin/admin_state.html')

# Sadmin State Insert page
def add_states(request):
    sf = AdminStateForm
    return render(request,'s_admin/add_states.html',{'sf':sf})

# State Inserting Data
def insert_states(request):
    sf = AdminStateForm(request.POST)
    if sf.is_valid():
        sf.save()
        message = "State is Saved"
        return render(request, 's_admin/add_states.html', {'sf': AdminStateForm, 'message': message})

    else:
        message  = sf.errors
        return render(request,'s_admin/add_states.html',{'sf':sf,'message':message})

# View The State List

def view_states(request):
    return render(request,"s_admin/view_states.html",{"sm":AdminStateModel.objects.all()})

# Get data for State_update

def update_state(request):
    no = request.GET['sno']
    #na = request.GET.get('sname')

    res = AdminStateModel.objects.get(state_id=no)
    print(res)
    return render(request,"s_admin/update_state.html",{"data":res})

# update State_Data
def update_state_data(request):
    no = request.POST['sno']
    name = request.POST['sname']
    AdminStateModel.objects.filter(state_id=no).update(state_name = name)
    return redirect('view_states')

#Delete State Data Based on State_Id
def delete_state(request):
    id = request.GET['sno']
    AdminStateModel.objects.filter(state_id=id).delete()
    return redirect('view_states')


#Admin City Views

def admin_city(request):
    cf = AdminCityForm
    return render(request,"s_admin/admin_city.html",{"cf":cf , "cm":AdminCityTable.objects.all()})


def insert_city(request):
    cf = AdminCityForm(request.POST)
    if cf.is_valid():
        cf.save()
        message = "City is Saved"
        return render(request, 's_admin/admin_city.html', {'cf': AdminCityForm, 'message': message ,"cm":AdminCityTable.objects.all()})
    else:
        message = cf.errors
        return render(request, 's_admin/admin_city.html', {'cf': cf, 'message': message,"cm":AdminCityTable.objects.all()})


def view_city(request):
    return render(request,'s_admin/admin_city.html',{"cm":AdminCityTable.objects.all(),"cf":AdminCityForm})


def update_city(request):
    cno = request.GET["cno"]

    res = AdminCityTable.objects.get(city_id=cno)
    return render(request,"s_admin/update_city.html",{"data":res , "data1":AdminStateModel.objects.all()})


def update_city_data(request):
    cno = request.POST['cno']
    cname = request.POST['cname']
    state = request.POST['state']
    AdminCityTable.objects.filter(city_id=cno).update(city_name = cname , state = state)
    return redirect('view_city')


def delete_city(request):
    cno = request.GET['cno']
    AdminCityTable.objects.filter(city_id=cno).delete()
    return redirect('view_city')

#Admin Area Main Operatins
def area_operations(request):
    af = AdminAreaForm
    return render(request,'s_admin/area_operations.html',{"af":af,"am":AdminAreaModel.objects.all()})


def insert_area(request):
    af = AdminAreaForm(request.POST)
    if af.is_valid():
        af.save()
        message = "Area Saved"
        return render(request,'s_admin/area_operations.html',{"af":AdminAreaForm,"message":message,"am":AdminAreaModel.objects.all()})
    else:
        message = af.errors
        return render(request,'s_admin/area_operations.html',{"af":af,"message":message,"am":AdminAreaModel.objects.all()})


def update_area(request):
    no = request.GET['ano']
    name = request.GET['aname']
    d1 = {"no":no,"name":name}
    return render(request,'s_admin/area_operations.html',{"d1":d1,"am":AdminAreaModel.objects.all()})


def update_area_data(request):
    no = request.POST['ano']
    name = request.POST['aname']
    AdminAreaModel.objects.filter(area_id=no).update(area_name = name)
    return redirect('view_area')


def view_area(request):
    return render(request,'s_admin/area_operations.html',{"am":AdminAreaModel.objects.all()})


def delete_area(request):
    no = request.GET['ano']
    AdminAreaModel.objects.filter(area_id=no).delete()
    return redirect('view_area')


#Admin Restuarant Type Operations

class AdminRestaurantType(CreateView,ListView):
    model = AdminRestaurantTypeModel
    template_name = "s_admin/admin_restaurant_home.html"
    fields = ('restaurant_type_name',)
    success_url = "/insert_restaurant/"


class Dlete(DeleteView):
    template_name = "s_admin/delete.html"
    model = AdminRestaurantTypeModel
    success_url = "/insert_restaurant/"


class Update(UpdateView):
    template_name = "s_admin/update.html"
    model = AdminRestaurantTypeModel
    fields = ('restaurant_type_name',)
    success_url = '/insert_restaurant/'