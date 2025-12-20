# Definimos un precio base para la entrada.
precio_base = 5000  # Precio base en pesos (ejemplo).

# Pedimos el tipo de usuario.
tipo = input("Tipo de usuario (estudiante / adulto mayor / otro): ")  # Leemos texto del usuario.

# Normalizamos un poco el texto para evitar errores por mayúsculas.
tipo = tipo.lower()  # Pasamos a minúsculas para comparar más fácil.

# Partimos asumiendo que no hay descuento.
precio_final = precio_base  # Por defecto, el precio se mantiene igual.

# Si el usuario es estudiante, aplicamos 20% de descuento.
if tipo == "estudiante":  # Preguntamos si el tipo coincide exactamente.
    precio_final = precio_base * 0.8  # 0.8 significa “paga el 80%”.

# Si el usuario es adulto mayor, aplicamos 30% de descuento.
if tipo == "adulto mayor":  # Otra pregunta independiente.
    precio_final = precio_base * 0.7  # 0.7 significa “paga el 70%”.

# Si NO es estudiante Y NO es adulto mayor, no hay descuento.
if tipo != "estudiante" and tipo != "adulto mayor":  # Usamos and para exigir que ambas sean verdad.
    precio_final = precio_base  # Se queda igual (sin descuento).

# Mostramos el precio final.
print("Precio final de la entrada:", precio_final)  # Resultado final para el usuario.