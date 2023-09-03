from django import forms
from .models import ChatGroup, PertenenciaGrupo
from django.contrib.auth import get_user_model


class CrearGrupoForm(forms.ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['name'] 

class AddMemberForm(forms.ModelForm):
    """
    Formulario para agregar miembros a un grupo
    """
    class Meta:
        """
        Se define el modelo y los campos que se van a utilizar
        """
        model = PertenenciaGrupo
        fields = ['usuario', 'rol']

    def __init__(self, *args, **kwargs):
        """
        Se recibe el grupo como parametro para personalizar el queryset del campo 'usuario'
        """
        grupo = kwargs.pop('grupo')
        super().__init__(*args, **kwargs)

        # Personaliza el queryset del campo 'usuario' para excluir los usuarios que ya son miembros del grupo
        usuarios_en_grupo = PertenenciaGrupo.objects.filter(grupo=grupo).values_list('usuario__id', flat=True)
        CustomUser = get_user_model()
        self.fields['usuario'].queryset = CustomUser.objects.exclude(id__in=usuarios_en_grupo)
