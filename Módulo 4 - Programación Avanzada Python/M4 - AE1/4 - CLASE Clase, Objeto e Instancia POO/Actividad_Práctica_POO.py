# ==============================================================================
# DEMO CLASE PERSONA
# Objetivo: Crear una clase, instanciar objetos y ver que son independientes.
# ==============================================================================

# 1. DEFINICIÓN DE LA CLASE (El Molde)
class Persona:
    """Clase que representa a una persona con nombre y edad."""

    # El método especial __init__ (El Inicializador)
    # Se ejecuta automáticamente cada vez que creamos una nueva Persona.
    # self: Se refiere al objeto que se está creando AHORA MISMO.
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Asignamos el nombre al atributo del objeto
        self.edad = edad  # Asignamos la edad al atributo del objeto
        print(f"✨ Ha nacido una nueva persona: {self.nombre}")

    # Método para presentarse (Acción)
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    # Bonus (Pág 15): Método para cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumple {self.nombre}! Ahora tienes {self.edad} años. 🎂")


# 2. INSTANCIACIÓN (Crear Objetos / Hornear Galletas)
# Creamos dos objetos totalmente diferentes usando el mismo molde.
persona1 = Persona("Ana", 30)
persona2 = Persona("Luis", 25)

print("\n--- Probando Comportamientos ---")
# 3. EJECUTAR MÉTODOS
persona1.presentarse()  # Ana usa SUS datos
persona2.presentarse()  # Luis usa SUS datos

print("\n--- Demostrando Independencia de Estado ---")
# 4. MODIFICAR UN OBJETO NO AFECTA AL OTRO
# Vamos a hacer que Luis cumpla años.
persona2.cumplir_anios()

# Verificamos:
print(f"Edad de Luis (persona2): {persona2.edad}")  # Luis cambió a 26
print(f"Edad de Ana (persona1): {persona1.edad}")  # Ana SIGUE teniendo 30

# Conclusión: Aunque salieron del mismo molde, sus vidas son separadas.

print("\n--- Dinamismo de Python (Pág 17) ---")
# 5. AGREGAR ATRIBUTOS "AL VUELO"
# Python permite agregar cosas extra a un solo objeto sin cambiar la clase.
persona1.profesion = "Ingeniera"

print(f"{persona1.nombre} es {persona1.profesion}.")

# Si intento preguntar la profesión de Luis, dará error porque él no la tiene.
try:
    print(persona2.profesion)
except AttributeError:
    print(f"¡Error! {persona2.nombre} no tiene el atributo 'profesion'.")