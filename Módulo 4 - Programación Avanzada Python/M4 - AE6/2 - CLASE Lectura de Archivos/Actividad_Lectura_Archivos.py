# --- PASO 0: CREAR EL ARCHIVO DE PRUEBA ---
# Creamos un archivo con varias líneas para notar la diferencia.
with open("prueba.txt", "w") as f:
    f.write("Línea 1: Python es genial\n")
    f.write("Línea 2: Aprender es crecer\n")
    f.write("Línea 3: Archivos dominados")

print("--- INICIO DEMO COMPARATIVA (Pág. 19) ---\n")

# --- PRUEBA 1: Usando read() ---
print("1️⃣ Probando read():")
archivo = open("prueba.txt", "r")
contenido_string = archivo.read()  # Lee TODO de golpe
print(f"Tipo de dato: {type(contenido_string)}") # <class 'str'>
print(f"Contenido:\n{contenido_string}")
archivo.close() # Cerramos para reiniciar
print("-" * 30)

# --- PRUEBA 2: Usando readline() ---
print("2️⃣ Probando readline():")
archivo = open("prueba.txt", "r")
linea_1 = archivo.readline() # Lee solo la primera línea
linea_2 = archivo.readline() # Lee la segunda línea (el cursor avanzó)
print(f"Tipo de dato: {type(linea_1)}") # <class 'str'>
print(f"Primera lectura: {linea_1.strip()}") # strip() para quitar el doble enter visual
print(f"Segunda lectura: {linea_2.strip()}")
archivo.close()
print("-" * 30)

# --- PRUEBA 3: Usando readlines() ---
print("3️⃣ Probando readlines():")
archivo = open("prueba.txt", "r")
contenido_lista = archivo.readlines() # Convierte el archivo en LISTA
print(f"Tipo de dato: {type(contenido_lista)}") # <class 'list'>
print(f"Contenido (Lista cruda): {contenido_lista}")

# Podemos iterar sobre la lista
print("\nIterando la lista:")
for i, linea in enumerate(contenido_lista):
    print(f"Índice {i}: {linea.strip()}")

archivo.close()
print("\n✅ Demo finalizada con éxito.")