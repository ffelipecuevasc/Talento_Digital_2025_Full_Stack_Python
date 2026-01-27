class Motor:
    """
    Componente vital.
    En este diseño, el motor no tiene sentido sin un auto que lo aloje.
    """

    def __init__(self, cilindrada):
        self.cilindrada = cilindrada
        self.encendido = False

    def iniciar(self):
        if not self.encendido:
            self.encendido = True
            print(f"⚙️ Motor {self.cilindrada}cc: ¡RRRUUUMMM! Arrancando sistemas...")
        else:
            print("⚠️ El motor ya estaba encendido.")

    def detener(self):
        self.encendido = False
        print("🤫 Motor detenido.")


class Automovil:
    """
    Clase Compuesta (El Todo).
    TIENE UN (Has-a) Motor.
    """

    def __init__(self, modelo):
        self.modelo = modelo

        # --- AQUÍ OCURRE LA COMPOSICIÓN ---
        # No recibimos el motor desde fuera. ¡Lo creamos aquí dentro!
        # Si este objeto 'Automovil' se borra de la memoria,
        # este 'self.motor' también se perderá.
        self.motor = Motor(cilindrada=2000)

    def arrancar(self):
        print(f"🚗 Conductor gira la llave del {self.modelo}...")
        # Delegamos la tarea técnica al componente interno
        self.motor.iniciar()
        print("🚗 ¡Listo para viajar!")

    def apagar(self):
        print(f"🚗 Estacionando el {self.modelo}...")
        self.motor.detener()


# --- EJECUCIÓN DE LA DEMO ---

# 1. Creamos el Auto (y el motor nace automáticamente en su interior)
mi_auto = Automovil("Toyota Corolla")

# 2. Usamos el Auto (que internamente usa su motor)
mi_auto.arrancar()
# Salida: Gira llave -> Motor hace ruido -> Listo.

mi_auto.apagar()