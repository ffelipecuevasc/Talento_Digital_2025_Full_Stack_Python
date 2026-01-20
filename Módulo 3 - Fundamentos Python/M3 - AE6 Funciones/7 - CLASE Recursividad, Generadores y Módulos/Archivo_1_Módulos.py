# --- ARCHIVO: 4_Módulos_Archivo_1 ---
# Este archivo contiene solo la LÓGICA PURA.
# No tiene inputs ni prints.

def calcular_promedio(nota1, nota2, nota3):
    """Recibe 3 notas y devuelve el promedio redondeado a 1 decimal."""
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return round(promedio, 1)

def obtener_situacion_final(promedio):
    """
    Define si el alumno aprueba o reprueba según el reglamento.
    Escala chilena: 1.0 a 7.0 (Aprobación con 4.0)
    """
    if promedio >= 4.0:
        return "🎓 APROBADO"
    else:
        return "📚 REPROBADO (Debe repetir)"
