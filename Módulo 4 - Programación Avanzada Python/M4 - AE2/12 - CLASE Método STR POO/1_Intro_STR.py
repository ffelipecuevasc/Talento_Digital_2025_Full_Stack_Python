# --- FASE 1: Sin Identidad (El problema) ---
class PersonaAburrida:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p1 = PersonaAburrida("Juan", 25)
print("1. Sin __str__:", p1)
# Salida esperada (algo feo): <__main__.PersonaAburrida object at 0x7f8b...>


# --- FASE 2: Con Personalidad (La solución) ---
class Persona:
    """
    Clase que sabe presentarse cortésmente gracias a __str__.
    """
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método mágico __str__
    # OJO: Debe RETORNAR (return) un string, ¡nunca imprimir (print) dentro!
    def __str__(self):
        return f"Persona: {self.nombre}, Edad: {self.edad}"

    # BONUS: Definimos __repr__ para ver la diferencia (técnico)
    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

# --- PRUEBAS ---
p2 = Persona("Ana", 30)

print("\n2. Con __str__ (Para humanos):")
print(p2)
# Salida: Persona: Ana, Edad: 30

print("\n3. Usando str() explícitamente:")
mensaje = "El ganador es " + str(p2)
print(mensaje)
# Salida: El ganador es Persona: Ana, Edad: 30

print("\n4. Representación Técnica (__repr__):")
# Esto es lo que verías si fueras desarrollador depurando
print(repr(p2))
# Salida: Persona('Ana', 30)