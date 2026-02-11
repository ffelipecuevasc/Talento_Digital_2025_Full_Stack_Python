print("--- 🛡️ PROBANDO CONTEXT MANAGER ---")

# Usamos 'with' para crear y escribir
with open("secreto.txt", "w") as f:
    print(f"1. Dentro del bloque: ¿Está cerrado? {f.closed}") # False (Abierto)
    f.write("Este mensaje se autodestruirá... o se guardará.")

# Al salir de la indentación, el archivo se cierra solo.
print(f"2. Fuera del bloque: ¿Está cerrado? {f.closed}") # True (Cerrado)

# Intentar escribir ahora daría error
try:
    f.write("Intento fallido")
except ValueError as e:
    print(f"3. Error esperado: {e}")
    print("   (No puedes escribir en un archivo cerrado, ¡el sistema funciona!)")