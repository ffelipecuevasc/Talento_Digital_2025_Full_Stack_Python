# --------------------------------------------
# Forma menos clara: range(len(lista))
# --------------------------------------------

frutas = ["Manzana", "Uva", "Plátano"]  # Lista de frutas

for i in range(len(frutas)):  # i es el índice (0, 1, 2...)
    print("Fruta:", frutas[i])  # Accedemos usando el índice


# --------------------------------------------
# Forma recomendada: enumerate()
# --------------------------------------------

for i, fruta in enumerate(frutas, start=1):  # i es posición desde 1, fruta es el valor
    print(f"Fruta {i}: {fruta}")  # Más legible: te da posición y valor directo