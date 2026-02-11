# --- SIMULACIÓN DE CRISIS ---
print("--- 💥 INICIANDO SIMULACIÓN DE ERROR ---")

archivo = None  # Inicializamos la variable por seguridad

try:
    print("1. Abriendo archivo...")
    archivo = open("datos_vitales.txt", "w")

    print("2. Escribiendo datos...")
    archivo.write("Datos importantes...")

    # ¡BUM! Provocamos un error fatal aquí
    print("3. Intentando una operación matemática loca...")
    resultado = 10 / 0  # Error: ZeroDivisionError

    # Esta línea NUNCA se ejecutará porque el programa saltó al except
    print("4. Cerrando archivo normalmente (Nunca llegaré aquí)")
    archivo.close()

except ZeroDivisionError:
    print("\n🚨 ¡ALERTA! Ocurrió una división por cero.")
    print("   -> El programa ha interrumpido su flujo normal.")

finally:
    # ESTO ES LO IMPORTANTE:
    # Aunque hubo un error arriba, Python SIEMPRE pasa por aquí.
    print("\n🧹 LIMPIEZA (Bloque finally):")
    if archivo and not archivo.closed:
        archivo.close()
        print("✅ Archivo cerrado de emergencia exitosamente.")
    else:
        print("ℹ️ El archivo ya estaba cerrado o no se abrió.")

print("\n--- Fin de la simulación ---")