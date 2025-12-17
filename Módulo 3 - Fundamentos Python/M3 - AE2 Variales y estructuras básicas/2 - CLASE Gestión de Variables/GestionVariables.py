# 1) Inicialización + asignación: la variable nace con un valor
nombre = "Felipe"  # Guardamos un texto

# 2) Salida: mostramos lo que guardamos
print("Nombre guardado:", nombre)  # El programa "habla"

# 3) Entrada: le pedimos un dato al usuario
edad_texto = input("Escribe tu edad: ")  # OJO: esto llega como texto (str)

# 4) Conversión: si queremos usar la edad como número, la convertimos
edad = int(edad_texto)  # Convertimos el texto a entero

# 5) Mostramos el resultado final
print("Tu edad es:", edad)  # Ya es número, útil para cálculos