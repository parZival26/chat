from typing import Any, Dict
from .models import ChatGroup, PertenenciaGrupo, Mensaje
from .forms import CrearGrupoForm, AddMemberForm

from accounts.models import CustomUser as User


from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError


class home(LoginRequiredMixin, ListView):
    model = PertenenciaGrupo
    template_name = 'core/home.html'
    context_object_name = 'grupos_usuario'

    def get_queryset(self):
        user = self.request.user
        return PertenenciaGrupo.objects.filter(usuario=user)
    
class CreateGrupo(LoginRequiredMixin, CreateView):
    form_class = CrearGrupoForm
    template_name = 'core/create.html'
    success_url = 'core/'

    def form_valid(self, form) :
        grupo = form.save(commit=False)
        grupo.save()

        PertenenciaGrupo.objects.create(usuario=self.request.user, grupo=grupo, rol='administrador')

        return super().form_valid(form)
    


class DetailGroup(LoginRequiredMixin, DetailView):
    model = ChatGroup
    template_name = 'core/group.html'
    # Aqui se define el nombre de la variable de contexto que se va a utilizar en el template
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        grupo = self.get_object()
        context['miembros'] = PertenenciaGrupo.objects.filter(grupo=grupo)
        return context
    
    
    
class AddMember(LoginRequiredMixin, CreateView):
    """
    Vista para agregar miembros a un grupo
    """
    model = PertenenciaGrupo
    template_name = 'core/add_member.html'
    form_class = AddMemberForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        grupo_id = self.kwargs['pk']
        grupo = ChatGroup.objects.get(id=grupo_id)
        kwargs['grupo'] = grupo  # Pasa el grupo como argumento al formulario
        return kwargs

    def get_context_data(self, **kwargs: Any):
        """
        Se sobreescribe el metodo get_context_data para poder pasarle el grupo al template
        """
        context = super().get_context_data(**kwargs)
        grupo_id = self.kwargs['pk']
        grupo = ChatGroup.objects.get(id=grupo_id)
        context['grupo'] = grupo
        return context
    
    def form_valid(self, form):
        """
        Se sobreescribe el metodo form_valid para poder asignarle el grupo al que se esta agregando el miembro
        """
        grupo_id = self.kwargs['pk']
        grupo = ChatGroup.objects.get(id=grupo_id)
        usuario = form.cleaned_data['usuario']

        if PertenenciaGrupo.objects.filter(grupo=grupo, usuario=usuario).exists():
            raise ValidationError("El usuario ya es miembro del grupo")

        form.instance.grupo = grupo
        return super().form_valid(form)
    
    def get_success_url(self):
        """
        Se sobreescribe el metodo get_success_url para poder redirigir al usuario al grupo al que se le agrego el miembro
        """
        grupo_id = self.kwargs['pk']
        return reverse('group', kwargs={'pk': grupo_id})

