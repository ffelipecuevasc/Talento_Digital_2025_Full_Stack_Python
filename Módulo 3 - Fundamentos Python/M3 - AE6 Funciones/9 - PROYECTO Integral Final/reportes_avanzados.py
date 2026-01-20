# Módulo: reportes_avanzados.py
from datetime import datetime, timedelta


def generador_informe(lista_alumnos):
    """
    Generador existente: Emite documentos oficiales uno a uno.
    """
    for alumno in lista_alumnos:
        promedio = sum(alumno['notas']) / len(alumno['notas'])
        estado = "Aprobado" if promedio >= 4.0 else "Reprobado"
        boletin = f"DOCUMENTO OFICIAL | Alumno: {alumno['nombre']} | RUT: {alumno['rut']} | Final: {round(promedio, 1)} ({estado})"
        yield boletin