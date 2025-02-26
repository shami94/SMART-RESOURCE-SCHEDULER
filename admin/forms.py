from django import forms
from .models import *

class EquipmentForm(forms.ModelForm):
    """Form definition for Equipment."""

    class Meta:
        """Meta definition for Equipmentform."""

        model = Equipment
        fields ='__all__'

class HouseDesignForm(forms.ModelForm):
    """Form definition for HouseDesign."""

    class Meta:
        """Meta definition for HouseDesignform."""

        model = HouseDesign
        fields = '__all__'


