# Definimos el "Molde" (Clase) de un Auto
class Auto:
    # 1. EL NACIMIENTO DEL AUTO (__init__)
    # Aquí definimos sus características iniciales (Atributos)
    def __init__(self, marca, color):
        self.marca = marca  # Guardo la marca
        self.color = color  # Guardo el color
        self.velocidad = 0  # Todo auto nuevo empieza quieto (0 km/h)
        self.encendido = False  # El motor empieza apagado

    # 2. COMPORTAMIENTOS (Métodos)

    def arrancar(self):
        if not self.encendido:  # Si no está encendido...
            self.encendido = True  # ¡Lo prendemos!
            print(f"🚗 El {self.marca} {self.color} ha arrancado.")
        else:
            print("⚠️ ¡Oye! El auto ya estaba prendido.")

    def acelerar(self):
        if self.encendido:  # Solo acelera si está prendido
            self.velocidad += 10  # Aumentamos la velocidad en 10
            print(f"💨 Vrummm... Velocidad actual: {self.velocidad} km/h")
        else:
            print("❌ No puedes acelerar con el motor apagado.")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad = 0  # Frenazo en seco
            print("🛑 ¡Has frenado! El auto está detenido.")
        else:
            print("El auto ya está quieto.")


# --- ZONA DE PRUEBAS (Instanciando Objetos) ---

# Creemos mi auto soñado: Un Ferrari Rojo
mi_ferrari = Auto("Ferrari", "Rojo")

# Intentemos acelerar sin prenderlo (Lógica de la vida real)
mi_ferrari.acelerar()  # Salida: ❌ No puedes acelerar...

# Hagámoslo bien
mi_ferrari.arrancar()  # Salida: 🚗 El Ferrari Rojo ha arrancado.
mi_ferrari.acelerar()  # Salida: 💨 Vrummm... Velocidad actual: 10 km/h
mi_ferrari.acelerar()  # Salida: 💨 Vrummm... Velocidad actual: 20 km/h