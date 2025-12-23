# --------------------------------------------
# break en while: salir cuando ocurre algo importante
# --------------------------------------------

intentos = 1  # Contador de intentos

while True:  # True significa "esto podría repetirse para siempre"
    print("Intento:", intentos)  # Mostramos el intento

    if intentos == 3:  # Si llegamos al intento 3...
        print("🛑 Llegaste al máximo, salimos del ciclo")
        break  # Cortamos el while inmediatamente

    intentos += 1  # Sumamos 1 intento para avanzar

# --------------------------------------------
# continue en while: saltar una vuelta específica
# --------------------------------------------

numero = 0  # Partimos desde 0

while numero < 5:  # Mientras numero sea menor que 5...
    numero += 1  # Aumentamos primero para avanzar siempre (evita ciclo infinito)

    if numero == 3:  # Si el número es 3...
        print("⏭️ Me salto el 3")
        continue  # Saltamos el resto y volvemos al inicio del while

    print("Número:", numero)  # Esto NO se ejecuta cuando numero == 3