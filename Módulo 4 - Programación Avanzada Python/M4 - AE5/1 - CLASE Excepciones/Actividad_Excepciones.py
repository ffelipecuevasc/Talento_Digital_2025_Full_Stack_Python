# ================================================================
# SOLUCIÓN MINI-DEMO (Página 10 del PDF M4 AE5)
# Objetivo: Provocar ZeroDivisionError y ValueError
# ================================================================
# Paso 1: Solicitamos un dato al usuario.
# OJO: 'input' devuelve texto, así que usamos 'int()' para convertirlo.
# RIESGO 1: Si el usuario escribe "hola", int() fallará -> ValueError
numero = int(input("Ingresá un número para dividir al 10: "))
# Paso 2: Realizamos la operación matemática.
# RIESGO 2: Si el usuario ingresó "0", dividir por cero es imposible -> ZeroDivisionError
resultado = 10 / numero
# Paso 3: Mostramos el resultado (solo llegamos aquí si no hubo errores)
print("El resultado de la división es:", resultado)
# --- INSTRUCCIONES PARA EL ALUMNO ---
# Ejecuta este código dos veces:
# 1. Ingresa el número 0. Observa el mensaje "ZeroDivisionError".
# 2. Ingresa la palabra "Python". Observa el mensaje "ValueError".
# ¡Acabas de descubrir las Excepciones!