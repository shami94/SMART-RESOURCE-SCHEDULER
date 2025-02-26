from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def signin(request):
    if request.method == 'POST':
        user = authenticate(request, 
        username=request.POST['username'],
        password=request.POST['password'])
        if user is not None:
            login(request, user)
            if user.user_type == 'admin':
                return redirect('admin_index')
            elif user.user_type == 'engineer':
                return redirect('engineer_index')
            else:
                return redirect('custome_index')
        else:
            error = "Invalid Username / Password or Admin not Approved"
    else:
        error = None
    return render(request, 'accounts/login.html', {'error': error})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.set_password(form.cleaned_data['password'])
            obj.user_type = 'customer'
            obj.save()
            return redirect('accounts_signin')
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})

def engineer_register(request):
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2 = SiteEngineerForm(data=request.POST, files=request.FILES)
        if form1.is_valid() and form2.is_valid():
            obj1 = form1.save(commit=False)
            obj1.set_password(form1.cleaned_data['password'])
            obj1.user_type = 'engineer'
            obj1.is_active = False
            obj1.save()
            obj2 = form2.save(commit=False)
            obj2.user = obj1
            obj2.save()
            return redirect('accounts_signin')
    else:
        form1 = UserForm()
        form2 = SiteEngineerForm()
    return render(request, 'accounts/engineer_registration.html', {'form1': form1, 'form2': form2})


def logout_action(request):
    logout(request)
    return redirect('accounts_signin')


def edit_customer(request):
    if request.method == 'POST':
        form = UserEditForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts_signin')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts_signin')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
