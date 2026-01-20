# =============================================================================
# 7.1. El Aspirador de Datos: *args (Tuplas Infinitas)
# =============================================================================

# El asterisco * avisa a Python: "Prepárate para recibir múltiples insumos"
# y guárdalos todos en una tupla llamada 'insumos'.

def entregar_insumos(rut_vecino, *insumos):
    """Genera una entrega para el RUT dado con N materiales."""

    print(f"\nEntregando ayuda a RUT {rut_vecino} que incluye:")

    # Dentro de la función, 'insumos' es una TUPLA (lista inmutable).
    # La recorremos con un bucle for, igual que en el ejemplo de la pizza.
    for material in insumos:
        print(f"- {material}")


# PRUEBA 1: Un vecino con una necesidad puntual
entregar_insumos("12.345.678-9", "Caja de Alimentos")

# PRUEBA 2: Un vecino damnificado (Múltiples necesidades)
# ¡Nota que no cambiamos la función! El * se adaptó a la cantidad de argumentos.
entregar_insumos("9.876.543-K", "Caja de Alimentos", "Carbón", "Frazadas", "Pañales")