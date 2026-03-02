from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portal_alumnos(request):
    return render(request, 'alumnos/inicio.html')

@login_required
def lista_alumnos(request):
    # Acá nosotros simulamos la consulta de datos a la BD (MySQL)
    # Guardamos los datos en una LISTA de Python
    # Acá hacemos un "SELECT * FROM ALUMNOS;"
    alumnos = ["Chuck Norris", "Steven Seagal", "Jean Claude Van Damm", "Bruce Willis"]

    # Luego, creamos un DICCIONARIO llamado contexto (context) que almacena todos los datos de BD
    contexto = {
        'lista_alumnos' : alumnos
    }
    # Enviamos lo necesario a el TEMPLATE (request [solicitud HTTP], recurso [HTML], diccionario [contexto])
    return render(request, 'alumnos/lista_alumnos.html', contexto)

@login_required
def nuevo_alumno(request):
    if request.method == 'GET':
        # Acá llegaría cuando la persona apretó el botón de la barra de navegación, buscando el link
        form = forms.AlumnoForm()
    else:
        # Acá llegaría cuando la persona apretó el botón del formulario 'Crear Alumno'
        form = forms.AlumnoForm(request.POST)
        if form.is_valid():
            # Extraemos los datos de la solicitud HTTP (request) y los asignamos en variables
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['correo_electronico']
            contexto_post = {
                'nombre' : nombre,
                'apellido' : apellido,
                'email' : email
            }

            return render(request, 'alumnos/registro_exito.html', contexto_post)
    contexto = {
        'form' : form
    }
    return render(request, 'alumnos/registro_alumno.html', contexto)
