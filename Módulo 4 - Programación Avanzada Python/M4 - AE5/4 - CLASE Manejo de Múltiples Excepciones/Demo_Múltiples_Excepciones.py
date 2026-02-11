# ==============================================================================
# DEMO: CAPTURA MÚLTIPLE Y BUENAS PRÁCTICAS
# Objetivo: Manejar distintos errores con respuestas diferentes y específicas.
# ==============================================================================
print("--- INICIANDO CALCULADORA SEGURA ---")
# BUENA PRÁCTICA 1: Definimos las variables fuera del try para mantener el orden.
numerador = 100
try:
    # BUENA PRÁCTICA 2: El try es CORTO. Solo envuelve la interacción peligrosa.
    dato_usuario = input("Vamos a dividir 100 por tu número. Ingresa el divisor: ")
    # Riesgo A: Conversión (puede fallar si es texto)
    divisor = int(dato_usuario)
    # Riesgo B: Cálculo (puede fallar si es 0)
    resultado = numerador / divisor
    print(f"¡Éxito! El resultado es: {resultado}")
    # ESPECIALISTA 1: Atiende solo problemas de "texto en lugar de números"
except ValueError:
    print(" Error de TIPO: Debes ingresar un número entero, no letras ni símbolos.")
    # ESPECIALISTA 2: Atiende solo problemas de matemáticas imposibles
except ZeroDivisionError:
    print(" Error MATEMÁTICO: No es posible dividir por cero. Intenta con otro número.")
    # GENÉRICO (El último recurso): Atrapa cualquier cosa rara que no sean las anteriores
except Exception as e:
    # BUENA PRÁCTICA 3: Si usamos genérico, mostramos qué pasó (la variable 'e')
    print(f" Ocurrió un error inesperado (Detalles: {e})")
    print("--- Fin del proceso ---")
# --- INSTRUCCIONES PARA EL ALUMNO ---
# Prueba este código 3 veces para activar cada bloque:
# 1. Ingresa "hola" -> Se activa ValueError.
# 2. Ingresa "0" -> Se activa ZeroDivisionError.
# 3. Ingresa "5" -> Todo funciona (Camino feliz).