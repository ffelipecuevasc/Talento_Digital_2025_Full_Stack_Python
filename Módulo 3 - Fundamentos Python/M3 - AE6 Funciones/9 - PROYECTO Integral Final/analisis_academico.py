# Módulo: analisis_academico.py

def determinar_situacion_final(promedio):
    """
    Define si aprueba o reprueba basado en parámetros en Tupla.
    """
    # Tupla de configuración: (Nota Minima Aprobación, Estado Aprobado, Estado Reprobado)
    parametros_regla = (4.0, "Aprobado", "Reprobado")

    if promedio >= parametros_regla[0]:
        return parametros_regla[1]
    else:
        return parametros_regla[2]


def filtrar_aprobados(lista_alumnos):
    """
    Retorna lista de alumnos con promedio >= 4.0.
    """
    aprobados = []
    for alumno in lista_alumnos:
        prom = sum(alumno['notas']) / len(alumno['notas'])
        # Reutilizamos la lógica centralizada
        estado = determinar_situacion_final(prom)
        if estado == "Aprobado":
            # Creamos una copia del alumno con el promedio calculado para el reporte
            alumno_reporte = alumno.copy()
            alumno_reporte['promedio_final'] = round(prom, 1)
            aprobados.append(alumno_reporte)
    return aprobados


def filtrar_reprobados(lista_alumnos):
    """
    Retorna lista de alumnos con promedio < 4.0.
    """
    reprobados = []
    for alumno in lista_alumnos:
        prom = sum(alumno['notas']) / len(alumno['notas'])
        estado = determinar_situacion_final(prom)
        if estado == "Reprobado":
            alumno_reporte = alumno.copy()
            alumno_reporte['promedio_final'] = round(prom, 1)
            reprobados.append(alumno_reporte)
    return reprobados


def calcular_estadisticas_curso(lista_alumnos):
    """
    Genera métricas generales del curso.
    """
    if not lista_alumnos:
        return None

    # Crear lista plana de todos los promedios
    promedios = []
    for x in lista_alumnos:
        p = sum(x['notas']) / len(x['notas'])
        promedios.append(p)

    reporte = {
        'total_alumnos': len(lista_alumnos),
        'promedio_curso': round(sum(promedios) / len(promedios), 1),
        'mejor_promedio': round(max(promedios), 1),
        'peor_promedio': round(min(promedios), 1),
        'cantidad_aprobados': len([p for p in promedios if p >= 4.0]),
        'cantidad_reprobados': len([p for p in promedios if p < 4.0])
    }
    return reporte