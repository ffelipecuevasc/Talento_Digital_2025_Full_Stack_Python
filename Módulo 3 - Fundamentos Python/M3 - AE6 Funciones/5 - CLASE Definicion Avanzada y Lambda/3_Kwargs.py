# =============================================================================
# 7.2. El Archivador Inteligente: **kwargs (Diccionarios Infinitos)
# =============================================================================

# El doble asterisco ** le dice a Python: "Recibe cualquier etiqueta extra (clave=valor)
# que me manden y organízala en un diccionario llamado 'condiciones'".

def registrar_ficha(rut, **condiciones):
    """Crea una ficha social flexible con el RUT y N datos extra."""

    # Primero aseguramos el dato obligatorio en el diccionario
    condiciones['rut_vecino'] = rut

    # Devolvemos el diccionario completo (el "expediente")
    return condiciones


# CASO A: Vecino estándar (Sin condiciones especiales)
ficha_1 = registrar_ficha('12.345.678-9')
print(ficha_1)
# Salida: {'rut_vecino': '12.345.678-9'}

# CASO B: Vecino prioritario (Con múltiples variables sociales)
# Usamos argumentos por nombre para detallar su situación específica.
ficha_2 = registrar_ficha('9.876.543-K',
                          registro_social=40,
                          tercera_edad=True,
                          zona='Rural')
print(ficha_2)

# Salida: {'registro_social': 40, 'tercera_edad': True, 'zona': 'Rural',
#          'rut_vecino': '9.876.543-K'}

# ¿La lección?
# Con **kwargs, la Ficha Social se adapta a la realidad de cada familia
# sin tener que modificar el código del sistema.