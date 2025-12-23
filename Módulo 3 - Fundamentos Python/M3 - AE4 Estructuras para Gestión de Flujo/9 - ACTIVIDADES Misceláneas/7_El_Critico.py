# 7. El Crítico de Comida
# Enfoque: Saltar iteración con continue.

comidas = ["Pizza", "Brócoli", "Hamburguesa", "Brócoli", "Tacos"]

for comida in comidas:
    if comida == "Brócoli":
        print("¡Guácala! (Saltando...) 🤢")
        continue  # Salta al siguiente ciclo del for, ignorando lo de abajo

    print(f"¡Qué rico es comer {comida}! 😋")