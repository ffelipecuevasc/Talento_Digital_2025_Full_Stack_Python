# 6. Buscando el Tesoro
# Enfoque: Interrupción con break y uso de enumerate.

lugares = ["sala", "cocina", "sótano", "tesoro", "jardín"]

# enumerate nos da el índice (i) y el valor (lugar) al mismo tiempo
for i, lugar in enumerate(lugares):
    if lugar == "tesoro":
        print(f"¡Lo encontré en la posición {i}! 💎")
        break # Dejamos de buscar, el jardín se ignora