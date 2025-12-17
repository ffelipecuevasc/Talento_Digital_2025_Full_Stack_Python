# 1) Pedimos datos al usuario (input siempre llega como texto)
precio_texto = input("Precio del producto: ")
cantidad_texto = input("Cantidad: ")
es_estudiante_texto = input("¿Eres estudiante? (si/no): ")

# 2) Convertimos a números para poder calcular
precio = float(precio_texto)   # float porque podría ser 199.90
cantidad = int(cantidad_texto) # int porque normalmente compramos unidades enteras

# 3) Calculamos el subtotal con operadores aritméticos
subtotal = precio * cantidad  # multiplicación
print("Subtotal:", subtotal)

# 4) Regla: descuento si compra 3 o más (comparación)
compra_grande = (cantidad >= 3)  # True si cantidad es 3 o más

# 5) Convertimos el "si/no" a booleano real
es_estudiante = (es_estudiante_texto.lower() == "si")  # comparación con texto

# 6) Regla final: hay descuento si (compra grande) OR (es estudiante)
tiene_descuento = compra_grande or es_estudiante  # operador lógico OR

# 7) Aplicamos descuento si corresponde
if tiene_descuento:
    descuento = subtotal * 0.10  # 10% de descuento
else:
    descuento = 0

# 8) Precio final (aritmética)
total = subtotal - descuento

# 9) Mostramos resultados con claridad
print("¿Compra grande?:", compra_grande)
print("¿Es estudiante?:", es_estudiante)
print("¿Tiene descuento?:", tiene_descuento)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total)