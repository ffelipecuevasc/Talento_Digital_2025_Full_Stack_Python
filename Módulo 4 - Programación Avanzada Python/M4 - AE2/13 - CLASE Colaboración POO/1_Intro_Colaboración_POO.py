class Cuchillo:
    def cortar(self, ingrediente):
        print(f"🔪 Cortando {ingrediente} en trocitos finos...")

class Chef:
    def __init__(self, nombre):
        self.nombre = nombre

    # AQUÍ OCURRE LA COLABORACIÓN
    # El método recibe un objeto 'herramienta' (que esperamos sea un cuchillo)
    def preparar_ensalada(self, herramienta, ingrediente):
        print(f"👨‍🍳 Chef {self.nombre} va a cocinar.")
        # El Chef DELEGA la acción de cortar al objeto herramienta
        herramienta.cortar(ingrediente)
        print("🥗 ¡Ensalada lista!")

# --- PUESTA EN ESCENA ---

mi_chef = Chef("Gusteau")
mi_cuchillo = Cuchillo()

# El Chef COLABORA con el cuchillo para procesar una zanahoria
mi_chef.preparar_ensalada(mi_cuchillo, "Zanahoria")