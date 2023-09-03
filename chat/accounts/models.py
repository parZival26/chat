from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Correo")
    first_name = models.CharField(max_length=30, verbose_name="Nombres")
    last_name = models.CharField(max_length=30, verbose_name="Apellidos")
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username