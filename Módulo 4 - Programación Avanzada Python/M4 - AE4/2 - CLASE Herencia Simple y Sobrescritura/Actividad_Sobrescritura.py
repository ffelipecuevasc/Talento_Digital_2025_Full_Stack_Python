# 1. Clase Base (Superclase)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    # Este método existe para ser sobrescrito. Es un "placeholder" o plantilla.
    def emitir_sonido(self):
        print("Sonido genérico (aún no sé qué animal soy) 🔇")


# 2. Subclase Perro
class Perro(Animal):
    # No necesitamos definir __init__ si solo vamos a usar el del padre (nombre)

    # SOBRESCRITURA: Cambiamos el sonido genérico por uno de perro
    def emitir_sonido(self):
        print("¡Guau! ¡Guau! 🐕")


# 3. Subclase Gato
class Gato(Animal):
    # SOBRESCRITURA: Cambiamos el sonido genérico por uno de gato
    def emitir_sonido(self):
        print("¡Miau! 🐈")


# --- EJECUCIÓN DEL DEMO ---

# Creamos una lista de animales (Polimorfismo en acción)
mis_mascotas = [
    Animal("Cosa Rara"),
    Perro("Firulais"),
    Gato("Michi")
]

print("--- Probando Sonidos ---")
# Recorremos la lista y les pedimos a todos lo mismo: emitir_sonido()
for mascota in mis_mascotas:
    # Cada objeto sabe cuál versión del método usar gracias a la sobrescritura
    print(f"{mascota.nombre} dice:")
    mascota.emitir_sonido()
    print("-" * 20)