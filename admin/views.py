from django.shortcuts import render, redirect
from .forms import *
from customer.models import Complaint
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == 'POST':
        pass
    return render(request, 'admin/index.html')

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_add_equipment')
    else:
        form = EquipmentForm()
    return render(request, 'admin/create_equipment.html', {'form': form})

def manage_equipment(request):
    equipments = Equipment.objects.all()
    return render(request, 'admin/manage_equipments.html', {'equipments': equipments})

def edit_equipment(request, id):
    equipment = Equipment.objects.get(pk=id)
    if request.method == 'POST':
        form = EquipmentForm(data=request.POST, files=request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('admin_manage_equipment')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'admin/edit_equipment.html', {'form': form})

def delete_equipment(request, id):
    Equipment.objects.get(pk=id).delete()
    return redirect('admin_manage_equipment')

def equipment_orders(request):
    orders = EquipmentRentBooking.objects.all()[::-1]
    return render(request, 'admin/orders.html', {'orders': orders})


def equipment_orders_approve(request, id):
    orders = EquipmentRentBooking.objects.get(pk=id)
    orders.is_approved = True
    orders.save()
    return redirect('admin_equipment_orders')

def new_project(request):
    project_ids = ProjectAssignment.objects.all().values_list('project_id')
    projects = Project.objects.filter(status='not_started').exclude(pk__in=project_ids)
    return render(request, 'admin/new_projects.html', {'projects': projects})

def assigned_project(request):
    projects = ProjectAssignment.objects.exclude(status=0)
    return render(request, 'admin/assigned_projects.html', {'projects': projects})

def manage_site_engineer(request):
    siteengineers = SiteEngineer.objects.all()
    return render(request, 'admin/manage_site_engineer.html', {'siteengineers': siteengineers})

def delete_engineer(request, id):
    User.objects.get(pk=id).delete()
    return redirect('admin_manage_site_engineer')

def change_status(request, id):
    user = User.objects.get(pk=id)
    user.is_active = not user.is_active
    user.save()
    return redirect('admin_manage_site_engineer')

def add_house_design(request):
    if request.method == 'POST':
        form = HouseDesignForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_add_house_design')
    else:
        form = HouseDesignForm()
    return render(request, 'admin/create_house_design.html', {'form': form})

def manage_house_design(request):
    house_designs = HouseDesign.objects.all()
    return render(request, 'admin/manage_house_design.html', {'house_designs': house_designs})

def edit_house_design(request, id):
    house_design = HouseDesign.objects.get(pk=id)
    if request.method == 'POST':
        form = HouseDesignForm(data=request.POST, files=request.FILES, instance=house_design)
        if form.is_valid():
            form.save()
            return redirect('admin_manage_house_design')
    else:
        form = HouseDesignForm(instance=house_design)
    return render(request, 'admin/edit_house_design.html', {'form': form})

def delete_house_design(request, id):
    HouseDesign.objects.get(pk=id).delete()
    return redirect('admin_manage_house_design')

def assign_engineer(request, id):
    if request.method == 'POST':
        obj = ProjectAssignment(
            project = Project.objects.get(pk=id),
            engineer = SiteEngineer.objects.get(pk=request.POST['eid']),
            status = 1
        )
        obj.save()
        return redirect('admin_assigned_project')
    else:
        engineers = SiteEngineer.objects.filter(user__is_active=True)
    return render(request, 'admin/assign_engineer.html', {'engineers':engineers})

def manage_complaints(request):
    datas = Complaint.objects.filter(is_resolved=False)
    return render(request, 'admin/manage_complaints.html', {'datas': datas})

def mark_complete(request, id):
    obj = Complaint.objects.get(pk=id)
    obj.is_resolved = True
    obj.date_resolved = datetime.now()
    obj.save()
    return redirect('admin_manage_complaints')
