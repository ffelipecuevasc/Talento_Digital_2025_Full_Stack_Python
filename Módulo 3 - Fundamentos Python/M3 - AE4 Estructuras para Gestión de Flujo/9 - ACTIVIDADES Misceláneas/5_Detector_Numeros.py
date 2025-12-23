# 5. El Detector de Números Pares
# Enfoque: Operador módulo %.

maximo = int(input("Ingresa un número máximo: "))

# range(inicio, fin) no incluye el último número, por eso sumamos 1
for numero in range(1, maximo + 1):
    if numero % 2 == 0: # Si el residuo de la división por 2 es 0
        print(f"El número {numero} es par")