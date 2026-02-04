import math  # Importamos la librería matemática para usar Pi (π)


# 1. Definimos la Clase Base
class Figura:
    def calcular_area(self):
        # Esta es una clase abstracta conceptualmente.
        # No sabe calcular el área porque no tiene forma definida,
        # pero obliga a sus hijos a tener este método.
        pass

    # 2. Definimos el Círculo (Hija de Figura)


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio  # Guardamos el radio

    # POLIMORFISMO: Implementamos el método a la manera del Círculo
    def calcular_area(self):
        # Fórmula: Pi * radio al cuadrado
        return math.pi * (self.radio ** 2)


# 3. Definimos el Rectángulo (Hija de Figura)
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # POLIMORFISMO: Implementamos el método a la manera del Rectángulo
    def calcular_area(self):
        # Fórmula: base * altura
        return self.base * self.altura


# --- PRUEBA DEL SISTEMA ---

# Creamos una lista mixta (Polimorfismo en acción)
# No importa que sean distintos, ambos son "Figuras"
mis_figuras = [
    Circulo(5),  # Un círculo de radio 5
    Rectangulo(4, 6),  # Un rectángulo de 4x6
    Circulo(10)  # Otro círculo más grande
]

print("--- Calculadora de Áreas Universal ---")

# Recorremos la lista
for figura in mis_figuras:
    # AQUÍ es donde brilla el polimorfismo.
    # Llamamos a .calcular_area() y cada objeto sabe qué fórmula usar.
    # Usamos 'round' para que no salgan tantos decimales.
    area = round(figura.calcular_area(), 2)

    # Imprimimos el resultado.
    # Usamos type(figura).__name__ solo para que veas en pantalla quién es quién.
    print(f"El área del {type(figura).__name__} es: {area}")