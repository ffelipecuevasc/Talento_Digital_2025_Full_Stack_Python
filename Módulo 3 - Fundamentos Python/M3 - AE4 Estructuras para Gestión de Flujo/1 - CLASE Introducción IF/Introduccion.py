# Introducción a la estructura de decisión IF

# Pedimos la edad al usuario (input siempre devuelve texto).
edad_texto = input("Ingresa tu edad: ")  # Guardamos lo que el usuario escribió.

# Convertimos la edad a número entero para poder compararla con 18.
edad = int(edad_texto)  # Sin esto, Python no puede comparar bien texto con números.

# Preguntamos la condición: ¿edad es mayor o igual a 18?
if edad >= 18:  # Si esto es True, entra al bloque de abajo.
    print("✅ Eres mayor de edad: puedes ingresar.")  # Mensaje si cumple la condición.

# Este print está fuera del if, así que se muestra siempre (pase lo que pase).
print("Fin del programa.")  # Esto demuestra cómo el flujo continúa.