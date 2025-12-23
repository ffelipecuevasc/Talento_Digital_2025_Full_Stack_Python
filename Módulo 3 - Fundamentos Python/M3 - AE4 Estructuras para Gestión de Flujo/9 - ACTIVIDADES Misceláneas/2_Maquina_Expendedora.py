# 2. La Máquina Expendedora
# Enfoque: Estructura match.

print("Opciones: A (Refresco), B (Papas), C (Galletas)")
opcion = input("Elige una opción: ").upper() # Convertimos a mayúscula para evitar errores

match opcion:
    case "A":
        print("Aquí tienes tu refresco 🥤")
    case "B":
        print("Aquí tienes tus papas fritas 🍟")
    case "C":
        print("Aquí tienes tus galletas 🍪")
    case _:
        # Case default para capturar cualquier otra entrada
        print("Opción no reconocida ❌")