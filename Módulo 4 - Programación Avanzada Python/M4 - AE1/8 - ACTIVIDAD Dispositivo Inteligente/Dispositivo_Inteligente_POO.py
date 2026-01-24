class DispositivoInteligente:
    """
    Clase que modela un dispositivo inteligente (ej. Parlante o Luz).
    Gestiona el estado (ON/OFF) y un nivel ajustable (Volumen/Brillo).
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False  # False = Apagado, True = Encendido
        self.nivel = 0  # Nivel inicial (puede ser volumen o brillo)
        print(f"📦 Nuevo dispositivo instalado: {self.nombre}")

    def encender(self):
        """Cambia el estado a Encendido."""
        if not self.estado:
            self.estado = True
            print(f"🟢 {self.nombre} se ha ENCENDIDO.")
        else:
            print(f"⚠️ {self.nombre} ya estaba encendido.")

    def apagar(self):
        """Cambia el estado a Apagado y resetea el nivel a 0."""
        if self.estado:
            self.estado = False
            self.nivel = 0
            print(f"🔴 {self.nombre} se ha APAGADO.")
        else:
            print(f"⚠️ {self.nombre} ya estaba apagado.")

    def ajustar_nivel(self, nuevo_nivel):
        """
        Ajusta el volumen o brillo.
        VALIDACIÓN: Solo funciona si el dispositivo está encendido.
        """
        if self.estado:
            # Validamos que el nivel sea lógico (ej. entre 0 y 100)
            if 0 <= nuevo_nivel <= 100:
                self.nivel = nuevo_nivel
                print(f"🎚️ Nivel de {self.nombre} ajustado a: {self.nivel}")
            else:
                print("❌ Error: El nivel debe estar entre 0 y 100.")
        else:
            print(f"❌ Error: No puedes ajustar {self.nombre} porque está APAGADO.")


# --- ZONA DE PRUEBAS ---

# 1. Instalamos un Parlante
parlante = DispositivoInteligente("Alexa Cocina")

# 2. Intentamos subir volumen estando apagado (Debe fallar)
parlante.ajustar_nivel(50)

# 3. Encendemos y ajustamos
parlante.encender()
parlante.ajustar_nivel(30)  # Funciona

# 4. Apagamos y verificamos estado
parlante.apagar()