# Definimos una variable simple
numero = 10
texto = "Hola Python"

# Usamos isinstance para preguntar: "¿Eres un número entero?"
resultado_numero = isinstance(numero, int)
print(f"¿Es '10' un número entero? {resultado_numero}")
# Salida: True

# Preguntamos: "¿Eres un texto (string)?"
resultado_texto = isinstance(texto, str)
print(f"¿Es 'Hola Python' un texto? {resultado_texto}")
# Salida: True

# Ahora la prueba de fuego: Preguntamos algo falso
# "¿Es el texto un número entero?"
es_impostor = isinstance(texto, int)
print(f"¿Es el texto un número? {es_impostor}") 