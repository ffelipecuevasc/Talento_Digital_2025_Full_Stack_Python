# --- EJERCICIO INTEGRADOR 1: GESTIÓN DE ESTUDIANTES ---

# 1. Crear la base de datos vacía
# Usamos una LISTA porque necesitamos agregar más alumnos en el futuro.
estudiantes = []

# 2. Agregar estudiantes
# Cada estudiante es una TUPLA (Nombre, Edad, Ciudad) porque son datos fijos de esa persona.
# Agregamos 5 estudiantes variados:
estudiantes.append(("Ana", 25, "Santiago"))
estudiantes.append(("Luis", 30, "Valdivia"))
estudiantes.append(("Carla", 22, "Santiago"))
estudiantes.append(("Pedro", 28, "Concepción"))
estudiantes.append(("Marta", 24, "Valdivia"))

# O solicitamos al usuario que ingrese los estudiantes:
# i = 0
# while i < 5:
#    print(f"-- ESTUDIANTE {(i+1)} --")
#    nombre = input("Ingrese el nombre del estudiante: ")
#    edad = int(input("Ingrese la edad del estudiante: "))
#    ciudad = input("Ingrese la ciudad del estudiante: ")
#    tupla_estudiante = (nombre, edad, ciudad)
#    estudiantes.append(tupla_estudiante)
#    i += 1

# 3. Mostrar el registro completo
print("--- Lista de Estudiantes Registrados ---")
# Usamos un bucle 'for' para recorrer la lista y desempaquetar la tupla
for estudiante in estudiantes:
    nombre = estudiante[0]
    edad = estudiante[1]
    ciudad = estudiante[2]
    # Imprimimos con un formato limpio y legible
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# 4. Consultar estudiantes por ciudad
# Pedimos al usuario que escriba una ciudad para buscar
print("\n--- Búsqueda por Ciudad ---")
ciudad_buscada = input("Ingresa la ciudad que quieres buscar (ej. Santiago): ")
contador_ciudad = 0

# Recorremos la lista para contar las coincidencias
for estudiante in estudiantes:
    # El índice 2 de la tupla corresponde a la ciudad
    if estudiante[2].lower() == ciudad_buscada.lower(): # .lower() ayuda a ignorar mayúsculas
        contador_ciudad += 1

print(f"Total de estudiantes en {ciudad_buscada}: {contador_ciudad}")

# 5. Calcular estadísticas (Edad Promedio)
print("\n--- Estadísticas del Curso ---")
suma_edades = 0
total_estudiantes = len(estudiantes)

# Sumamos todas las edades (índice 1 de cada tupla)
for estudiante in estudiantes:
    suma_edades += estudiante[1]

# Agregar un nuevo estudiante por consola
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
ciudad = input("Ingrese la ciudad del estudiante: ")
tupla_estudiante = (nombre, edad, ciudad)
estudiantes.append(tupla_estudiante)

# Calculamos el promedio (Suma total / Cantidad de alumnos)
if total_estudiantes > 0:
    promedio = suma_edades / total_estudiantes
    print(f"La edad promedio del curso es: {promedio} años")
else:
    print("No hay estudiantes para calcular el promedio.")