# ----------------------------------------------------
# SISTEMA DE GESTIÓN DE RESERVAS - CINE
# ----------------------------------------------------
# Este programa permite:
# - Mostrar películas y horarios
# - Reservar boletos
# - Validar disponibilidad
# - Mostrar un resumen final de compra
# - Repetir reservas hasta que el usuario decida salir
# ----------------------------------------------------

# 1) Definimos las películas disponibles con horarios y cupos
peliculas = {
    "Avengers": {
        "horario": "18:00",
        "disponibles": 30,
        "precio": 5000
    },
    "Matrix": {
        "horario": "20:00",
        "disponibles": 25,
        "precio": 4500
    },
    "Interestelar": {
        "horario": "22:00",
        "disponibles": 20,
        "precio": 5500
    }
}

# 2) Lista para guardar todas las reservas realizadas
reservas = []

# 3) Variable para controlar el menú principal
continuar = True

# ----------------------------------------------------
# MENÚ PRINCIPAL (se repite mientras el usuario no salga)
# ----------------------------------------------------
while continuar:

    print("\n🎥 PELÍCULAS DISPONIBLES")
    print("-" * 30)

    # 4) Mostramos las películas usando for
    for nombre, datos in peliculas.items():
        print(f"- {nombre} | Horario: {datos['horario']} | Boletos disponibles: {datos['disponibles']}")

    # 5) Solicitamos la película
    pelicula_seleccionada = input("\nEscribe el nombre de la película (o 'salir' para terminar): ")

    # 6) Opción para salir del sistema
    if pelicula_seleccionada.lower() == "salir":
        break

    # 7) Validamos que la película exista
    if pelicula_seleccionada not in peliculas:
        print("❌ Película no válida. Intenta nuevamente.")
        continue

    # 8) Solicitamos cantidad de boletos
    boletos = int(input("¿Cuántos boletos deseas comprar?: "))

    # 9) Verificamos disponibilidad
    disponibles = peliculas[pelicula_seleccionada]["disponibles"]

    if boletos > disponibles:
        print("❌ No hay suficientes boletos disponibles.")
        continue

    # 10) Calculamos el total
    precio_unitario = peliculas[pelicula_seleccionada]["precio"]
    total = boletos * precio_unitario

    # 11) Guardamos la reserva
    reserva = {
        "pelicula": pelicula_seleccionada,
        "horario": peliculas[pelicula_seleccionada]["horario"],
        "boletos": boletos,
        "total": total
    }

    reservas.append(reserva)

    # 12) Actualizamos la disponibilidad
    peliculas[pelicula_seleccionada]["disponibles"] -= boletos

    # 13) Mostramos resumen parcial
    print("\n✅ RESERVA CONFIRMADA")
    print(f"Película: {pelicula_seleccionada}")
    print(f"Horario: {reserva['horario']}")
    print(f"Boletos: {boletos}")
    print(f"Total a pagar: ${total}")

    # 14) Preguntamos si desea seguir reservando
    opcion = input("\n¿Deseas hacer otra reserva? (s/n): ").lower()

    if opcion != "s":
        continuar = False

# ----------------------------------------------------
# RESUMEN FINAL DE COMPRA
# ----------------------------------------------------
print("\n🧾 RESUMEN FINAL DE COMPRA")
print("-" * 35)

costo_total = 0

for r in reservas:
    print(f"- {r['pelicula']} ({r['horario']}) | Boletos: {r['boletos']} | Total: ${r['total']}")
    costo_total += r["total"]

print("-" * 35)
print(f"💰 TOTAL A PAGAR: ${costo_total}")
print("🎉 ¡Gracias por tu compra!")