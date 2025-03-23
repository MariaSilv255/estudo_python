from django import forms
from .models import agenda


class InsereRegistros(forms.ModelForm):
    class Meta:
        model = agenda
        
        fields = ['nome','telefone']