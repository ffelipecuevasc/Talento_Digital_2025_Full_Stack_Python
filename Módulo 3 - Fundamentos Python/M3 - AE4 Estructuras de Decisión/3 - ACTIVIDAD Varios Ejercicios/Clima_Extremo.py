# Clima extremo: ¿salgo o no salgo?
# Pide temperatura, humedad y si llueve. Calcula un "nivel de incomodidad" y decide qué hacer.

temperatura = float(input("Temperatura actual (°C): "))
humedad = float(input("Humedad (%): "))
respuesta_lluvia = input("¿Está lloviendo? (si/no): ")

# Convertimos "si/no" a una variable booleana (True/False) usando comparaciones simples
llueve = (respuesta_lluvia == "si" or respuesta_lluvia == "Si" or respuesta_lluvia == "SI")

# Nivel de incomodidad (fórmula simple elegida)
# Idea: la humedad aporta "peso" al calor. Puedes ajustar el 0.1 si quieres.
incomodidad = temperatura + (humedad * 0.1)

# Clasificación por rangos (bajo/medio/alto)
if incomodidad < 25:
    nivel = "BAJO (cómodo)"
elif incomodidad < 35:
    nivel = "MEDIO (aceptable, pero incómodo)"
else:
    nivel = "ALTO (muy pesado)"

print("\n--- RESUMEN ---")
print("Incomodidad calculada:", incomodidad)
print("Nivel:", nivel)

# Condiciones combinadas (lógicos)
mucho_calor_y_humedad = (temperatura >= 30) and (humedad >= 70)
frio = (temperatura <= 10)
lluvia_y_mucha_humedad = llueve and (humedad >= 80)

# Decisión final (if / elif / else)
if mucho_calor_y_humedad or (temperatura <= 0) or lluvia_y_mucha_humedad:
    print("Mejor quédate en casa, el clima está extremo.")
elif frio or llueve:
    print("Puedes salir, pero lleva paraguas / abrigo.")
else:
    print("Día ideal para salir a caminar.")