# ============================================
# 3) “Centro de becas del Bootcamp”
# Objetivo: diccionario + get() + if/elif/else
# ============================================

# Diccionario de becas (al menos 3)
becas = {
    "JOVEN": {
        "nombre": "Beca Talento Joven",
        "descuento": 40,
        "edad_max": 25,
        "promedio_min": 4.5,
        "asistencia_min": 80,
        "situacion": "estudiante"
    },
    "RECONVERSION": {
        "nombre": "Beca Reconversión Laboral",
        "descuento": 35,
        "edad_min": 18,
        "promedio_min": 4.0,
        "asistencia_min": 75,
        "situacion": "cesante"
    },
    "EXCELENCIA": {
        "nombre": "Beca Excelencia Académica",
        "descuento": 50,
        "promedio_min": 6.0,
        "asistencia_min": 90
        # Esta beca no exige situación laboral específica
    }
}

# Datos del estudiante
edad = int(input("Edad: "))
promedio = float(input("Promedio de notas: "))
asistencia = float(input("Asistencia (%): "))
situacion_laboral = input("Situación laboral (trabajando/cesante/estudiante): ").lower()
codigo_beca = input("Código de beca (JOVEN/RECONVERSION/EXCELENCIA): ").upper()

# Usamos get() como “switch”
beca = becas.get(codigo_beca, None)

if beca is None:
    print("\n❌ Esta beca no existe. Revisa los códigos disponibles: JOVEN, RECONVERSION, EXCELENCIA")
else:
    # Mostramos información base
    print("\n=== CENTRO DE BECAS ===")
    print("Beca seleccionada:", beca["nombre"])
    print("Descuento base:", str(beca["descuento"]) + "%")
    print("Datos estudiante -> Edad:", edad, "| Promedio:", promedio, "| Asistencia:", asistencia, "| Situación:", situacion_laboral)

    # Evaluamos requisitos (sin listas, solo variables)
    cumple_edad = True
    cumple_promedio = True
    cumple_asistencia = True
    cumple_situacion = True

    # Edad mínima y máxima (si existen)
    if "edad_min" in beca:
        if edad < beca["edad_min"]:
            cumple_edad = False
    if "edad_max" in beca:
        if edad > beca["edad_max"]:
            cumple_edad = False

    # Promedio mínimo (si existe)
    if "promedio_min" in beca:
        if promedio < beca["promedio_min"]:
            cumple_promedio = False

    # Asistencia mínima (si existe)
    if "asistencia_min" in beca:
        if asistencia < beca["asistencia_min"]:
            cumple_asistencia = False

    # Situación laboral requerida (si existe)
    if "situacion" in beca:
        if situacion_laboral != beca["situacion"]:
            cumple_situacion = False

    # Contamos cuántos requisitos cumple (usando True/False como 1/0)
    requisitos_cumplidos = 0
    if cumple_edad:
        requisitos_cumplidos += 1
    if cumple_promedio:
        requisitos_cumplidos += 1
    if cumple_asistencia:
        requisitos_cumplidos += 1
    if cumple_situacion:
        requisitos_cumplidos += 1

    # Calculamos cuántos requisitos se evaluaron realmente
    requisitos_totales = 3  # edad, promedio, asistencia
    if "situacion" in beca:
        requisitos_totales = 4

    # Resultado final
    if requisitos_cumplidos == requisitos_totales:
        print("\n✅ Calificas a la beca con", str(beca["descuento"]) + "%", "de descuento.")
    elif requisitos_cumplidos >= requisitos_totales - 1:
        # “Casi calificas”: damos descuento menor (por ejemplo, la mitad)
        descuento_menor = int(beca["descuento"] / 2)
        print("\n🟡 Casi calificas. Puedes optar a un descuento menor de", str(descuento_menor) + "%.")
        print("Te falta cumplir al menos 1 requisito.")
    else:
        print("\n❌ No calificas. Te falta cumplir:")
        # Explicamos qué falta (sin listas)
        if not cumple_edad:
            print("- Requisito de edad")
        if not cumple_promedio:
            print("- Promedio mínimo")
        if not cumple_asistencia:
            print("- Asistencia mínima")
        if not cumple_situacion:
            print("- Situación laboral requerida")