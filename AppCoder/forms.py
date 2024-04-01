from django import forms

class Curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()


class Alumno_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    

class Profesor_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=100)
    especialidad = forms.CharField(max_length=100)
    correo = forms.EmailField()