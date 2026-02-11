# Demo Pág. 18: Control de Errores con finally

print("--- INICIO DEMO ROBUSTA ---")

# Paso previo: Crear el archivo para leer
with open("demo_error.txt", "w") as f:
    f.write("Texto de prueba")

archivo = None

try:
    # 1. Intentamos abrir y procesar
    print("1️⃣ Abriendo archivo 'demo_error.txt'...")
    archivo = open("demo_error.txt", "r")

    # 2. Simulamos un error durante el procesamiento
    # Imagina que leemos el archivo pero algo falla en la lógica
    print("2️⃣ Procesando contenido...")

    # Simulamos un error forzado (lanzamos una excepción manual)
    # En la vida real, esto podría ser un error de formato de datos, memoria, etc.
    raise Exception("¡Error inesperado durante la lectura!")

    # Esta línea es inalcanzable
    print("Esto no se imprimirá nunca.")

except Exception as e:
    # 3. Capturamos el error para que no sea tan feo
    print(f"\n❌ Se capturó un error: {e}")

finally:
    # 4. LA GARANTÍA DE CIERRE
    # Este bloque se ejecuta SIEMPRE, haya error o no.
    print("\n🔄 Ejecutando bloque 'finally'...")

    if archivo is not None and not archivo.closed:
        archivo.close()
        print("✅ Mensaje crítico: 'Cerrando archivo...' (Recurso liberado).")

# Verificación final
if archivo.closed:
    print("\n🏁 Conclusión: El archivo terminó cerrado gracias al finally.")