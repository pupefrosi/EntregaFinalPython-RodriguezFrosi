from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from AppCoder.forms import Alumno_formulario
from AppCoder.forms import Profesor_formulario

# Create your views here.
def inicio(request):
    return render( request , "padre.html")


def ver_cursos(request):
    cursos = Curso.objects.all() #este Curso lo traigo del modelo planteado en models donde trabajo con DB
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)
    

def alta_curso(request, nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la DB el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def curso_formulario(request):

    if request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            curso = Curso( nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request, "formulario.html")

    return render(request, "formulario.html")

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        curso = Curso.objects.filter(nombre__icontains= nombre)
        return render(request, "resultado_busqueda.html", {"curso": curso})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

#Alumnos

def ver_alumnos(request):
    alumnos = Alumno.objects.all() #este Alumno lo traigo del modelo planteado en models donde trabajo con DB
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alta_alumnos(request, nombre, correo):
    alumno = Alumno(nombre=nombre , correo=correo)
    alumno.save()
    texto = f"Se guardaron datos del alumno: {alumno.nombre} {alumno.correo}"
    return HttpResponse(texto)

def alumnos_formulario(request):

    if request.method == "POST":
        
        mi_formulario = Alumno_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            alumno = Alumno( nombre=datos["nombre"], correo=datos["correo"])
            alumno.save()
            return render(request, "formulario_alumno.html")

    return render(request, "formulario_alumno.html")

#Profesores
def profesores(request):
    return render(request, "profesores.html")

def ver_profesores(request):
    profesores = Profesor.objects.all() #este Profesor lo traigo del modelo planteado en models donde trabajo con DB
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alta_profesor(request, nombre, especialidad, correo):
    profesor = Profesor(nombre=nombre , especialidad=especialidad, correo=correo)
    profesor.save()
    texto = f"Se guardaron datos del profesor: {profesor.nombre} {profesor.especialidad} {profesor.correo}"
    return HttpResponse(texto)


def profesores_formulario(request):

    if request.method == "POST":
        
        mi_formulario = Profesor_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            profesor = Profesor( nombre=datos["nombre"], especialidad=datos["especialidad"], correo=datos["correo"])
            profesor.save()
            return render(request, "formulario_profesor.html")

    return render(request, "formulario_profesor.html")

#eliminar y editar curso
def eliminar_curso(request, id):
    curso= Curso.objects.get(id=id)
    curso.delete()
    #lo anterior se puede escribir tambien como Curso.objects.get(id=id).delete() directamente sin declarar la variable
    curso = Curso.objects.all()

    return render(request, "cursos.html", {"cursos":curso})

def editar(request, id):
    curso = Curso.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

        curso = Curso.objects.all()

        return render(request, "cursos.html", {"cursos":curso})

    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre, "camada":curso.camada})

    return render(request, "editar_curso.html", {"mi_formulario":mi_formulario, "curso":curso})

#eliminar y editar alumno
def eliminar_alumno(request, id):
    alumno= Alumno.objects.get(id=id)
    alumno.delete()
    #lo anterior se puede escribir tambien como Curso.objects.get(id=id).delete() directamente sin declarar la variable
    alumno = Alumno.objects.all()

    return render(request, "alumnos.html", {"alumnos":alumno})

def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Alumno_formulario( request.POST )
        if mi_formulario.is_valid(): 
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.correo = datos["correo"]
            alumno.save()

        alumno = Alumno.objects.all()

        return render(request, "alumnos.html", {"alumnos":alumno})

    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre, "correo":alumno.correo})

    return render(request, "editar_alumno.html", {"mi_formulario":mi_formulario, "alumno":alumno})

#eliminar y editar profesor
def eliminar_profesor(request, id):
    profesor= Profesor.objects.get(id=id)
    profesor.delete()
    #lo anterior se puede escribir tambien como Curso.objects.get(id=id).delete() directamente sin declarar la variable
    profesor = Profesor.objects.all()

    return render(request, "profesores.html", {"profesor":profesor})

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        mi_formulario = Profesor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.especialidad = datos["especialidad"]
            profesor.correo = datos["correo"]
            profesor.save()

        profesor = Profesor.objects.all()

        return render(request, "profesores.html", {"profesores":profesor})

    else:
        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre, "especialidad":profesor.especialidad, "correo":profesor.correo})

    return render(request, "editar_profesor.html", {"mi_formulario":mi_formulario, "profesor":profesor})