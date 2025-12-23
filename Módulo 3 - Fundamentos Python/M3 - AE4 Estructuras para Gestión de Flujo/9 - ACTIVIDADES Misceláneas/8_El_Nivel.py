# 8. El Nivel del Personaje
# Enfoque: Comparación encadenada.

xp = int(input("Ingresa tu XP: "))

if xp < 100:
    print("Nivel 1: Novato")
elif 100 <= xp < 500: # Python permite esta sintaxis matemática natural
    print("Nivel 2: Intermedio")
else:
    print("Nivel 3: Maestro")