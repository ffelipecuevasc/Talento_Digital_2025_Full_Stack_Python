from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.portal_alumnos, name='inicio_alumnos'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('registrar_alumno/', views.nuevo_alumno, name='registro_alumno')
]