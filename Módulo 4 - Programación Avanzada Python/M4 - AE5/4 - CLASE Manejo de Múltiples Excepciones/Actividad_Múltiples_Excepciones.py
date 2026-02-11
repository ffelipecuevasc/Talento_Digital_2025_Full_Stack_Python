# ==============================================================================
# ACTIVIDAD N° 1: DIVISIÓN SEGURA (Página 23 del PDF M4 AE5)
# Objetivo: Realizar una división manejando errores de tipo y matemáticos,
# asegurando que el programa siempre termine limpiamente.
# ==============================================================================
def realizar_division_segura():
    print("--- INICIANDO CALCULADORA SEGURA ---")
    while True: # Opcional: Usamos un bucle para permitir reintentos si se desea
        try:
            # 1. SOLICITUD DE DATOS (ZONA DE RIESGO A)
            # Pedimos los números. Si el usuario ingresa texto, int() fallará.
            num1 = int(input("Ingresa el primer número (dividendo): "))
            num2 = int(input("Ingresa el segundo número (divisor): "))
            # 2. OPERACIÓN MATEMÁTICA (ZONA DE RIESGO B)
            # Si num2 es 0, esta línea lanzará un error matemático.
            resultado = num1 / num2
        except ValueError:
            # CAPTURA ESPECÍFICA 1: Entrada no numérica
            # Este bloque se activa si falla la conversión int().
            print(" Error: Debes ingresar solamente números enteros válidos.")
        except ZeroDivisionError:
            # CAPTURA ESPECÍFICA 2: División por cero
            # Este bloque se activa si num2 es 0.
            print(" Error: No es posible dividir por cero. Intenta con otro divisor.")
        else:
            # BLOQUE ELSE: El camino del éxito
            # Se ejecuta SOLO si NO hubo ninguna excepción en el bloque try.
            # Es el lugar ideal para mostrar el resultado final.
            print(f" ¡Éxito! El resultado de la división es: {resultado:.2f}")
            break # Rompemos el bucle
        finally:
            # BLOQUE FINALLY: La limpieza final
            # Se ejecuta SIEMPRE, haya ocurrido un error o no.
            # Útil para cerrar archivos, conexiones o despedirse.
            print("--- Proceso de cálculo finalizado (Bloque Finally) ---\n")
# Ejecutamos la función para probar la actividad
realizar_division_segura()