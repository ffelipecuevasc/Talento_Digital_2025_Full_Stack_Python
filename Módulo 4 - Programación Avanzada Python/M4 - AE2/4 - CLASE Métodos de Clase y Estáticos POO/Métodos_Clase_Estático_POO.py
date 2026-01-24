class Robot:
    # Atributo de Clase: Todos los robots pertenecen a esta empresa
    marca = "Cyberdyne"

    def __init__(self, nombre):
        # Atributo de Instancia: Cada robot tiene su propio nombre
        self.nombre = nombre

    # 1. MÉTODO DE INSTANCIA (Usa self)
    # Acción personal del robot
    def presentarse(self):
        return f"Hola, soy {self.nombre} y fui fabricado por {self.marca}."

    # 2. MÉTODO DE CLASE (Usa cls)
    # Acción corporativa: Cambia la marca para TODOS (presentes y futuros)
    @classmethod
    def cambiar_marca(cls, nueva_marca):
        cls.marca = nueva_marca
        print(f"📢 ¡ATENCIÓN! La empresa ha sido comprada. Ahora somos {cls.marca}.")

    # 3. MÉTODO ESTÁTICO (Sin self, sin cls)
    # Herramienta utilitaria: Solo suma, no le importa quién pregunta
    @staticmethod
    def calcular_fuerza(voltaje, amperaje):
        return voltaje * amperaje

# --- PRUEBAS ---

r1 = Robot("T-800")
r2 = Robot("Wall-E")

# Probando Instancia
print(r1.presentarse()) # Hola, soy T-800...

# Probando Estático (Se puede llamar desde la clase o el objeto)
potencia = Robot.calcular_fuerza(220, 5)
print(f"Potencia calculada: {potencia} Watts") # 1100 Watts

# Probando Clase (Cambio Global)
Robot.cambiar_marca("Skynet")
# Salida: 📢 ¡ATENCIÓN! La empresa ha sido comprada...

# Verificamos que afectó a los objetos ya creados
print(r1.presentarse()) # Hola, soy T-800 y fui fabricado por Skynet.