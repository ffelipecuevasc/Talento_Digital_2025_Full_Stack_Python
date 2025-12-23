# --------------------------------------------
# Ejemplo 1: break en un for
# --------------------------------------------

numeros = [4, 7, 9, 12, 15]  # Creamos una lista de números
objetivo = 12  # Este es el número que queremos encontrar

for n in numeros:  # Recorremos cada número de la lista
    print("Revisando:", n)  # Mostramos el número actual que estamos revisando

    if n == objetivo:  # Si el número actual es el que buscamos...
        print("✅ Encontrado:", objetivo)  # Confirmamos que lo encontramos
        break  # Salimos del ciclo inmediatamente (no seguimos revisando lo demás)

print("Fin de la búsqueda con break")  # Esto se ejecuta después del ciclo

# --------------------------------------------
# Ejemplo 2: continue en un for
# --------------------------------------------

print("\n--- Filtrando números (ignorando impares) ---")  # Separador para que sea más claro

for n in range(1, 11):  # Recorremos números del 1 al 10
    if n % 2 != 0:  # Si el número es impar...
        continue  # Saltamos esta vuelta y seguimos con el siguiente número

    print("Número par:", n)  # Solo se imprimen los pares