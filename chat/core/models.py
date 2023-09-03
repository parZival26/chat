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
        return f"{self.usuario.__str__() } Rol:{self.rol}  Grupo:{self.grupo.__str__()}"
    
class Mensaje(models.Model):
    grupo = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fechaCreacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mensaje de {self.usuario.first_name} en {self.grupo.__str__}"