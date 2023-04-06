from django import forms

from .models import Module, Pin


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['is_used']