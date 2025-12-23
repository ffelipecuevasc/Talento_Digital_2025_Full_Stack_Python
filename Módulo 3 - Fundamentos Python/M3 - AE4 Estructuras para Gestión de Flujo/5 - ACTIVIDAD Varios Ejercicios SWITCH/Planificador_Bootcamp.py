# ============================================
# 1) “Planificador diario del Bootcamp”
# Objetivo: match-case + if/elif/else
# ============================================

# Pedimos datos de entrada
dia = input("Ingresa el día de la semana (lunes, martes, ...): ").lower()
modulo_texto = input("Ingresa el número de módulo (1, 2, 3...): ")
modulo = int(modulo_texto)

tema_principal = ""
tipo_actividad = ""
recomendacion = ""

# Usamos match/case para definir el "tema base" según el día
match dia:
    case "lunes":
        tema_principal = "Python"
        # Ajustamos mensaje según módulo
        if modulo == 1:
            tema_principal = "Introducción a Python"
            tipo_actividad = "Clase sincrónica en vivo"
            recomendacion = "Ten listo VSCode y practica variables e input()."
        elif modulo == 2:
            tema_principal = "Python: práctica guiada"
            tipo_actividad = "Trabajo autónomo"
            recomendacion = "Repasa apuntes y resuelve ejercicios cortos."
        else:
            tema_principal = "Python aplicado (Django / Proyecto)"
            tipo_actividad = "Clase sincrónica en vivo"
            recomendacion = "Revisa el material antes de conectarte y ten tu proyecto a mano."

    case "miércoles" | "miercoles":
        tema_principal = "HTML/CSS"
        if modulo == 1:
            tema_principal = "Introducción a HTML"
            tipo_actividad = "Clase sincrónica en vivo"
            recomendacion = "Ten listo tu editor y una carpeta de proyecto."
        elif modulo == 2:
            tema_principal = "CSS y estilos básicos"
            tipo_actividad = "Trabajo autónomo"
            recomendacion = "Practica selectores y prueba cambios en el navegador."
        else:
            tema_principal = "Integración Front + Back (enfoque proyecto)"
            tipo_actividad = "Día de entrega o quiz"
            recomendacion = "Ordena tu código y revisa requisitos de la entrega."

    case "viernes":
        tema_principal = "Proyecto / Revisión"
        if modulo == 1:
            tema_principal = "Mini-proyecto y repaso"
            tipo_actividad = "Trabajo autónomo"
            recomendacion = "Organiza tus archivos y deja comentarios claros."
        elif modulo == 2:
            tema_principal = "Revisión + ejercicios integradores"
            tipo_actividad = "Clase sincrónica en vivo"
            recomendacion = "Llega con tus dudas anotadas para aprovechar la clase."
        else:
            tema_principal = "Proyecto final / Revisión avanzada"
            tipo_actividad = "Día de entrega o quiz"
            recomendacion = "Valida tu solución con casos de prueba antes de enviar."

    case _:
        # Caso por defecto si el día no coincide con los esperados
        tema_principal = "Sin planificación definida"
        tipo_actividad = "Por definir"
        recomendacion = "Revisa que el día esté bien escrito (ej: lunes, miércoles, viernes)."

# Salida esperada
print("\n=== PLANIFICADOR DEL BOOTCAMP ===")
print("Día:", dia)
print("Módulo:", modulo)
print("Tema principal:", tema_principal)
print("Tipo de actividad:", tipo_actividad)
print("Recomendación:", recomendacion)