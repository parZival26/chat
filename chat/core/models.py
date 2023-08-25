from django.db import models
from accounts.models import CustomUser as Usuario

class ChatGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.name

class PertenenciaGrupo(models.Model):
    grupo = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    ROL_CHOICES = (
        ('Admin', 'Administrador'),
        ('Member', 'Miembro'),
    )

    rol = models.CharField(max_length=10, choices=ROL_CHOICES, default='Member')

    def __str__(self):
        return self.grupo.name + " - " + self.usuario.nickname + " - " + self.rol