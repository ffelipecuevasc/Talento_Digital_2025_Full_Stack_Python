from django.shortcuts import render

# Create your views here.
def portal_alumnos(request):
    return render(request, 'alumnos/inicio.html')