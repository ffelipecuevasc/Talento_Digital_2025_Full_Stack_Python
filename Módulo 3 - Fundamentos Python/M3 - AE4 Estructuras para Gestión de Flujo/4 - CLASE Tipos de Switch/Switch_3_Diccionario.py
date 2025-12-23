# ============================================
# SWITCH 1: Restaurante (menú del día 1–7)
# Usando diccionario + get(clave, default)
# ============================================

print("=== RESTAURANTE: MENÚ DEL DÍA ===")
print("1) Lunes")
print("2) Martes")
print("3) Miércoles")
print("4) Jueves")
print("5) Viernes")
print("6) Sábado")
print("7) Domingo")

opcion_texto = input("Elige un número (1 a 7): ")      # 1) Pedimos la opción (llega como texto)
opcion = int(opcion_texto)                              # 2) Convertimos a entero para comparar/buscar

menu_opciones = {                                       # 3) Diccionario: "opción" -> "resultado"
    1: "🍲 Lunes: Lentejas + ensalada",
    2: "🍝 Martes: Tallarines + salsa",
    3: "🍗 Miércoles: Pollo al horno + arroz",
    4: "🐟 Jueves: Pescado + puré",
    5: "🍔 Viernes: Hamburguesa + papas",
    6: "🍕 Sábado: Pizza + bebida",
    7: "🥗 Domingo: Ensalada completa + jugo"
}

resultado = menu_opciones.get(opcion, "⚠️ Número inválido (elige del 1 al 7)")  # 4) Valor por defecto si no existe
print(resultado)                                                               # 5) Mostramos el resultado


# ============================================
# SWITCH 2: Asistente bancario (opciones 1–5)
# Usando diccionario + get(clave, default)
# ============================================

print("\n=== ASISTENTE BANCARIO ===")
print("1) Consultar saldo")
print("2) Realizar transferencia")
print("3) Pagar servicios")
print("4) Solicitar préstamo")
print("5) Atención al cliente")

opcion_texto = input("Elige una opción (1 a 5): ")      # 1) Pedimos la opción
opcion = int(opcion_texto)                              # 2) Convertimos a entero

acciones = {                                            # 3) Diccionario: "opción" -> "acción"
    1: "💰 Tu saldo es: $250.000 (ejemplo)",
    2: "🔁 Transferencia: ingresa monto y destinatario (simulación)",
    3: "🧾 Pago de servicios: luz, agua, internet (simulación)",
    4: "🏦 Préstamos: revisaremos tu solicitud (simulación)",
    5: "☎️ Atención al cliente: te conectaremos con un ejecutivo (simulación)"
}

respuesta = acciones.get(opcion, "⚠️ Opción inválida (elige del 1 al 5)")       # 4) Default si la clave no existe
print(respuesta)                                                                # 5) Mostramos la respuesta