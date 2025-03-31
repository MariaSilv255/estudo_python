from django import forms
from .models import Boletins

class inserer_registro(forms.ModelForm):
    class Meta:
        model = Boletins
        fields = ['matricula','nome_do_aluno',"nota1",'nota2']

        
       