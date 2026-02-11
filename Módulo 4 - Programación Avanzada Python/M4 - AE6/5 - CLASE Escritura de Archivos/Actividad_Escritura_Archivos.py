# Demo Pág. 10: Escritura y Agregado (Append)

print("--- INICIO DEMO DE ESCRITURA ---")

# PASO 1: Crear el archivo y escribir la primera línea
# Usamos 'w' (write). Si 'notas.txt' no existe, lo crea.
print("1️⃣ Abriendo en modo 'w' para escribir la primera nota...")
archivo = open("notas.txt", "w")
archivo.write("Nota 1: Comprar leche\n") # Agregamos \n para que no quede pegado
archivo.close()
print("   -> Archivo creado y cerrado.")

# PASO 2: Agregar una segunda línea sin borrar la primera
# Usamos 'a' (append). Esto coloca el cursor al final del archivo.
print("2️⃣ Abriendo en modo 'a' para agregar la segunda nota...")
archivo = open("notas.txt", "a")
archivo.write("Nota 2: Estudiar Python\n")
archivo.close()
print("   -> Nota agregada y archivo cerrado.")

# PASO 3: Verificación (Lectura)
# Leemos para confirmar que ambas líneas están ahí.
print("3️⃣ Verificando el contenido final:")
archivo_lectura = open("notas.txt", "r")
contenido = archivo_lectura.read()
print("-" * 20)
print(contenido)
print("-" * 20)
archivo_lectura.close()

# Conclusión: Si hubiéramos usado 'w' en el paso 2, la "Nota 1" habría desaparecido.