from django.db import models
from accounts.models import User, SiteEngineer
from datetime import date
from customer.models import Project

# Create your models here.

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type_choices = [
        ('excavator', 'Excavator'),
        ('bulldozer', 'Bulldozer'),
        ('crane', 'Crane'),
        ('loader', 'Loader')
    ]
    equipment_type = models.CharField(choices=type_choices, max_length=20)
    status_choices = [
        ('available', 'Available'),
        ('scheduled', 'Scheduled'),
        ('in_use', 'In Use'),
        ('in_repair', 'In Repair')
    ]
    rent_amount = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(
        upload_to='Equipment',
        max_length=300,
        default=''
    )
    status = models.CharField(choices=status_choices, max_length=20, default='available')

    def __str__(self):
        return self.name

class HouseDesign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    style_choices = [
        ('modern', 'Modern'),
        ('traditional', 'Traditional'),
        ('contemporary', 'Contemporary'),
        ('rustic', 'Rustic')
    ]
    style = models.CharField(choices=style_choices, max_length=20)
    square_footage = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    num_floors = models.IntegerField()
    garage_choices = [
        ('none', 'None'),
        ('attached', 'Attached'),
        ('detached', 'Detached')
    ]
    garage = models.CharField(choices=garage_choices, max_length=20, default='none')
    image = models.ImageField(upload_to='house_designs/', blank=True)

    def __str__(self):
        return self.name


class EquipmentRentBooking(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    quantity = models.PositiveIntegerField()
    total_cost = models.DecimalField(max_digits=8, decimal_places=2)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.equipment.name} - {self.start_date} to {self.end_date}'

class ProjectAssignment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    engineer = models.ForeignKey(SiteEngineer, on_delete=models.CASCADE)
    assigned_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.engineer.user.username} - {self.project.name}'