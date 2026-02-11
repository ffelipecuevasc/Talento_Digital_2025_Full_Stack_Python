# --- PREPARACIÓN ---
# Creamos un archivo de prueba para el ejemplo
with open("datos_usuario.txt", "w") as f:
    f.write("Nombre: Juan Perez\nEdad: 28\nCiudad: Santiago")

# --- CÓDIGO EN VIVO ---

# 1. Abrimos el archivo en modo lectura
mi_archivo = open("datos_usuario.txt", "r")

# 2. Consultamos sus "Metadatos" (Atributos)
print(f"📄 Nombre del archivo: {mi_archivo.name}")   # Imprime: datos_usuario.txt
print(f"🛠️ Modo de apertura: {mi_archivo.mode}")     # Imprime: r
print(f"🔒 ¿Está cerrado?: {mi_archivo.closed}")   # Imprime: False

print("-" * 20)

# 3. Leemos una línea para probar (Mueve el cursor)
primera_linea = mi_archivo.readline()
print(f"📖 Leí esto: {primera_linea.strip()}") # .strip() quita el salto de línea sobrante

# 4. Cerramos
mi_archivo.close()

# 5. Verificamos el cierre
print(f"🔒 ¿Está cerrado ahora?: {mi_archivo.closed}") # Imprime: True