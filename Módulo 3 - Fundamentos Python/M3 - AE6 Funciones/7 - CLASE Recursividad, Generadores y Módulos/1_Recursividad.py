# BASE DE DATOS DE LA UNIVERSIDAD (Diccionario)
# Clave: El ramo que quieres tomar
# Valor: El requisito obligatorio para tomarlo (None significa que no tiene requisito)
malla_ingenieria = {
    "Tesis de Grado": "Proyecto de Software",
    "Proyecto de Software": "Arquitectura de Sistemas",
    "Arquitectura de Sistemas": "Programación Avanzada",
    "Programación Avanzada": "Introducción a la Programación",
    "Introducción a la Programación": None  # <--- ¡Este es el fin del camino!
}


def obtener_ruta_critica(asignatura_objetivo):
    # 1. CASO BASE (El freno de mano)
    # Buscamos el requisito inmediato en el diccionario
    requisito_previo = malla_ingenieria.get(asignatura_objetivo)

    # Si no tiene requisito (es None), ¡Llegamos al inicio de la carrera!
    if requisito_previo is None:
        print(f"🏁 ¡Encontré el origen! Debes partir por: {asignatura_objetivo}")
        return [asignatura_objetivo]  # Retornamos una lista con el primer ramo

    # 2. CASO RECURSIVO (La llamada al pasado)
    else:
        print(f"🔍 Para tomar '{asignatura_objetivo}', necesito aprobar '{requisito_previo}'...")

        # --- AQUÍ OCURRE LA MAGIA ---
        # Nos llamamos a nosotros mismos, pero ahora preguntando por el ramo ANTERIOR
        historial_completo = obtener_ruta_critica(requisito_previo)

        # Cuando la recursión vuelva del pasado, agregamos el ramo actual a la lista
        historial_completo.append(asignatura_objetivo)

        return historial_completo


# --- PROBANDO EL SISTEMA ---
print("🎓 CONSULTA DE MALLA CURRICULAR")
print("Alumno desea inscribir: 'Tesis de Grado'\n")

ruta_final = obtener_ruta_critica("Tesis de Grado")

print("\n✅ TU RUTA DE ESTUDIO COMPLETA ES:")
for paso, ramo in enumerate(ruta_final, 1):
    print(f"   {paso}. {ramo}")