from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('crear_grupo', views.CreateGrupo.as_view(), name="createGroup")
]