# Demostración de lo que se puede lograr con Python y Operadores

# 1) Mostramos un saludo para que el usuario sepa que el programa empezó.
print("¡Hola! Bienvenido/a a esta demostración")

# 2) Pedimos un dato al usuario.
# input() SIEMPRE devuelve texto (string), aunque el usuario escriba números.
nombre = input("¿Cómo te llamas? ")

# 3) Imprimimos usando el dato capturado.
print("Mucho gusto,", nombre)

# 4) Pedimos un número, pero ojo: llega como texto.
edad_texto = input("¿Qué edad tienes? ")

# 5) Convertimos ese texto a número entero para poder usarlo como número.
edad = int(edad_texto)

# 6) Tomamos una decisión simple (aquí la indentación es CLAVE).
# Si no indentas bien, Python se confunde y te lanza error.
if edad >= 18:
    print("Eres mayor de edad. ✅")
else:
    print("Eres menor de edad. ✅")

# 7) Cerramos con un mensaje final.
print("¡Listo! Acabas de usar print(), input(), conversión y una condición usando operadores")