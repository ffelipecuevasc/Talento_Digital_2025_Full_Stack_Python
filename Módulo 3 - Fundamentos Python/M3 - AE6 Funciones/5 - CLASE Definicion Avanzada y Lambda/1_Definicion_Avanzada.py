# =============================================================================
# PROYECTO S.I.G.E.M. (Sistema de Gestión Municipal)
# Actividad 1: La Ventanilla Única
# =============================================================================

# -----------------------------------------------------------------------------
# 1. DECLARACIÓN Y DEFINICIÓN (El "Protocolo")
# -----------------------------------------------------------------------------

# Aquí definimos cómo funciona la ventanilla.
# 'nombre_vecino' y 'es_urgente' son PARÁMETROS.
# Piénsalos como los espacios en blanco en un formulario impreso.
# No sabemos quién vendrá, solo sabemos que pediremos un nombre y si es urgente.

def registrar_atencion(nombre_vecino, es_urgente):
    print(f"--> Iniciando protocolo de atención...")
    print(f"Validando RUT y datos de: {nombre_vecino}")

    # Usamos el parámetro 'es_urgente' para tomar decisiones
    if es_urgente:
        print("¡ALERTA! Derivando inmediatamente a Asistencia Social (Prioridad Alta).")
        estado = "ATENCIÓN INMEDIATA"
    else:
        print("Derivando a sala de espera general.")
        estado = "TURNO NORMAL"

    # La función devuelve un "Ticket" de confirmación
    mensaje_ticket = f"Ticket generado para {nombre_vecino}: [{estado}]"
    return mensaje_ticket


# -----------------------------------------------------------------------------
# 2. EJECUCIÓN O INVOCACIÓN (La "Vida Real")
# -----------------------------------------------------------------------------

print("--- Vecino 1 (Datos Directos) ---")

# Aquí "Sra. Juanita" y True son los ARGUMENTOS.
# "Sra. Juanita" viaja y llena el espacio (parámetro) 'nombre_vecino'.
# True viaja y llena el espacio (parámetro) 'es_urgente'.

resultado1 = registrar_atencion("Sra. Juanita", True)
print(resultado1)

print("\n--- Vecino 2 (Usando variables externas) ---")

# A menudo los datos vienen de otras partes del sistema (base de datos, input, etc.)
persona_en_fila = "Don Pedro"
situacion_critica = False

# Aquí 'persona_en_fila' es el ARGUMENTO.
# Python toma el VALOR "Don Pedro" y se lo entrega al PARÁMETRO 'nombre_vecino'.
# ¡Nota importante!: No importa que la variable se llame 'persona_en_fila' y el
# parámetro 'nombre_vecino'. Lo que importa es que el DATO se pasa de una mano a otra.

resultado2 = registrar_atencion(persona_en_fila, situacion_critica)
print(resultado2)

# Conclusión: La función 'registrar_atencion' es el molde del trámite,
# y los vecinos son los datos que pasan por ese molde.