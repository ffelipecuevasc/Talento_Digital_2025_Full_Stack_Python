# Preparación previa: Crearemos el archivo 'prueba.txt' para que la demo no falle.
# (En un caso real, este archivo ya existiría en tu computador).
with open("prueba.txt", "w") as f:
    f.write("Hola Mundo!\nEsta es una prueba de lectura.\nPython es divertido.")

print("--- INICIO DE LA DEMO (Pág. 15) ---\n")

try:
    # 1. Usar open() en modo "r" para abrir el archivo "prueba.txt"
    # El modo 'r' es lectura. Si el archivo no está, saltaría al 'except'.
    archivo_demo = open("prueba.txt", "r")

    # 2. Leer el contenido usando read()
    # Esto toma todo el texto del archivo y lo guarda en la variable 'contenido_completo'
    contenido_completo = archivo_demo.read()

    # 3. Imprimir el contenido en consola
    print("Contenido del archivo:")
    print(contenido_completo)

    # 4. Cerrar el archivo usando close()
    # Paso vital para liberar el recurso del sistema.
    archivo_demo.close()

    # Observación importante del PDF: Verificar si se cerró correctamente.
    # El atributo .closed devuelve True si ya se cerró.
    if archivo_demo.closed:
        print("\n✅ Éxito: El archivo se ha cerrado correctamente.")
    else:
        print("\n⚠️ Alerta: El archivo sigue abierto.")

except FileNotFoundError:
    # El PDF menciona que si no existe, lanza FileNotFoundError.
    # Aquí capturamos ese error para mostrar un mensaje amigable.
    print("❌ Error: No se encontró el archivo 'prueba.txt'. Asegúrate de crearlo primero.")