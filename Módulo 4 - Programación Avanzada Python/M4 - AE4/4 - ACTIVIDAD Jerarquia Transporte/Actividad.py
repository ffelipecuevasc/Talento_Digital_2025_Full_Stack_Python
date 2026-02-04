# 1. Definimos la Clase Base (Superclase)
class Vehiculo:
    # Constructor común para todos los vehículos
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método genérico que será compartido (o sobrescrito)
    def moverse(self):
        print(f"El {self.marca} {self.modelo} se está moviendo... 🛤️")


# 2. Subclase Auto (Sobrescritura de comportamiento)
class Auto(Vehiculo):
    # No tocamos el __init__ porque usa los mismos datos que Vehiculo (marca, modelo)

    # SOBRESCRITURA: Cambiamos "moverse"
    def moverse(self):
        print(f"🚗 El auto {self.marca} {self.modelo} está conduciendo por la carretera.")


# 3. Subclase Bicicleta (Sobrescritura de comportamiento)
class Bicicleta(Vehiculo):
    # SOBRESCRITURA: Cambiamos "moverse" por algo específico de bicis
    def moverse(self):
        print(f"🚲 La bicicleta {self.marca} {self.modelo} avanza pedaleando.")


# 4. Subclase Motocicleta (Ampliación de atributos)
class Motocicleta(Vehiculo):
    # Aquí necesitamos un dato extra: cilindrada.
    # Por eso debemos sobrescribir el constructor __init__
    def __init__(self, marca, modelo, cilindrada):
        # Usamos super() para que la clase Vehiculo maneje marca y modelo
        super().__init__(marca, modelo)
        # Nosotros nos encargamos del dato nuevo
        self.cilindrada = cilindrada

    # Nota: No sobrescribimos moverse(), así que usará el método original de Vehiculo.
    # (A menos que queramos cambiarlo también, pero el ejercicio pide enfocarse en el atributo).

    def info_motor(self):
        print(f"🏍️ Motocicleta de {self.cilindrada}cc lista para rodar.")


# --- VALIDACIÓN DEL POLIMORFISMO ---

# Creamos una lista con diferentes tipos de vehículos
# Fíjate que la moto recibe un tercer argumento (cilindrada)
mis_vehiculos = [
    Auto("Toyota", "Corolla"),
    Bicicleta("Trek", "Marlin"),
    Motocicleta("Yamaha", "R3", 320),
    Vehiculo("Vehículo", "Genérico")  # Para comparar con la base
]

print("--- 🚦 Iniciando Prueba de Transporte ---")

# Recorremos la lista. No nos importa qué clase específica es cada objeto,
# solo sabemos que todos son "Vehiculos" y saben "moverse()".
for transporte in mis_vehiculos:
    # POLIMORFISMO EN ACCIÓN:
    # Llamamos al mismo método, pero cada objeto responde a su manera.
    transporte.moverse()

    # Si es una moto, mostramos su dato especial
    # (Esto es un extra para verificar que el atributo se guardó bien)
    if isinstance(transporte, Motocicleta):
        transporte.info_motor()

    print("-" * 30)