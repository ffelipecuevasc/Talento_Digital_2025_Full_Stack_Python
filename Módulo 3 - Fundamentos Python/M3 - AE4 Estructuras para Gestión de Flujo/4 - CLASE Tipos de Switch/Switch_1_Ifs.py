# ============================================
# SWITCH 1: Restaurante (menú del día 1–7)
# Usando varios If - Elif - Else
# ============================================

# Mostramos las opciones al usuario (1 a 7).
print("=== RESTAURANTE: MENÚ DEL DÍA ===")  # Título del menú.
print("1) Lunes")   # Opción 1.
print("2) Martes")  # Opción 2.
print("3) Miércoles")  # Opción 3.
print("4) Jueves")  # Opción 4.
print("5) Viernes")  # Opción 5.
print("6) Sábado")  # Opción 6.
print("7) Domingo")  # Opción 7.

# Pedimos la opción (llega como texto).
opcion_texto = input("Elige un número (1 a 7): ")  # Capturamos lo que escribe el usuario.

# Convertimos a número entero para comparar.
opcion = int(opcion_texto)  # Convertimos "3" a 3, por ejemplo.

# Creamos una variable para guardar el menú elegido.
menu_del_dia = ""  # Aquí guardaremos el resultado.

# Seleccionamos el menú según el número (estilo switch con if/elif).
if opcion == 1:  # Caso 1.
    menu_del_dia = "🍲 Lunes: Lentejas + ensalada"  # Resultado para lunes.
elif opcion == 2:  # Caso 2.
    menu_del_dia = "🍝 Martes: Tallarines + salsa"  # Resultado para martes.
elif opcion == 3:  # Caso 3.
    menu_del_dia = "🍗 Miércoles: Pollo al horno + arroz"  # Resultado para miércoles.
elif opcion == 4:  # Caso 4.
    menu_del_dia = "🐟 Jueves: Pescado + puré"  # Resultado para jueves.
elif opcion == 5:  # Caso 5.
    menu_del_dia = "🍔 Viernes: Hamburguesa + papas"  # Resultado para viernes.
elif opcion == 6:  # Caso 6.
    menu_del_dia = "🍕 Sábado: Pizza + bebida"  # Resultado para sábado.
elif opcion == 7:  # Caso 7.
    menu_del_dia = "🥗 Domingo: Ensalada completa + jugo"  # Resultado para domingo.
else:  # Si no es 1 a 7.
    menu_del_dia = "⚠️ Opción inválida: elige un número del 1 al 7"  # Mensaje por defecto.

# Mostramos el resultado final.
print(menu_del_dia)  # Imprime el menú o la advertencia.

# ============================================
# SWITCH 2: Asistente bancario (opciones 1–5)
# Usando varios If - Elif - Else
# ============================================

# Mostramos las opciones del asistente bancario.
print("=== ASISTENTE BANCARIO ===")  # Título del sistema.
print("1) Consultar saldo")  # Opción 1.
print("2) Realizar transferencia")  # Opción 2.
print("3) Pagar servicios")  # Opción 3.
print("4) Solicitar préstamo")  # Opción 4.
print("5) Atención al cliente")  # Opción 5.

# Pedimos la opción al usuario.
opcion_texto = input("Elige una opción (1 a 5): ")  # Capturamos texto.

# Convertimos a entero para comparar.
opcion = int(opcion_texto)  # Convertimos a número.

# Variable donde guardamos la respuesta.
respuesta = ""  # Aquí quedará lo que el asistente dirá.

# Elegimos la acción según la opción (estilo switch).
if opcion == 1:  # Caso 1.
    respuesta = "💰 Tu saldo es: $250.000 (ejemplo)"  # Respuesta simulada.
elif opcion == 2:  # Caso 2.
    respuesta = "🔁 Transferencia: ingresa monto y destinatario (simulación)"  # Mensaje guía.
elif opcion == 3:  # Caso 3.
    respuesta = "🧾 Pago de servicios: luz, agua, internet (simulación)"  # Mensaje guía.
elif opcion == 4:  # Caso 4.
    respuesta = "🏦 Préstamos: revisaremos tu solicitud (simulación)"  # Mensaje guía.
elif opcion == 5:  # Caso 5.
    respuesta = "☎️ Atención al cliente: te conectaremos con un ejecutivo (simulación)"  # Mensaje guía.
else:  # Opción fuera de rango.
    respuesta = "⚠️ Opción inválida: elige un número del 1 al 5"  # Valor por defecto.

# Mostramos la respuesta final.
print(respuesta)  # Imprime la acción o la advertencia.