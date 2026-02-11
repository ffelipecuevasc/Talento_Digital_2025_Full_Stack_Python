import os

# --- PASO PREVIO: CREACIÓN DEL ESCENARIO ---
# Creamos el archivo 'notas.txt' y la carpeta 'archivos' para que la demo funcione
with open("notas.txt", "w") as f:
    f.write("Mis apuntes importantes.")

if not os.path.exists("archivos"):
    os.mkdir("archivos") # Creamos el subdirectorio destino

print("--- INICIO DEMO PÁGINA 12 ---")

# 1. RENOMBRAR EL ARCHIVO
# Usamos os.rename para cambiar el nombre in-situ
# Sintaxis: os.rename(actual, nuevo)
print("🔄 Renombrando 'notas.txt' a 'notas_final.txt'...")
os.rename("notas.txt", "notas_final.txt")

# Verificación rápida (opcional)
if os.path.exists("notas_final.txt"):
    print("   -> ¡Nombre cambiado con éxito!")

# 2. MOVER EL ARCHIVO A UN SUBDIRECTORIO
# Para mover, usamos os.rename pero indicamos la ruta nueva en el segundo argumento.
# Queremos que vaya a la carpeta "archivos".
print("📦 Moviendo 'notas_final.txt' a la carpeta 'archivos/'...")

# Nota: En Windows usamos backslash (\) o slash (/), Python entiende ambos.
# Es buena práctica usar os.path.join, pero aquí lo haremos manual como en la demo básica.
ruta_nueva = "archivos/notas_final.txt"

os.rename("notas_final.txt", ruta_nueva)

# 3. CONFIRMACIÓN FINAL
if os.path.exists("archivos/notas_final.txt"):
    print("✅ ¡Éxito! El archivo ha sido movido correctamente.")
else:
    print("❌ Algo salió mal, no encuentro el archivo en la carpeta destino.")