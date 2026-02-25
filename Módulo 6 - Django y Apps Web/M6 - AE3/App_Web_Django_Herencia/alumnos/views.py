from django.shortcuts import render

# Create your views here.
def portal_alumnos(request):
    return render(request, 'alumnos/inicio.html')

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