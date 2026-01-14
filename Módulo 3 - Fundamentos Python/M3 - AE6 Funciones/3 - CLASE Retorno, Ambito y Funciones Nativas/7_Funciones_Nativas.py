# --- SISTEMA DE REGISTRO BÁSICO ---

print("--- Inicio del Registro ---")

# 1. Usamos input() para obtener datos (El Micrófono)
# OJO: input() SIEMPRE devuelve texto (str), aunque escribas números.
nombre = input("Ingresa tu nombre: ")
edad_texto = input("Ingresa tu edad: ")

# 2. Usamos int() para corregir el dato (El Transformador)
# Convertimos el texto "25" en el número 25 para poder calcular.
edad_numero = int(edad_texto)

# 3. Usamos range() y list() (Generador y Contenedor)
# Imaginemos que queremos generar códigos para sus 3 primeros tickets de sorteo.
# range(1, 4) genera los números 1, 2 y 3.
# list() los mete en una cajita.
tickets = list(range(1, 4))

# 4. Usamos len() (La Regla)
# Queremos saber cuántas letras tiene su nombre para darle un premio extra.
largo_nombre = len(nombre)

# 5. Usamos str() para preparar el mensaje final
# Convertimos el número de tickets en texto para unirlo al mensaje.
mensaje_tickets = "Tus tickets son: " + str(tickets)

print("\n--- Resumen ---")
print(f"Bienvenido, {nombre}.")
print(f"El próximo año tendrás {edad_numero + 1} años.") # Aquí sumamos porque ya es int.
print(f"Tu nombre tiene {largo_nombre} letras.")
print(mensaje_tickets)