class Producto:
    """
    Clase que representa un producto con descuentos globales.
    Demuestra el uso de @classmethod y @staticmethod.
    """

    # Atributo de Clase: Descuento compartido por TODOS los productos.
    # 0.10 significa 10% de descuento.
    descuento = 0.10

    def __init__(self, nombre, precio):
        self.nombre = nombre

        # Validamos el precio usando el Método Estático ANTES de asignar
        if Producto.validar_precio(precio):
            self._precio = precio
        else:
            print(f"⚠️ Precio inválido para '{nombre}'. Se asignará $0 por defecto.")
            self._precio = 0

    # --- MÉTODO ESTÁTICO (@staticmethod) ---
    # Herramienta utilitaria: No usa self ni cls. Solo valida lógica.
    @staticmethod
    def validar_precio(precio):
        """Retorna True si el precio es mayor a 0, False si no."""
        return precio > 0

    # --- MÉTODO DE CLASE (@classmethod) ---
    # Modifica el estado global de la clase (el atributo descuento)
    @classmethod
    def set_descuento(cls, nuevo_descuento):
        """Actualiza el porcentaje de descuento para TODOS los productos."""
        cls.descuento = nuevo_descuento
        print(f"📢 Oferta Actualizada: Ahora el descuento global es del {int(nuevo_descuento * 100)}%")

    # --- MÉTODO DE INSTANCIA ---
    # Usa datos propios (self._precio) y datos de clase (self.descuento)
    def aplicar_descuento(self):
        """Calcula y devuelve el precio final con el descuento actual aplicado."""
        precio_final = self._precio * (1 - self.descuento)
        return precio_final


# --- EJECUCIÓN DEL CÓDIGO (PRUEBAS) ---

print("--- 1. Creación de Productos y Validación ---")
p1 = Producto("Teclado Mecánico", 100)
p2 = Producto("Mouse Gamer", -50)  # Precio inválido, validado por @staticmethod

print(f"\nProducto 1: {p1.nombre} | Precio Base: ${p1._precio}")
# Calculamos precio con descuento inicial (10%)
print(f"Precio con descuento actual ({int(Producto.descuento * 100)}%): ${p1.aplicar_descuento()}")

print("\n--- 2. Actualizando el Descuento Global ---")
# Usamos el método de clase para cambiar la oferta para TODOS
Producto.set_descuento(0.50)  # ¡Super oferta del 50%!

print("\n--- 3. Verificando impacto en productos existentes ---")
# Al calcular de nuevo, p1 debe tener el nuevo descuento automáticamente
print(f"Nuevo precio final de {p1.nombre} (50% OFF): ${p1.aplicar_descuento()}")