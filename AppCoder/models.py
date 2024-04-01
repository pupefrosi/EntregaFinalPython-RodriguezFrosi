from django.db import models

# Create your models here.

#modelo son todas aquellas funciones que quiero que tenga mi app o entidades
#como voy a almacenar mis datos en la base de dato
#voy a crear ABM (altas, bajas y modificaciones)

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()


class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre