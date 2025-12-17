# “Gimnasio de números”
# Operadores aritméticos + asignación

# 1) Definir precios (3 productos)
precio_libro = 12990
precio_mouse = 9990
precio_teclado = 19990

# 2) Definir cantidades
cantidad_libro = 1
cantidad_mouse = 1
cantidad_teclado = 1

# 3) Definir descuento (%)
descuento_porcentaje = 10  # por ejemplo 10% o 15%

# 4) Calcular total bruto (suma y multiplicación)
total_bruto = (precio_libro * cantidad_libro) + (precio_mouse * cantidad_mouse) + (precio_teclado * cantidad_teclado)

# 5) Calcular descuento en dinero (operadores aritméticos)
descuento_dinero = total_bruto * descuento_porcentaje / 100

# 6) Calcular total final
total_final = total_bruto - descuento_dinero

# 7) Mostrar por pantalla
print("TOTAL BRUTO (sin descuento):", total_bruto)
print("DESCUENTO APLICADO (en dinero):", descuento_dinero)
print("TOTAL FINAL (con descuento):", total_final)

print("\n--- SIMULACIÓN DE CAMBIOS ---")

# 8) Agregar una unidad extra usando operador de asignación compuesto (+=)
cantidad_mouse += 1

# 9) El precio de un producto sube o baja usando += o -=
precio_teclado += 1500  # sube 1500 (puedes cambiarlo por -= si quieres que baje)

# 10) Recalcular reutilizando variables
total_bruto = (precio_libro * cantidad_libro) + (precio_mouse * cantidad_mouse) + (precio_teclado * cantidad_teclado)
descuento_dinero = total_bruto * descuento_porcentaje / 100
total_final = total_bruto - descuento_dinero

# 11) Mostrar el nuevo total final
print("NUEVO TOTAL FINAL (después de cambios):", total_final)