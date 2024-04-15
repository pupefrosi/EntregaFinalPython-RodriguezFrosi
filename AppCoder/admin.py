from django.contrib import admin
from .models import *
# Register your models here.

#Agregado de Modelos en Admin para su manejo por allí
admin.site.register(Curso)

admin.site.register(Alumno)

admin.site.register(Profesor)
