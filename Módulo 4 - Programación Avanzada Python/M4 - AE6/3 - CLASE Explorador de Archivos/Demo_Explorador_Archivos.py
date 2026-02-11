import os  # Importamos 'os' para interactuar con el sistema operativo (necesario para ver el peso del archivo)
import time  # Importamos 'time' solo para darle un efecto dramático a la lectura línea por línea (opcional)

print("🔍 --- EXPLORADOR DE ARCHIVOS SIMPLE --- 🔍")

# 1. Solicitamos el nombre del archivo al usuario
nombre_archivo = input("Por favor, ingresa el nombre del archivo a inspeccionar (ej. prueba.txt): ")

try:
    # 2. Intentamos abrir el archivo en modo lectura
    # Usamos 'try' porque el usuario podría escribir un nombre que no existe.
    archivo = open(nombre_archivo, "r")

    print("\n✅ ¡Archivo encontrado con éxito!")
    print("-" * 40)

    # 3. Mostramos los atributos del objeto archivo (Metadata)
    print(f"📄 Nombre: {archivo.name}")
    print(f"🛠️  Modo: {archivo.mode}")
    print(f"🔒 Cerrado: {archivo.closed} (Aún está abierto, ¡cuidado!)")

    # 4. Obtenemos el tamaño del archivo en bytes
    # os.stat(ruta).st_size nos devuelve el peso exacto.
    peso_bytes = os.stat(nombre_archivo).st_size
    print(f"⚖️  Peso: {peso_bytes} bytes")
    print("-" * 40)

    # 5. TOMA DE DECISIÓN INTELIGENTE
    print("\n🧠 Analizando la mejor estrategia de lectura...")

    if peso_bytes < 500:
        # ESTRATEGIA A: Archivo pequeño -> Leer todo de una vez
        print("🟢 El archivo es pequeño (< 500 bytes). Usando read()...")
        print("--- CONTENIDO ---")
        contenido = archivo.read()
        print(contenido)
        print("-----------------")

    else:
        # ESTRATEGIA B: Archivo grande -> Leer línea por línea
        print("🟠 El archivo es grande (> 500 bytes). Usando readline() para ahorrar memoria...")
        print("--- CONTENIDO (Línea por línea) ---")

        # Bucle infinito que se rompe cuando no hay más líneas
        while True:
            linea = archivo.readline()

            if not linea:  # Si readline devuelve vacío, llegamos al final
                break

            print(linea.strip())  # strip() quita el salto de línea doble
            # time.sleep(0.1) # Descomentar para ver el efecto "Matrix" de carga

        print("-----------------------------------")

    # 6. Cierre del archivo (¡OBLIGATORIO!)
    archivo.close()

    # Verificación final
    if archivo.closed:
        print(f"\n🔒 Archivo '{nombre_archivo}' cerrado correctamente. Memoria liberada.")

except FileNotFoundError:
    # Capturamos el error si el archivo no existe para que el programa no colapse feo.
    print(f"\n❌ ERROR: El archivo '{nombre_archivo}' no existe en este directorio.")
    print("💡 Pista: Revisa que el nombre esté bien escrito y incluya la extensión (ej. .txt)")

except Exception as e:
    # Capturamos cualquier otro error inesperado
    print(f"\n⚠️ Ocurrió un error inesperado: {e}")