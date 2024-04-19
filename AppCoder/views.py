from django.shortcuts import render
from AppCoder.models import Curso, Alumno, Profesor, Avatar
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, Alumno_formulario, Profesor_formulario, UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'padre.html', {'url': avatares[0].imagen.url if avatares.exists() else None})

def ver_cursos(request):
    cursos = Curso.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'cursos.html', {'cursos': cursos, 'url': avatares[0].imagen.url if avatares.exists() else None})

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
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "formulario.html", {'url': avatares[0].imagen.url if avatares.exists() else None})


def buscar_curso(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'buscar_curso.html', {'url': avatares[0].imagen.url if avatares.exists() else None})

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        curso = Curso.objects.filter(nombre__icontains= nombre)
        return render(request, "resultado_busqueda.html", {"curso": curso})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    

#Alumnos

def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'alumnos.html', {"alumnos": alumnos, 'url': avatares[0].imagen.url if avatares.exists() else None})

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
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "formulario_alumno.html", {'url': avatares[0].imagen.url if avatares.exists() else None})

#Profesores
def profesores(request):
    return render(request, "profesores.html")


def ver_profesores(request):
    profesores = Profesor.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'profesores.html', {'profesores': profesores, 'url': avatares[0].imagen.url if avatares.exists() else None})

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
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, "formulario_profesor.html", {'url': avatares[0].imagen.url if avatares.exists() else None})

#eliminar y editar curso
@login_required
def eliminar_curso(request, id):
    curso= Curso.objects.get(id=id)
    curso.delete()
    #lo anterior se puede escribir tambien como Curso.objects.get(id=id).delete() directamente sin declarar la variable
    curso = Curso.objects.all()

    return render(request, "cursos.html", {"cursos":curso})

@login_required
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
@login_required
def eliminar_alumno(request, id):
    alumno= Alumno.objects.get(id=id)
    alumno.delete()
    #lo anterior se puede escribir tambien como Curso.objects.get(id=id).delete() directamente sin declarar la variable
    alumno = Alumno.objects.all()

    return render(request, "alumnos.html", {"alumnos":alumno})

@login_required
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
@login_required
def eliminar_profesor(request, id):
    profesor= Profesor.objects.get(id=id)
    profesor.delete()
    #lo anterior se puede escribir tambien como Curso.objects.get(id=id).delete() directamente sin declarar la variable
    profesor = Profesor.objects.all()

    return render(request, "profesores.html", {"profesor":profesor})

@login_required
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

#LOGIN
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request, "inicio.html", {"url":avatares[0].imagen.url, "mensaje":f"¡Bienvenido/a {usuario}!", "usuario":usuario})
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"Formulario Incorrecto {form}")

    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse("Usuario creado con éxito")
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form":form})

def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request, "inicio.html")


    else:
        mi_formulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "editar_perfil.html", {"mi_formulario":mi_formulario, "usuario":usuario})
