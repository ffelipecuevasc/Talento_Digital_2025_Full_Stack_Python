# Control de acceso al laboratorio del bootcamp
# Pide credencial, asistencia, si es monitor y si está en horario permitido. Decide acceso y explica por qué.

respuesta_credencial = input("¿Tienes credencial activa? (si/no): ")
asistencia = float(input("Porcentaje de asistencia al bootcamp: "))
respuesta_monitor = input("¿Eres monitor/ayudante? (si/no): ")
respuesta_horario = input("¿Estás dentro del horario permitido? (si/no): ")

tiene_credencial = (respuesta_credencial == "si" or respuesta_credencial == "Si" or respuesta_credencial == "SI")
es_monitor = (respuesta_monitor == "si" or respuesta_monitor == "Si" or respuesta_monitor == "SI")
dentro_horario = (respuesta_horario == "si" or respuesta_horario == "Si" or respuesta_horario == "SI")

# Regla de asistencia mínima (puedes ajustarla)
asistencia_ok = (asistencia >= 75)

print("\n--- DECISIÓN DE ACCESO ---")

# Si no hay credencial, no entra nunca
if not tiene_credencial:
    print("Acceso denegado: No tienes credencial activa.")
else:
    # Si es monitor y tiene credencial, puede entrar incluso fuera de horario
    if es_monitor and (not dentro_horario):
        print("Acceso permitido: ACCESO COMPLETO (monitor fuera de horario).")
    # Acceso normal: credencial + asistencia OK + dentro del horario
    elif asistencia_ok and dentro_horario:
        print("Acceso permitido: ACCESO NORMAL (dentro de horario).")
    else:
        # Explicamos el motivo principal
        if not asistencia_ok:
            print("Acceso denegado: Tu asistencia es baja (mínimo 75%).")
        elif not dentro_horario:
            print("Acceso denegado: Estás fuera del horario permitido.")
        else:
            print("Acceso denegado: No cumples las condiciones de acceso.")