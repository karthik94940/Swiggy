from django.contrib import messages
from django.shortcuts import render,redirect
from s_admin.models import AdminLoginModel
# Create your views here.
def login(request):
    return render(request,"s_admin/login.html")


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


def admin_home(request):
    return render(request, "s_admin/home.html")


def admin_logout(request):
    request.session['status'] = False
    return redirect('login')


def admin_state(request):
    return render(request,'s_admin/admin_state.html')