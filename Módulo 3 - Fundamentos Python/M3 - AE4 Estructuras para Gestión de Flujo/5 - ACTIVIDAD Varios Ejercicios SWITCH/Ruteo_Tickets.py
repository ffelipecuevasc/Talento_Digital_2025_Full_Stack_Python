# ============================================
# 4) “Ruteo inteligente de tickets del bootcamp”
# Objetivo: diccionario + get() + if/elif/else
# ============================================

# Diccionario de categorías de tickets
ruteo = {
    "pago": {
        "equipo": "Finanzas",
        "correo": "finanzas@bootcamp.cl",
        "tiempo": "48h",
        "prioridad_base": "MEDIA"
    },
    "plataforma": {
        "equipo": "Soporte Técnico",
        "correo": "soporte@bootcamp.cl",
        "tiempo": "24h",
        "prioridad_base": "MEDIA"
    },
    "contenido": {
        "equipo": "Soporte Académico",
        "correo": "academico@bootcamp.cl",
        "tiempo": "48h",
        "prioridad_base": "BAJA"
    },
    "proyecto": {
        "equipo": "Mentoría de Proyecto",
        "correo": "proyecto@bootcamp.cl",
        "tiempo": "24h",
        "prioridad_base": "ALTA"
    },
    "beca": {
        "equipo": "Admisión y Becas",
        "correo": "becas@bootcamp.cl",
        "tiempo": "72h",
        "prioridad_base": "BAJA"
    }
}

# Datos del ticket
tipo_problema = input("Tipo de problema (pago/plataforma/contenido/proyecto/beca): ").lower()
gravedad = int(input("Gravedad (1 a 5): "))
modulo = int(input("Módulo en el que estás (1, 2, 3...): "))

# get() como “switch”
config = ruteo.get(tipo_problema, None)

if config is None:
    print("\n❌ Categoría no reconocida. Intenta con: pago, plataforma, contenido, proyecto, beca")
else:
    # Info base
    equipo = config["equipo"]
    correo = config["correo"]
    tiempo = config["tiempo"]
    prioridad_base = config["prioridad_base"]

    # Ajuste por “módulo crítico”
    # (Ejemplo simple: si estás en módulo 3 o más, lo tratamos como etapa sensible)
    modulo_critico = False
    if modulo >= 3:
        modulo_critico = True

    # Decidimos prioridad final
    prioridad_final = prioridad_base

    # Reglas simples:
    # - gravedad 5 -> URGENTE
    # - gravedad 4 -> ALTA (y si además es módulo crítico -> URGENTE)
    # - gravedad 3 -> MEDIA
    # - gravedad 1-2 -> BAJA o la base
    if gravedad == 5:
        prioridad_final = "URGENTE"
    elif gravedad == 4 and modulo_critico:
        prioridad_final = "URGENTE"
    elif gravedad == 4:
        prioridad_final = "ALTA"
    elif modulo_critico and prioridad_base == "BAJA":
        prioridad_final = "MEDIA"
    elif gravedad == 3:
        prioridad_final = "MEDIA"
    else:
        # Para 1-2 mantenemos la prioridad base si ya es mayor, o BAJA si es baja
        prioridad_final = prioridad_base

    # Salida esperada
    print("\n=== RUTEO DE TICKET ===")
    print("Categoría:", tipo_problema, "| Equipo:", equipo, "| Tiempo estimado:", tiempo)
    if modulo_critico:
        print("Gravedad declarada:", gravedad, "/ Módulo:", modulo, "(etapa sensible)")
    else:
        print("Gravedad declarada:", gravedad, "/ Módulo:", modulo)
    print("Prioridad final del ticket:", prioridad_final)
    print("Tu ticket será gestionado por:", equipo, "– contacto:", correo)