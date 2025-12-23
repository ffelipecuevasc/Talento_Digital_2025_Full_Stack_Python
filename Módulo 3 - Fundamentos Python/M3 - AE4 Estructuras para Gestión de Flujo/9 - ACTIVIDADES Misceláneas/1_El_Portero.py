# 1. El Portero de la Discoteca
# Enfoque: Normalización de entradas de texto y lógica booleana.

# Solicitamos datos. Convertimos la edad a entero.
edad = int(input("¿Qué edad tienes? "))
trae_identificacion = input("¿Traes identificación? (si/no): ").lower()

# Condición compuesta: Ambas deben ser verdaderas
if edad >= 18 and trae_identificacion == "si":
    print("¡Adelante, disfruta la fiesta!")
else:
    print("Lo siento, hoy no entras.")