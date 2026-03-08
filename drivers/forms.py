from django import forms
from drivers.models import Driver


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'