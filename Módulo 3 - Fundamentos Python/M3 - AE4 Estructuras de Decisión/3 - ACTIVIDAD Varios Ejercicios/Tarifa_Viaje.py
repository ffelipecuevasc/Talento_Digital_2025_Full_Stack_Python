# Simulador de tarifa de viaje al bootcamp
# Pide distancia, horario y si hace carpool (compartir viaje)
# Calcula tarifa final con recargos/descuentos y un bonus con %.

distancia = int(input("Distancia aproximada (km, número entero): "))
horario = input("Horario (punta/normal): ")
respuesta_carpool = input("¿Harás carpool? (si/no): ")

carpool = (respuesta_carpool == "si" or respuesta_carpool == "Si" or respuesta_carpool == "SI")
hora_punta = (horario == "punta" or horario == "Punta" or horario == "PUNTA")

# Valores base (puedes ajustarlos)
tarifa_base = 500          # costo fijo por subir
costo_por_km = 200         # costo por kilómetro

# Tarifa inicial (suma y multiplicación)
tarifa = tarifa_base + (distancia * costo_por_km)

# Recargo por hora punta (por ejemplo 20%)
if hora_punta:
    tarifa = tarifa + (tarifa * 0.20)

# Descuento por carpool (por ejemplo 15%)
if carpool:
    tarifa = tarifa - (tarifa * 0.15)

# Regla creativa con módulo: si la distancia es múltiplo de 5, bonus descuento (por ejemplo 5%)
if distancia % 5 == 0:
    tarifa = tarifa - (tarifa * 0.05)

print("\n--- RESULTADO ---")
print("Tarifa final:", tarifa)

# Mensaje según tipo de viaje
if tarifa <= 2000:
    print("Tipo de viaje: Viaje económico")
elif tarifa <= 4000:
    print("Tipo de viaje: Viaje normal")
else:
    print("Tipo de viaje: Viaje caro")