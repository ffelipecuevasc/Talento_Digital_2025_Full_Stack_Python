def formatear_nombre(nombre, apellido, segundo_nombre=None):
    """
    Esta función es flexible.
    'segundo_nombre' tiene un valor por defecto de 'None' (Vacío).
    Si no lo enviamos, no pasa nada malo.
    """

    # Verificamos si el "fantasma" (segundo_nombre) apareció
    if segundo_nombre:
        # Si existe, lo incluimos en el saludo
        nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
    else:
        # Si es None, saludamos solo con nombre y apellido
        nombre_completo = f"{nombre} {apellido}"

    return nombre_completo.title()  # .title() pone Mayúsculas bonitas


# CASO 1: Usuario con dos nombres
musico = formatear_nombre('john', 'hooker', 'lee')
print(musico)  # Salida: John Lee Hooker

# CASO 2: Usuario que solo tiene un nombre (¡La función no explota!)
musico_dos = formatear_nombre('jimi', 'hendrix')
print(musico_dos)  # Salida: Jimi Hendrix