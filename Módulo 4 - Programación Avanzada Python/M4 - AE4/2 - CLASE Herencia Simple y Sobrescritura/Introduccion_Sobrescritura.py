# Definimos la clase base (Padre)
class Robot:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        # Saludo estándar y aburrido
        print(f"Hola, soy el robot {self.nombre}. 🤖")

# Definimos la clase hija (Hijo)
class RobotFiesta(Robot):
    # SOBRESCRITURA: Redefinimos el método saludar
    # Usamos el MISMO nombre, pero cambiamos el comportamiento
    def saludar(self):
        print(f"¡Wooo! ¡Soy {self.nombre} y vengo a poner música! 🎵🎉")

# --- ZONA DE PRUEBAS ---

# 1. Creamos un robot normal
robot_serio = Robot("C-3PO")
robot_serio.saludar()
# Salida: Hola, soy el robot C-3PO. 🤖 (Usa el método del padre)

# 2. Creamos un robot fiestero
robot_loco = RobotFiesta("R2-D2")
robot_loco.saludar()
# Salida: ¡Wooo! ¡Soy R2-D2 y vengo a poner música! 🎵🎉 (Usa SU propia versión sobrescrita)