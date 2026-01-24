class Coche:
    """
    Clase que representa un coche.
    Demuestra cómo el cambio de atributos modifica el estado y comportamiento.
    """

    def __init__(self, marca, modelo, combustible_actual):
        # Estado Inicial: Definimos quién es el coche y cuánta gasolina tiene.
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible_actual  # Litros disponibles
        print(f"🚗 Nuevo coche creado: {self.marca} {self.modelo} con {self.combustible}L.")

    def conducir(self, kilometros):
        """Intenta conducir. Requiere combustible."""
        # Calculamos el gasto (Digamos que gasta 1L por cada 10km para simplificar)
        consumo_necesario = kilometros / 10

        print(f"\n--- Intentando conducir {kilometros} km ---")

        # Verificamos el ESTADO antes de actuar
        if self.combustible >= consumo_necesario:
            self.combustible -= consumo_necesario  # Modificamos el estado (Gasta gasolina)
            print(f"✅ ¡Viaje exitoso! Has llegado a tu destino.")
            print(f"⛽ Combustible restante: {self.combustible} Litros.")
        else:
            print(f"❌ Error: No tienes suficiente gasolina. Necesitas {consumo_necesario}L.")
            print(f"Estado actual: Solo tienes {self.combustible}L.")

    def repostar(self, litros):
        """Carga gasolina y actualiza el estado."""
        self.combustible += litros
        print(f"\n⛽ ¡Glug, glug! Has repostado {litros} litros.")
        print(f"Nuevo estado del tanque: {self.combustible} Litros.")


# --- ZONA DE PRUEBAS ---

# 1. Instanciamos el objeto (Estado inicial: 5 Litros)
mi_auto = Coche("Toyota", "Corolla", 5)

# 2. Intentamos un viaje corto (Requiere 2 Litros)
mi_auto.conducir(20)
# El estado cambió: De 5L bajó a 3L.

# 3. Intentamos un viaje largo (Requiere 10 Litros)
mi_auto.conducir(100)
# Falla porque el estado actual (3L) no permite la acción.

# 4. Cambiamos el estado recargando
mi_auto.repostar(20)  # Ahora tiene 23L

# 5. Reintentamos el viaje largo
mi_auto.conducir(100)  # ¡Ahora sí funciona!