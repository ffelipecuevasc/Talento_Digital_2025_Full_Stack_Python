# Demo Pág. 15: Reescribiendo con 'with'

print("--- INICIO DEMO 'WITH' ---")

# 1. ESCRITURA SEGURA
# Antes hacíamos: archivo = open(...) -> write -> close()
# Ahora hacemos todo en un solo bloque:
print("✍️  Escribiendo datos usando 'with'...")
with open("demo_with.txt", "w") as archivo:
    archivo.write("Línea 1: Usando Context Managers\n")
    archivo.write("Línea 2: Código más limpio y seguro\n")
    # No hace falta archivo.close(), ¡es automático!

print("   -> Archivo escrito y cerrado automáticamente.")

# 2. LECTURA SEGURA
print("📖 Leyendo datos usando 'with'...")
with open("demo_with.txt", "r") as archivo_lectura:
    contenido = archivo_lectura.read()
    print("-" * 20)
    print(contenido.strip())
    print("-" * 20)

# Verificación final (solo para demostrar que funcionó)
if archivo_lectura.closed:
    print("✅ Confirmado: El archivo de lectura se cerró solo al terminar el bloque.")