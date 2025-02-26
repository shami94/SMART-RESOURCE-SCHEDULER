from django.shortcuts import render, redirect
from .forms import *
from admin.models import ProjectAssignment, Project, HouseDesign

# Create your views here.

def index(request):
    projects = ProjectAssignment.objects.filter(engineer=SiteEngineer.objects.get(user=request.user), status=1)
    return render(request, 'engineer/index.html', {'projects': projects})

def accept(request, id):
    obj = ProjectAssignment.objects.get(pk=id)
    obj.status = 2
    obj.save()
    return redirect('engineer_index')

def reject(request, id):
    obj = ProjectAssignment.objects.get(pk=id)
    obj.status = 3
    obj.save()
    return redirect('engineer_index')

def manage_labour(request):
    labours = ConstructionLabour.objects.filter(engineer=SiteEngineer.objects.get(user=request.user))
    return render(request, 'engineer/manage_labour.html', {'labours': labours})

def add_labour(request):
    user = SiteEngineer.objects.get(user=request.user)
    print(user)
    if request.method == 'POST':
        form = ConstructionLabourForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.engineer = user
            obj.save()
            return redirect('engineer_add_labour')
    else:
        form = ConstructionLabourForm()
    return render(request, 'engineer/add_labour.html', {'form': form})

def delete_labour(request, id):
    ConstructionLabour.objects.get(pk=id).delete()
    return redirect('engineer_manage_labour')


def accepted_project(request):
    if request.method == 'POST':
        project = Project.objects.get(pk=request.POST['pid'])
        project.status = request.POST['status']
        project.save()
        return redirect('engineer_accepted_project')
    else:
        pass
    projects = ProjectAssignment.objects.filter(engineer=SiteEngineer.objects.get(user=request.user), status=True)
    return render(request, 'engineer/accepted_projects.html', {'projects': projects, 'options': Project.status_choices})


def assigne_equipments(request, id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        equipment = Equipment.objects.get(pk=request.POST['eid'])
        obj = ProjectAssignEquipments(
            project=project,
            equipment=equipment
        )
        obj.save()
        equipment.status = 'scheduled'
        equipment.save()
        return redirect('engineer_assigne_equipments', id=id)
    else:
        pass
    datas = ProjectAssignEquipments.objects.filter(project=project)
    equipments = Equipment.objects.filter(status='available')
    return render(request, 'engineer/assigne_equipments.html', {'datas': datas, 'equipments': equipments})

def delete_assigne_equipments(request, id):
    obj = ProjectAssignEquipments.objects.get(pk=id)
    equipment = Equipment.objects.get(pk=obj.equipment)
    equipment.status = 'available'
    equipment.save()
    obj.delete()
    return redirect('engineer_accepted_project')

def assigne_labours(request, id):
    project = Project.objects.get(pk=id)
    if request.method == 'POST':
        labour = ConstructionLabour.objects.get(pk=request.POST['lid'])
        obj = ProjectAssignLabour(
            project=project,
            labour=labour
        )
        obj.save()
        return redirect('engineer_assigne_labours', id=id)
    else:
        pass
    datas = ProjectAssignLabour.objects.filter(project=project)
    labours = ConstructionLabour.objects.filter(engineer=SiteEngineer.objects.get(user=request.user))
    return render(request, 'engineer/assigne_labours.html', {'datas': datas, 'labours': labours})

def delete_assigne_labours(request, id):
    obj = ProjectAssignLabour.objects.get(pk=id)
    obj.delete()
    return redirect('engineer_accepted_project')

def house_designs(request):
    datas = HouseDesign.objects.all()
    return render(request, 'engineer/design.html',{'house_designs': datas} )

