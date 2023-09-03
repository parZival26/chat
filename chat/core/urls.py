from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('crear_grupo', views.CreateGrupo.as_view(), name="createGroup"),
    path('grupo/<int:pk>', views.DetailGroup.as_view(), name="group"),
    path('grupo/<int:pk>/add_member', views.AddMember.as_view(), name="addMember"),
]