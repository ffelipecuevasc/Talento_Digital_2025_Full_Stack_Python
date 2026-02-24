from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_app2, name="app2"),
]