class Libro:
    """
    Clase que representa un libro en el inventario de una librería.
    Maneja atributos públicos y privados con lógica de validación y ventas.
    """

    def __init__(self, titulo, autor, stock, precio):
        # Atributos Públicos: Accesibles directamente
        self.titulo = titulo
        self.autor = autor
        self.stock = stock

        # Atributo Privado: El precio es sensible, lo ocultamos.
        # Inicializamos en 0 y usamos el setter para validar el valor recibido
        self._precio = 0
        self.set_precio(precio)

        # --- GETTER Y SETTER (Encapsulamiento del Precio) ---

    def get_precio(self):
        """Devuelve el precio actual del libro."""
        return self._precio

    def set_precio(self, nuevo_precio):
        """
        Valida que el precio no sea negativo antes de asignarlo.
        Si es negativo, imprime un error y no modifica el valor.
        """
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print(f"🚫 ERROR: El precio no puede ser negativo (${nuevo_precio}).")

    # --- MÉTODOS DE LÓGICA DE NEGOCIO ---
    def vender(self, unidades):
        """
        Gestiona la venta de libros descontando del stock.
        Valida si hay suficientes unidades antes de vender.
        """
        if unidades <= self.stock:
            self.stock -= unidades
            print(f"✅ Venta exitosa: Se vendieron {unidades} unidades de '{self.titulo}'.")
            print(f"   Stock restante: {self.stock}")
        else:
            print(f"❌ Stock insuficiente: Solo quedan {self.stock} unidades. No se puede vender {unidades}.")

    def mostrar_info(self):
        """Imprime la ficha completa del libro."""
        print(f"--- Ficha del Libro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor:  {self.autor}")
        print(f"Stock:  {self.stock} unidades")
        print(f"Precio: ${self._precio}")
        print("-----------------------")


# --- EJECUCIÓN DEL CÓDIGO (PRUEBAS) ---

# 1. Creamos un libro (Instanciación)
mi_libro = Libro("Python para Todos", "Raúl Gonzales", 20, 15000)

# 2. Mostramos información inicial
mi_libro.mostrar_info()

# 3. Intentamos cambiar el precio a un valor inválido (Prueba de Setter)
print("\n--- Intento de asignar precio negativo ---")
mi_libro.set_precio(-5000)  # Debería fallar
print(f"Precio actual: ${mi_libro.get_precio()}")  # Verifica que no cambió

# 4. Realizamos ventas (Prueba de método vender)
print("\n--- Realizando ventas ---")
mi_libro.vender(5)  # Venta válida
mi_libro.vender(20)  # Venta inválida (excede stock restante de 15)