from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(
        max_length=10,
        default=''
    )
    user_type = models.CharField(
        max_length=20,
        default='admin'
    )

class SiteEngineer(models.Model):
    qualification = models.CharField(
        max_length=50
    )
    qualification_proof = models.FileField(
        max_length=300,
        upload_to="Qualification",
        default="No File",
        blank=True,
        null=True
    )
    specializations = models.CharField(
        max_length=50
    )
    specializations_proof = models.FileField(
        max_length=300,
        upload_to="Specialization",
        default="No File",
        blank=True,
        null=True
    )
    notes = models.TextField(
        max_length=2000,
        default='',
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    profile_pic = models.ImageField(
        max_length=200,
        upload_to="Profile",
        default="No Pic",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
