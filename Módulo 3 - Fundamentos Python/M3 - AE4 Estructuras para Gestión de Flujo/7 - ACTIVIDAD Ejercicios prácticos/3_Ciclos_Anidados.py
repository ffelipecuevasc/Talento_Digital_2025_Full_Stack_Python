# --------------------------------------------
# Matriz (lista de listas) y recorrido completo con ciclos anidados
# --------------------------------------------

matriz = [
    [10, 20, 30],  # Fila 1
    [40, 50, 60],  # Fila 2
    [70, 80, 90]  # Fila 3
]

for fila in matriz:  # Recorremos cada fila (lista interna)
    print("Fila completa:", fila)  # Mostramos la fila entera

    for valor in fila:  # Recorremos cada valor dentro de esa fila
        print("  Valor:", valor)  # Mostramos cada valor con sangría para claridad