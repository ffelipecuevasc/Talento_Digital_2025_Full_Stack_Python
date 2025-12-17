# Creamos una variable de texto (str) porque está entre comillas
nombre = "Felipe"  # Guardamos el nombre como texto

# Creamos una variable entera (int) porque es un número sin decimales
edad = 17  # Guardamos la edad como número entero

# Creamos una variable decimal (float) porque tiene punto decimal
altura = 1.72  # Guardamos la altura con decimales

# Creamos una variable booleana (bool) porque es True o False
es_estudiante = True  # Guardamos si la persona es estudiante

# Mostramos los valores iniciales
print("=== VALORES INICIALES ===")  # Título en pantalla
print("Nombre:", nombre)  # Mostramos el nombre
print("Edad:", edad)  # Mostramos la edad
print("Altura:", altura)  # Mostramos la altura
print("¿Es estudiante?:", es_estudiante)  # Mostramos el booleano

# Mostramos el tipo de cada variable
print("\n=== TIPOS INICIALES ===")  # Salto de línea + título
print("Tipo de nombre:", type(nombre))  # Mostramos el tipo de nombre
print("Tipo de edad:", type(edad))  # Mostramos el tipo de edad
print("Tipo de altura:", type(altura))  # Mostramos el tipo de altura
print("Tipo de es_estudiante:", type(es_estudiante))  # Mostramos el tipo del booleano

# Reasignamos valores (cambiamos el contenido de las “cajitas”)
edad = 18  # Cambiamos la edad a 18
altura = 1.75  # Cambiamos la altura a 1.75

# Mostramos los valores actualizados
print("\n=== VALORES ACTUALIZADOS ===")  # Título para separar
print("Nombre:", nombre)  # El nombre sigue igual
print("Edad:", edad)  # Edad actualizada
print("Altura:", altura)  # Altura actualizada
print("¿Es estudiante?:", es_estudiante)  # Sigue igual

# Verificamos tipos otra vez (deberían mantenerse)
print("\n=== TIPOS DESPUÉS DE REASIGNAR ===")  # Nuevo título
print("Tipo de nombre:", type(nombre))  # Sigue siendo str
print("Tipo de edad:", type(edad))  # Sigue siendo int
print("Tipo de altura:", type(altura))  # Sigue siendo float
print("Tipo de es_estudiante:", type(es_estudiante))  # Sigue siendo bool
