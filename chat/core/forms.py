from django import forms
from .models import ChatGroup, PertenenciaGrupo

class CrearGrupoForm(forms.ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['name'] 
