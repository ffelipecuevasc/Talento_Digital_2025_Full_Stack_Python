# Creamos una variable de tipo texto (string) porque está entre comillas.
nombre = "Felipe"  # Guardamos un texto: el nombre de una persona.

# Creamos una variable de tipo entero (int) porque es un número sin decimales.
edad = 17  # Guardamos una edad como número entero.

# Creamos una variable de tipo decimal (float) porque tiene punto decimal.
altura = 1.72  # Guardamos una altura con decimales.

# Creamos una variable booleana (bool) porque es True/False (interruptor).
es_estudiante = True  # Guardamos una condición: sí, es estudiante.

# Mostramos los valores para comprobar que se guardaron bien.
print("Nombre:", nombre)  # Imprime el texto guardado en nombre.
print("Edad:", edad)  # Imprime el número entero guardado en edad.
print("Altura:", altura)  # Imprime el número decimal guardado en altura.
print("¿Es estudiante?:", es_estudiante)  # Imprime True o False.

# Ahora usamos type() para preguntarle a Python qué tipo es cada variable.
print("Tipo de nombre:", type(nombre))  # Muestra que nombre es <class 'str'>.
print("Tipo de edad:", type(edad))  # Muestra que edad es <class 'int'>.
print("Tipo de altura:", type(altura))  # Muestra que altura es <class 'float'>.
print("Tipo de es_estudiante:", type(es_estudiante))  # Muestra que es <class 'bool'>.

# BONUS útil: input() siempre entrega texto, aunque escribas números.
edad_texto = input("Escribe tu edad: ")  # Capturamos la edad como texto (str).

# Convertimos ese texto a entero para poder usarlo como número de verdad.
edad_numero = int(edad_texto)  # Transformamos el texto a int para cálculos y comparaciones.

# Confirmamos el tipo después de convertir.
print("Tu edad (como número):", edad_numero)  # Mostramos la edad convertida a número.
print("Tipo de tu edad convertida:", type(edad_numero))  # Verificamos que ahora es int.