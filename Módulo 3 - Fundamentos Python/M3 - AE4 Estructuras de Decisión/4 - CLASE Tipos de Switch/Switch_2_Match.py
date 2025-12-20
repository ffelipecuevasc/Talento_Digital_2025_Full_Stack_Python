# ============================================
# SWITCH 1: Restaurante (menú del día 1–7)
# Usando match/case (switch típico en Python 3.10+)
# ============================================

print("=== RESTAURANTE: MENÚ DEL DÍA ===")
print("1) Lunes")
print("2) Martes")
print("3) Miércoles")
print("4) Jueves")
print("5) Viernes")
print("6) Sábado")
print("7) Domingo")

opcion_texto = input("Elige un número (1 a 7): ")  # Pedimos la opción (llega como texto)
opcion = int(opcion_texto)                          # Convertimos a entero para el switch

match opcion:  # "switch" en Python
    case 1:
        print("🍲 Lunes: Lentejas + ensalada")
    case 2:
        print("🍝 Martes: Tallarines + salsa")
    case 3:
        print("🍗 Miércoles: Pollo al horno + arroz")
    case 4:
        print("🐟 Jueves: Pescado + puré")
    case 5:
        print("🍔 Viernes: Hamburguesa + papas")
    case 6:
        print("🍕 Sábado: Pizza + bebida")
    case 7:
        print("🥗 Domingo: Ensalada completa + jugo")
    case _:
        print("⚠️ Número inválido (elige del 1 al 7)")


# ============================================
# SWITCH 2: Asistente bancario (opciones 1–5)
# Usando match/case (switch típico en Python 3.10+)
# ============================================

print("\n=== ASISTENTE BANCARIO ===")
print("1) Consultar saldo")
print("2) Realizar transferencia")
print("3) Pagar servicios")
print("4) Solicitar préstamo")
print("5) Atención al cliente")

opcion_texto = input("Elige una opción (1 a 5): ")  # Pedimos la opción (texto)
opcion = int(opcion_texto)                          # Convertimos a entero

match opcion:  # "switch" en Python
    case 1:
        print("💰 Tu saldo es: $250.000 (ejemplo)")
    case 2:
        print("🔁 Transferencia: ingresa monto y destinatario (simulación)")
    case 3:
        print("🧾 Pago de servicios: luz, agua, internet (simulación)")
    case 4:
        print("🏦 Préstamos: revisaremos tu solicitud (simulación)")
    case 5:
        print("☎️ Atención al cliente: te conectaremos con un ejecutivo (simulación)")
    case _:
        print("⚠️ Opción inválida (elige del 1 al 5)")