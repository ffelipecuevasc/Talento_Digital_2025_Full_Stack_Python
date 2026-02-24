from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_app1, name="app1"),
]