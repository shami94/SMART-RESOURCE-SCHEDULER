from django.db import models
from accounts.models import *
from admin.models import Project, Equipment
# Create your models here.

class ConstructionLabour(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    position = models.CharField(max_length=255)
    hourly_rate = models.DecimalField(max_digits=7, decimal_places=2)
    engineer = models.ForeignKey(
        to=SiteEngineer,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class ProjectAssignEquipments(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.equipment.name} - {self.project.name}'

class ProjectAssignLabour(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    labour = models.ForeignKey(ConstructionLabour, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.labour.name} - {self.project.name}'


