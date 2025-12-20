# Evaluador de crédito para notebook del bootcamp
# Pide ingreso, deudas y si tiene trabajo estable. Calcula porcentaje de deuda y decide.

ingreso = float(input("Ingreso mensual aproximado: "))
deudas = float(input("Monto total de deudas actuales: "))
respuesta_trabajo = input("¿Tienes trabajo estable? (si/no): ")

trabajo_estable = (respuesta_trabajo == "si" or respuesta_trabajo == "Si" or respuesta_trabajo == "SI")

# Evitar división por cero (por si alguien pone ingreso = 0)
if ingreso == 0:
    print("\nNo se puede calcular porcentaje de deuda si el ingreso es 0.")
else:
    porcentaje_deuda = (deudas / ingreso) * 100

    print("\n--- RESULTADOS ---")
    print("Porcentaje de ingreso comprometido en deudas:", porcentaje_deuda, "%")

    # Reglas (puedes ajustar los números si quieres)
    # - Aprobado sin condiciones: ingreso alto + deuda baja + trabajo estable
    # - Aprobado con aval: ingreso medio + deuda moderada + trabajo estable
    # - Rechazado: ingreso bajo o deuda muy alta o sin trabajo estable
    if (ingreso >= 1000000) and (porcentaje_deuda <= 25) and trabajo_estable:
        print("Crédito aprobado sin condiciones.")
        print("Consejo: ¡Buen manejo financiero! Mantén tus deudas bajo control.")
    elif (ingreso >= 600000) and (porcentaje_deuda <= 45) and trabajo_estable:
        print("Crédito aprobado con aval.")
        print("Consejo: Sería bueno bajar un poco tus deudas para mejorar tu perfil.")
    else:
        print("Crédito rechazado.")
        print("Consejo: Intenta reducir tus deudas o aumentar tu ingreso antes de pedir crédito.")