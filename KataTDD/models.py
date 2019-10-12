from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    foto = models.URLField()
    perfil = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Portafolio(models.Model):
    titulo = models.CharField(max_length=255)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


# Create your models here.
class Imagen(models.Model):
    titulo = models.CharField(max_length=255)
    enlace = models.URLField()
    descripcion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=5)
    es_publica = models.BooleanField()
    portafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
