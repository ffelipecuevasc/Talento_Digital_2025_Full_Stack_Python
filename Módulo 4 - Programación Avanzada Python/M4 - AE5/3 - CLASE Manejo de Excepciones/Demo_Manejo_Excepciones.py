# ==============================================================================
# DEMO: VALIDACIÓN DE ENTRADA NUMÉRICA (Página 18 del PDF M4 AE5)
# Objetivo: Solicitar un número y capturar el error si el usuario escribe texto.
# ==============================================================================
print("--- INICIO DEL PROGRAMA DE VALIDACIÓN ---")
try:
    # ZONA RIESGOSA (try)
    # 1. Pedimos el dato al usuario.
    entrada = input("Por favor, ingresá tu edad (solo números enteros): ")
    # 2. Intentamos convertirlo a entero.
    # AQUÍ es donde puede ocurrir el 'accidente' si 'entrada' es "hola" o "10.5"
    edad = int(entrada)
    # Si la línea anterior funcionó, el programa sigue aquí:
    print(f"¡Genial! Tienes {edad} años (o eso dices).")
except ValueError:
    # ZONA DE RESCATE (except)
    # Si falló la conversión a int(), saltamos directamente aquí.
    # En lugar de un error rojo y feo, mostramos amabilidad:
    print(" ¡Epa! Eso no parece un número entero válido.")
    print("Por ejemplo, si tienes 25 años, escribe solo: 25")
    print("--- FIN DEL PROGRAMA (El show continuó sin crashear) ---")
# --- INSTRUCCIONES DE PRUEBA PARA EL ALUMNO ---
# Ejecuta el código 3 veces:
# 1. Ingresa "25" -> Verás el mensaje de éxito.
# 2. Ingresa "veinte" -> Se activará el bloque 'except' (ValueError).
# 3. Ingresa "10.5" -> Se activará el 'except' (ValueError) porque int() no acepta decimales en texto.
