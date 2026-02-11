# --- PASO 1: CREAR Y ESCRIBIR (Modo "w") ---
# Abrimos el archivo "diario.txt". Si no existe, se crea.
# El modo "w" (write) es peligroso: si existía, lo borra todo.
mi_archivo = open("diario.txt", "w")

# Escribimos contenido. Fíjate que necesitamos agregar "\n" para el salto de línea.
mi_archivo.write("Día 1: Hoy aprendí sobre persistencia en Python.\n")
mi_archivo.write("Día 1: Python es genial.\n")

# ¡CRUCIAL! Cerramos para guardar cambios y liberar el File Descriptor.
mi_archivo.close()

print("✅ Archivo escrito y cerrado correctamente.")

# --- PASO 2: LEER (Modo "r") ---
# Ahora abrimos en modo lectura ("r").
lectura_archivo = open("diario.txt", "r")

# Usamos .read() para traer TODO el contenido a una variable string.
contenido = lectura_archivo.read()

# Mostramos lo que había en el "cuaderno".
print("\n--- Contenido del Archivo ---")
print(contenido)
print("-----------------------------")

# Verificamos si el archivo está cerrado ANTES de cerrar (dará False)
print(f"¿El archivo está cerrado?: {lectura_archivo.closed}")

# Cerramos nuevamente.
lectura_archivo.close()

# Verificamos AHORA (dará True)
print(f"¿Y ahora?: {lectura_archivo.closed}")