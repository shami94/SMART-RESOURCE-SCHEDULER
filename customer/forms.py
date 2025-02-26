from django import forms
from .models import *
from admin.models import EquipmentRentBooking



class DateInput(forms.DateInput):
    input_type = 'date'

class ProjectForm(forms.ModelForm):
    """Form definition for Project."""

    class Meta:
        """Meta definition for Projectform."""

        model = Project
        exclude = ['customer', 'status']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }

class ComplaintForm(forms.ModelForm):
    """Form definition for Complaint."""

    class Meta:
        """Meta definition for Complaintform."""

        model = Complaint
        exclude = ['customer', 'is_resolved', 'date_resolved']


class EquipmentRentBookingForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = EquipmentRentBooking
        exclude = ('equipment', 'is_approved', 'user')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }


