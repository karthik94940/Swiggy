from django.contrib import messages
from django.shortcuts import render,redirect

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

# update State

def update_state(request):
    no = request.GET['no']
    na = request.GET.get('name')
    return render(request,"s_admin/update_state.html",{'no':no,"name":na})


def update_state_data(request):
    no = request.POST['no']
    name = request.POST['state_name']
    AdminStateModel.objects.filter(state_id=no).update(state_name = name)
    return redirect('view_states')