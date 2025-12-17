# “Contador de intentos de login”
# Asignación + incremento / decremento (sin while, sin for)

# 1) Variables base
intentos = 0
MAX_INTENTOS = 3
contrasena_correcta = "python123"

acceso_concedido = False

# --- Intento 1 ---
print("Intentos actuales:", intentos)
contrasena = input("Ingresa la contraseña: ")

if contrasena == contrasena_correcta:
    print("Acceso concedido.")
    acceso_concedido = True
else:
    intentos += 1
    print("Contraseña incorrecta, te quedan", MAX_INTENTOS - intentos, "intentos.")

# --- Intento 2 (solo si aún no entra y aún quedan intentos) ---
if acceso_concedido == False and intentos < MAX_INTENTOS:
    print("Intentos actuales:", intentos)
    contrasena = input("Ingresa la contraseña: ")

    if contrasena == contrasena_correcta:
        print("Acceso concedido.")
        acceso_concedido = True
    else:
        intentos += 1
        print("Contraseña incorrecta, te quedan", MAX_INTENTOS - intentos, "intentos.")

# --- Intento 3 (solo si aún no entra y aún quedan intentos) ---
if acceso_concedido == False and intentos < MAX_INTENTOS:
    print("Intentos actuales:", intentos)
    contrasena = input("Ingresa la contraseña: ")

    if contrasena == contrasena_correcta:
        print("Acceso concedido.")
        acceso_concedido = True
    else:
        intentos += 1
        # Aquí ya llegó al máximo
        print("Has alcanzado el número máximo de intentos, cuenta bloqueada.")

# Mostrar contador final
print("Intentos finales:", intentos)