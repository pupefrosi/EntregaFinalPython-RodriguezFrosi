from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#modelo son todas aquellas funciones que quiero que tenga mi app o entidades
#como voy a almacenar mis datos en la base de dato
#voy a crear ABM (altas, bajas y modificaciones)

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} Camada: {self.camada}"

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} Correo: {self.correo}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} Especialidad: {self.especialidad} Correo: {self.correo}"
    

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True , blank=True)

    def __str__(self):
        return f"Usuario: {self.user} Imagen: {self.imagen}"