def procesar_pedidos(lista_pedidos):
    """Simula que cocinamos los pedidos uno por uno."""
    print("--- Entrando a la cocina (Función) ---")

    # Mientras queden pedidos en la lista...
    while lista_pedidos:
        # Sacamos el último pedido (pop elimina el dato)
        pedido_actual = lista_pedidos.pop()
        print(f"Cocinando: {pedido_actual}")

    print("--- Fin del turno de cocina ---")


# ÁMBITO GLOBAL (Tu lista original)
mis_antojos = ['Pizza', 'Tacos', 'Sushi']

print(f"Mis antojos ANTES: {mis_antojos}")

# Llamamos a la función y le pasamos la lista
procesar_pedidos(mis_antojos)

# ¡SORPRESA!
print(f"Mis antojos DESPUÉS: {mis_antojos}")
# Salida: Mis antojos DESPUÉS: []
# ¡La lista quedó vacía! La función se "comió" tus datos globales.

# Tenemos la misma lista original
mis_antojos = ['Pizza', 'Tacos', 'Sushi']

print(f"Original antes de enviar: {mis_antojos}")

# TRUCO MAESTRO: Agregamos [:] al llamar a la función
# Esto crea una lista gemela temporal solo para la función.
procesar_pedidos(mis_antojos[:])

print(f"Original después de la función: {mis_antojos}")
# Salida: ['Pizza', 'Tacos', 'Sushi']
# ¡Salvados! La lista original está intacta.