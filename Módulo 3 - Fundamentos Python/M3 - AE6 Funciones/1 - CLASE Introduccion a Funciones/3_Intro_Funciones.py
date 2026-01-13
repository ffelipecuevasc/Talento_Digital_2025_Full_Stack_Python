# --- EJEMPLO 1: Función SIN Parámetros ---
# Esta es una función sencilla, como dar los "Buenos días".

def dar_bienvenida():  # 1. 'def' avisa que empieza la función. ':' abre el bloque.
    # Noten el espacio a la izquierda (indentación). ¡Estamos dentro de la función!
    print("¡Bienvenido al sistema!")   # Instrucción 1
    print("Cargando tu perfil...")     # Instrucción 2
    print("-----------------------")   # Instrucción 3

# Aquí ya no hay indentación (volvemos al margen).
# La función existe, pero si no la llamo, no pasa nada.

print("--- Inicio del programa ---")
dar_bienvenida()  # ¡LLAMADA! Apretamos el botón START con ().
print("--- Fin del programa ---")


# --- EJEMPLO 2: Función CON Parámetros ---
# Esta función es más inteligente, necesita información para trabajar.

def saludar_personalizado(nombre): # 'nombre' es el parámetro (el hueco a llenar).
    # Usamos la variable 'nombre' dentro de la función.
    print(f"Hola, {nombre}. ¡Qué gusto verte!")
    print("Espero que tengas un día genial.")

# Al llamar a la función, debemos enviarle el "argumento" (el dato real).
saludar_personalizado("Ana")    # Aquí la licuadora recibe "Ana".
saludar_personalizado("Carlos") # Aquí recibe "Carlos". Usa la misma lógica.

# Si intentas llamar a saludar_personalizado() sin nada dentro de los paréntesis...
# ¡Python te dará un error porque le falta un ingrediente!