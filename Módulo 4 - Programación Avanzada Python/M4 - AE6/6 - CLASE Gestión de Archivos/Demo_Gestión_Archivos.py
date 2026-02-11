import os

print("--- 🚚 INICIANDO SISTEMA DE MUDANZA ---")

# 1. PREPARACIÓN (Creamos un archivo para tener algo que mover)
# Creamos un archivo vacío llamado 'viejo.txt'
archivo = open("viejo.txt", "w")
archivo.close()
print("✅ Archivo 'viejo.txt' creado.")

# 2. RENOMBRAR (Cambio de etiqueta)
# Cambiamos el nombre en el mismo lugar
print("🏷️  Renombrando archivo...")
os.rename("viejo.txt", "nuevo.txt")
print("✅ Ahora se llama 'nuevo.txt'.")

# 3. MOVER (Cambio de ubicación)
# Primero: Necesitamos crear la carpeta destino (si no existe, os.rename falla)
# os.mkdir crea un directorio (make directory)
if not os.path.exists("carpeta_secreta"):
    os.mkdir("carpeta_secreta")
    print("📁 Carpeta 'carpeta_secreta' creada.")

# Ahora sí, movemos el archivo cambiando su ruta
print("🚚 Moviendo el archivo a su nueva casa...")
# Origen: "nuevo.txt" -> Destino: "carpeta_secreta/nuevo.txt"
os.rename("nuevo.txt", "carpeta_secreta/nuevo.txt")

print("✨ ¡Mudanza completada! Revisa la carpeta 'carpeta_secreta'.")