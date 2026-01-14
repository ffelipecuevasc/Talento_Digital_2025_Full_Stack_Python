# --- ESCENARIO 1: El error del 'print' (Solo muestra, no entrega) ---
def calcular_iva_malo(precio):
    impuesto = precio * 0.19
    total = precio + impuesto
    print(f"El precio con IVA es: {total}")
    # Muestra el texto en pantalla, pero devuelve 'None' (Nada)

# Intentamos usarlo:
precio_final = calcular_iva_malo(100) # En pantalla sale: "El precio con IVA es: 119.0"

# ¡PROBLEMA! Queremos sumar el envío (5 dólares)
# Python intentará sumar: None + 5
# print(precio_final + 5)
# ESTO DARÍA ERROR: TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'


# --- ESCENARIO 2: La forma correcta con 'return' (Entrega el dato) ---
def calcular_iva_bueno(precio):
    impuesto = precio * 0.19
    total = precio + impuesto
    return total # <--- ¡Aquí está la magia! Entrega el número 119.0 al programa

# Usamos la función:
costo_producto = calcular_iva_bueno(100) # La función me da 119.0 y lo guardo en la variable.

# Ahora sí puedo seguir operando con ese dato:
costo_total_con_envio = costo_producto + 5

print(f"El total a pagar (producto + envío) es: {costo_total_con_envio}")
# Resultado: 124.0. ¡Éxito total! 🎉