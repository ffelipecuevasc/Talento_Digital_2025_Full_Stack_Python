class Producto:
    """
    Clase que representa un artículo en una tienda.
    Controla que el precio nunca sea negativo mediante encapsulamiento.
    """

    def __init__(self, nombre, precio):
        # Atributo Público: El nombre no requiere validación especial aquí
        self.nombre = nombre

        # Atributo Privado (_precio):
        # IMPORTANTE: Inicializamos el precio usando el SETTER.
        # Así, si alguien intenta crear un producto con precio negativo,
        # la validación del setter actuará inmediatamente.
        # Definimos un valor por defecto temporal o manejamos la lógica en el setter.
        # Para este ejemplo, intentaremos asignarlo vía setter.
        self._precio = 0  # Valor base seguro
        self.set_precio(precio)

        # --- GETTER ---

    def get_precio(self):
        """Devuelve el precio actual del producto."""
        return self._precio

    # --- SETTER ---
    def set_precio(self, nuevo_precio):
        """
        Modifica el precio solo si el valor es positivo.
        Si es negativo, muestra un error y no guarda el cambio.
        """
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print(f"❌ ERROR: El precio no puede ser negativo (${nuevo_precio}). Se mantiene el anterior.")


# --- EJECUCIÓN DE LA DEMO ---

print("--- 1. Creando un producto válido ---")
laptop = Producto("Notebook Gamer", 1500)
print(f"Producto: {laptop.nombre}, Precio: ${laptop.get_precio()}")

print("\n--- 2. Intentando cambiar a un precio negativo ---")
# Intentamos "romper" el sistema con un precio inválido
laptop.set_precio(-500)

# Verificamos que el precio NO cambió (El setter protegió el dato)
print(f"Precio después del intento fallido: ${laptop.get_precio()}")

print("\n--- 3. Cambiando a un precio válido ---")
laptop.set_precio(1200)  # ¡Oferta!
print(f"Precio actualizado: ${laptop.get_precio()}")