# ============================================
# 2) “Asistente de feedback de evaluaciones”
# Objetivo: if/elif/else + match-case
# ============================================

# Entradas
nota_texto = input("Ingresa la nota (1.0 a 7.0): ")
nota = float(nota_texto)

entrega = input("¿Entregaste a tiempo o con atraso? (tiempo/atraso): ").lower()

# 1) Clasificamos la nota con if/elif/else
categoria = ""
if nota >= 6.0:
    categoria = "Excelente"
elif nota >= 5.0:
    categoria = "Bueno"
elif nota >= 4.0:
    categoria = "Suficiente"
else:
    categoria = "Insuficiente"

# 2) Feedback principal con match-case (según la categoría)
mensaje = ""

match categoria:
    case "Excelente":
        mensaje = "¡Excelente trabajo! Se nota dominio del contenido. "
        mensaje += "Desafío extra: intenta resolver un ejercicio parecido sin mirar apuntes. "

        # Ajuste por entrega
        if entrega == "tiempo":
            mensaje += "Además, muy buena gestión del tiempo. "
        else:
            mensaje += "Ojo con los plazos: trata de planificar tu semana con anticipación. "

        mensaje += "Sugerencia: comparte tu estrategia de estudio con un compañero."

    case "Bueno":
        mensaje = "¡Buen resultado! Vas por muy buen camino. "
        mensaje += "Te recomiendo reforzar los puntos donde dudaste. "

        if entrega == "tiempo":
            mensaje += "Excelente que hayas entregado a tiempo. "
        else:
            mensaje += "Para la próxima, intenta partir antes para evitar atrasos. "

        mensaje += "Sugerencia: practica 2 ejercicios más del mismo tema."

    case "Suficiente":
        mensaje = "Vas avanzando, ¡no te preocupes! Esto se construye paso a paso. "
        mensaje += "Hay bases, pero falta reforzar algunos conceptos clave. "

        if entrega == "tiempo":
            mensaje += "Bien por entregar a tiempo, eso ayuda mucho. "
        else:
            mensaje += "El atraso puede afectar tu aprendizaje: intenta hacer un plan diario corto. "

        mensaje += "Sugerencia: repasa el contenido y vuelve a intentar un ejercicio guiado."

    case _:
        # Insuficiente (y cualquier caso inesperado)
        mensaje = "Tranquilo/a: equivocarse es parte del aprendizaje. "
        mensaje += "Lo importante es detectar qué falló y mejorar. "

        if entrega == "tiempo":
            mensaje += "Al menos entregaste a tiempo, ¡buen hábito! "
        else:
            mensaje += "Primero mejora la planificación para llegar a tiempo. "

        mensaje += "Sugerencia concreta: repasa condicionales (if/elif/else) y practica con casos simples."

# Salida esperada
print("\n=== FEEDBACK DE EVALUACIÓN ===")
print("Nota:", nota)
print("Categoría:", categoria)
print("Entrega:", entrega)
print("Feedback:", mensaje)