# Definimos las variables base del ejercicio
a = 10  # Primer número
b = 3   # Segundo número

# Calculamos operaciones aritméticas y guardamos resultados
suma = a + b  # Sumamos a y b
resta = a - b  # Restamos b a a
multiplicacion = a * b  # Multiplicamos a por b
division = a / b  # Dividimos a entre b (da float normalmente)
modulo = a % b  # Obtenemos el resto de dividir a entre b

# Mostramos resultados en pantalla
print("=== OPERADORES ARITMÉTICOS ===")  # Título
print("a =", a)  # Mostramos a
print("b =", b)  # Mostramos b
print("Suma (a + b):", suma)  # Resultado suma
print("Resta (a - b):", resta)  # Resultado resta
print("Multiplicación (a * b):", multiplicacion)  # Resultado multiplicación
print("División (a / b):", division)  # Resultado división
print("Módulo (a % b):", modulo)  # Resultado módulo

# BONUS: operadores de asignación (actualizamos a sin escribir tanto)
print("\n=== OPERADORES DE ASIGNACIÓN (BONUS) ===")  # Nuevo título

a += 5  # Equivale a: a = a + 5
print("Después de a += 5, a =", a)  # Mostramos el nuevo valor

a *= 2  # Equivale a: a = a * 2
print("Después de a *= 2, a =", a)  # Mostramos el nuevo valor

a %= 4  # Equivale a: a = a % 4 (nos quedamos con el resto)
print("Después de a %= 4, a =", a)  # Mostramos el nuevo valor

# BONUS 2: comparación simple para saber si a es par
# Un número es par si al dividirlo por 2 el resto es 0
es_par = (a % 2 == 0)  # Comparación: devuelve True o False
print("\n¿El valor final de a es par?:", es_par)  # Mostramos la respuesta