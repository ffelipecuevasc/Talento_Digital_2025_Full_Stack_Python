from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.portal_alumnos, name='inicio_alumnos'),
]