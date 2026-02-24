from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def vista_app1(request):
    ip = request.META.get('REMOTE_ADDR', 'No disponible')
    metodo = request.method
    navegador = request.META.get('HTTP_USER_AGENT', 'No disponible')
    hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sesion_key = request.session.session_key or "Sin sesión activa"
    idioma = request.META.get('HTTP_ACCEPT_LANGUAGE', 'No disponible')

    respuesta = f"""
        ¡Hola desde la App 1!

        === DATOS DE TU VISITA ===
        IP de origen   : {ip}
        Método HTTP    : {metodo}
        Navegador      : {navegador}
        Idioma         : {idioma}
        Hora exacta    : {hora}
        Clave de sesión: {sesion_key}
        """

    return HttpResponse(respuesta, content_type="text/plain")