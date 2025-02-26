from django.db import models
from accounts.models import User
from datetime import datetime

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    status_choices = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(choices=status_choices, max_length=20)
    customer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Complaint(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    date_filed = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    date_resolved = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.subject} ({self.customer.name})'