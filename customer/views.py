from django.shortcuts import render, redirect
from .forms import *
from admin.models import ProjectAssignment, HouseDesign
from admin.models import Equipment, EquipmentRentBooking
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    equipments = Equipment.objects.filter(status='available')
    return render(request, 'customer/index.html', {'equipments': equipments})

def housedesigns(request):
    housedesigns = HouseDesign.objects.all()
    return render(request, 'customer/house.html', {'housedesigns': housedesigns})

def housedesignsdetails(request, id):
    design = HouseDesign.objects.get(pk=id)
    return render(request, 'customer/more.html', {'design': design})


@login_required
def booknow(request, id):
    equipment = Equipment.objects.get(pk=id)
    if request.method == 'POST':
        form = EquipmentRentBookingForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.equipment = equipment
            obj.user = request.user
            obj.save()
            return redirect('custome_index')
    else:
        form = EquipmentRentBookingForm()
    return render(request, 'customer/booking.html', {'form': form, 'equipment': equipment})

@login_required
def my_orders(request):
    orders = EquipmentRentBooking.objects.filter(user=request.user)
    return render(request, 'customer/orders.html', {'orders': orders})

@login_required
def delete_order(request, id):
    EquipmentRentBooking.objects.get(pk=id).delete()
    return redirect('custome_my_orders')

@login_required
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.status = 'not_started'
            obj.save()
            return redirect('custome_add_project')
    else:
        form = ProjectForm()
    return render(request, 'customer/create_project.html', {'form': form})

@login_required
def manage_project(request):
    projects = Project.objects.filter(customer=request.user)
    return render(request, 'customer/manage_project.html', {'projects': projects})

@login_required
def edit_project(request, id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        form = ProjectForm(data = request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('custome_manage_project')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'customer/edit_project.html', {'form': form})

@login_required
def delete_project(request, id):
    Project.objects.get(pk=id).delete()
    return redirect('custome_manage_project')

@login_required
def add_compalints(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('custome_add_compalints')
    else:
        form = ComplaintForm()
    return render(request, 'customer/add_compalints.html', {'form': form})


    
