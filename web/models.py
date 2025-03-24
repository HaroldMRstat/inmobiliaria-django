from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):  # Extendemos el modelo de usuario de Django
    TRABAJADOR = 'trabajador'
    CLIENTE = 'cliente'

    ROLES = [
        (TRABAJADOR, 'Trabajador'),
        (CLIENTE, 'Cliente'),
    ]

    rol = models.CharField(max_length=20, choices=ROLES, default=CLIENTE)

    # Evitar conflictos con auth.User al definir related_name en las relaciones
    groups = models.ManyToManyField(Group, related_name="usuario_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuario_permissions", blank=True)

    def es_trabajador(self):
        return self.rol == self.TRABAJADOR

class Propiedad(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='propiedades/', null=True, blank=True)

    def __str__(self):
        return self.titulo


