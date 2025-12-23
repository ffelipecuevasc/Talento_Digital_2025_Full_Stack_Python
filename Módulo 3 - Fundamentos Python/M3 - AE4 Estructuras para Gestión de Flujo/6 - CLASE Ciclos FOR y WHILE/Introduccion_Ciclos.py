# --------------------------------------------
# 0) "pass" (marcador de pendiente)
# --------------------------------------------

edad = 17  # Guardamos una edad de ejemplo para probar el if

if edad >= 18:  # Si la persona es mayor o igual a 18...
    print("Puedes entrar.")  # Mostramos un mensaje
else:  # Si no cumple la condición...
    pass  # "Por ahora no hago nada" (sirve como placeholder)

# --------------------------------------------
# 1) Sin ciclo vs con ciclo (la idea "sin for" vs "con for")
# --------------------------------------------

print("\n--- Sin ciclo (repetición manual) ---")  # Título para separar la salida
print("Hola, Felipe")  # Repetimos a mano (esto se vuelve tedioso)
print("Hola, Ana")  # Otra línea repetida
print("Hola, Diego")  # Otra línea repetida

print("\n--- Con ciclo for (repetición automática) ---")  # Título para separar la salida
nombres = ["Felipe", "Ana", "Diego"]  # Creamos una lista con nombres

for nombre in nombres:  # Por cada nombre dentro de la lista nombres...
    print("Hola,", nombre)  # Saludamos usando el nombre actual

# --------------------------------------------
# 2) for + range(): repetir un número definido de veces
# --------------------------------------------

print("\n--- for con range() (repetir 5 veces) ---")  # Título para separar la salida

for i in range(1, 6):  # range(1, 6) genera números del 1 al 5 (el 6 NO se incluye)
    print("Repetición número:", i)  # Mostramos el número de repetición

# --------------------------------------------
# 3) for recorriendo una lista + enumerate(): número de posición + valor
# --------------------------------------------

print("\n--- for con enumerate() (posición + valor) ---")  # Título para separar la salida
frutas = ["Manzana", "Plátano", "Uva"]  # Creamos una lista de frutas

for indice, fruta in enumerate(frutas, start=1):  # enumerate da (posición, valor) y start=1 comienza en 1
    print(f"Fruta {indice}: {fruta}")  # Imprimimos la fruta con su número

# --------------------------------------------
# 4) while: repetir "mientras" se cumpla una condición
# --------------------------------------------

print("\n--- while (contador del 1 al 5) ---")  # Título para separar la salida
contador = 1  # Partimos el contador desde 1

while contador <= 5:  # Mientras el contador sea menor o igual a 5...
    print("Contador:", contador)  # Mostramos el valor actual del contador
    contador += 1  # Aumentamos el contador en 1 para que el while avance y no se quede infinito
