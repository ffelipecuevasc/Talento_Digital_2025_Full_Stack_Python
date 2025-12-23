# 9. La Contraseña Segura
# Enfoque: Bucle infinito controlado.

secreta = "python123"

while True:
    intento = input("Introduce la contraseña: ")

    if intento == secreta:
        print("Acceso concedido 🔓")
        break  # Única forma de salir del bucle
    else:
        print("Contraseña incorrecta, intenta de nuevo 🔒")