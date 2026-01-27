class ImpresoraInteligente:
    """
    Esta clase simula una impresora que puede imprimir en blanco y negro
    o a color, dependiendo de si le damos el color o no.
    """

    # Definimos el método con un argumento OPCIONAL (color=None)
    # Si el usuario no nos da un color, la variable 'color' valdrá None automáticamente.
    def imprimir(self, texto, color=None):

        # Opción 1: El usuario NO dio color (color es None)
        if color is None:
            print(f"🖨️ Imprimiendo en B/N: {texto}")

        # Opción 2: El usuario SÍ dio un color (color tiene dato)
        else:
            print(f"🌈 Imprimiendo en {color}: {texto}")


# --- ZONA DE PRUEBAS ---

mi_impresora = ImpresoraInteligente()

# CASO 1: Llamada simple (sin color)
# Python usa el valor por defecto: color=None
mi_impresora.imprimir("Hola Mundo")
# Salida: 🖨️ Imprimiendo en B/N: Hola Mundo

# CASO 2: Llamada completa (con color)
# Python reemplaza el None por "Rojo"
mi_impresora.imprimir("Atención", "Rojo")
# Salida: 🌈 Imprimiendo en Rojo: Atención