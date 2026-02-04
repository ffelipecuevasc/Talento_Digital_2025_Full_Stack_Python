# Definimos una clase para un Perro
class Perro:
    def hablar(self):
        # El perro tiene su propia forma de hablar
        return "¡Guau! 🐶"

# Definimos una clase para un Gato
class Gato:
    def hablar(self):
        # El gato también sabe hablar, pero a su manera
        return "¡Miau! 🐱"

# Definimos una clase para... ¡Un Pato!
class Pato:
    def hablar(self):
        return "¡Cuack! 🦆"

# --- LA MAGIA DEL POLIMORFISMO ---

# Función genérica que acepta CUALQUIER animal
def hacer_hablar(animal):
    # Aquí ocurre la magia. No preguntamos qué animal es.
    # Solo confiamos en que sabe "hablar".
    print(animal.hablar())

# Creamos nuestros objetos
mi_perro = Perro()
mi_gato = Gato()
mi_pato = Pato()

# Usamos la misma función para tipos totalmente distintos
print("--- Concierto Animal ---")
hacer_hablar(mi_perro) # Salida: ¡Guau! 🐶
hacer_hablar(mi_gato)  # Salida: ¡Miau! 🐱
hacer_hablar(mi_pato)  # Salida: ¡Cuack! 🦆