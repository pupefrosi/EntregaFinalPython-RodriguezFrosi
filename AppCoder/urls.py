from django.urls import path
from . import views

urlpatterns = [
    path("inicio", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos, name="cursos"),
    path("ver_alumnos", views.ver_alumnos, name="alumnos"),
    path("ver_profesores", views.ver_profesores, name="profesores"),
    path("alta_curso", views.curso_formulario, name="alta_curso"),
    path("alta_alumnos", views.alumnos_formulario, name="alta_alumno"),
    path("alta_profesor", views.profesores_formulario, name="alta_profesor"),
    path("buscar_curso", views.buscar_curso, name="buscar"),
    path("buscar", views.buscar)
]