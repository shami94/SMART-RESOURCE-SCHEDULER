from django import forms
from .models import *

class UserForm(forms.ModelForm):
    """Form definition for User."""
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput()
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class SiteEngineerForm(forms.ModelForm):
    """Form definition for SiteEngineer."""

    class Meta:
        """Meta definition for SiteEngineerform."""

        model = SiteEngineer
        exclude = ['user']


class UserEditForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('email', 'phone', 'username')