# --------------------------------------------
# ACTIVIDAD: Cajero automático con PIN (máximo 3 intentos)
# --------------------------------------------

# 1) Definimos el PIN correcto (en un cajero real esto estaría protegido en el sistema)
PIN_CORRECTO = "1234"  # Guardamos el PIN correcto como texto para comparar fácil con input()

# 2) Definimos el máximo de intentos permitidos
MAX_INTENTOS = 3  # El usuario solo puede equivocarse 3 veces

# 3) Creamos un contador de intentos
intentos = 0  # Partimos en 0 porque todavía no se ha intentado nada

# 4) Creamos un ciclo while que se repetirá mientras queden intentos
while intentos < MAX_INTENTOS:
    # 5) Pedimos al usuario que ingrese el PIN
    pin_ingresado = input("🔐 Ingresa tu PIN (4 dígitos): ")  # input() siempre devuelve texto

    # 6) Sumamos 1 intento porque el usuario ya hizo un intento (correcto o no)
    intentos += 1  # Esto es clave para que el while avance y no se quede infinito

    # 7) Verificamos si el PIN ingresado es correcto
    if pin_ingresado == PIN_CORRECTO:
        # 8) Si es correcto, mostramos mensaje de éxito
        print("✅ PIN correcto. Acceso concedido. ¡Bienvenido/a!")

        # 9) Salimos del ciclo con break porque ya no tiene sentido seguir preguntando
        break

    else:
        # 10) Si el PIN es incorrecto, avisamos y mostramos intentos restantes
        intentos_restantes = MAX_INTENTOS - intentos  # Calculamos cuántos intentos quedan
        print("❌ PIN incorrecto.")

        # 11) Si todavía quedan intentos, se lo mostramos al usuario
        if intentos_restantes > 0:
            print(f"Te quedan {intentos_restantes} intento(s). Intenta nuevamente.\n")

# 12) IMPORTANTE:
#     Si el while termina "sin break", significa que el usuario agotó los 3 intentos.
#     ¿Cómo sabemos eso? Porque intentos llegó a MAX_INTENTOS y nunca se cumplió el PIN correcto.

if intentos == MAX_INTENTOS and pin_ingresado != PIN_CORRECTO:
    print("🚫 Has agotado los 3 intentos. Tarjeta bloqueada por seguridad.")