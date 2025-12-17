# Guardamos dos números para operar con ellos
a = 10  # Primer número
b = 3   # Segundo número

# SUMA
suma = a + b  # Sumamos a y b
print("Suma:", suma)  # Mostramos el resultado

# RESTA
resta = a - b  # Restamos b a a
print("Resta:", resta)

# MULTIPLICACIÓN
multiplicacion = a * b  # Multiplicamos a por b
print("Multiplicación:", multiplicacion)

# DIVISIÓN
division = a / b  # Dividimos a entre b (normalmente da float)
print("División:", division)

# MÓDULO (resto)
modulo = a % b  # Calculamos el resto de dividir a entre b
print("Módulo (resto):", modulo)

# EJEMPLO CLÁSICO: saber si un número es par o impar usando MOD (operador módulo)
numero = 8  # Probamos con 8
es_par = (numero % 2 == 0)  # Si el resto al dividir por 2 es 0, entonces es par
print("¿El número es par?:", es_par)