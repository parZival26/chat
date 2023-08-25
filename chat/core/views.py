from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ChatGroup, PertenenciaGrupo
from .forms import CrearGrupoForm

from django.views.generic import ListView, CreateView


class home(ListView):
    model = PertenenciaGrupo
    template_name = 'core/home.html'
    context_object_name = 'grupos_usuario'

    def get_queryset(self):
        user = self.request.user
        return PertenenciaGrupo.objects.filter(usuario=user)
    
class CreateGrupo(CreateView):
    form_class = CrearGrupoForm
    template_name = 'core/create.html'
    success_url = ''

    def form_valid(self, form) :
        grupo = form.save(commit=False)
        grupo.save()

        PertenenciaGrupo.objects.create(usuario=self.request.user, grupo=grupo, rol='administrador')

        return super().form_valid(form)



    

