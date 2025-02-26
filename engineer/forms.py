from django import forms
from .models import *

class ConstructionLabourForm(forms.ModelForm):
    """Form definition for ConstructionLabour."""

    class Meta:
        """Meta definition for ConstructionLabourform."""

        model = ConstructionLabour
        exclude = ['engineer']
