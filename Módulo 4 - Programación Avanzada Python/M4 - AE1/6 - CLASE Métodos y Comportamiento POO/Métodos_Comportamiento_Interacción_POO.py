# ======================================================
# DEMO 2 y 3: LA PERSONA Y SU MASCOTA (Interacción y Estados)
# ======================================================

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tiene_hambre = True  # Estado inicial: Hambriento

    def comer(self):
        """
        Método con lógica interna (Demo 3).
        La mascota decide si come o no basándose en su estado.
        """
        if self.tiene_hambre:
            print(f"🐶 {self.nombre}: ¡Yummy! Gracias por la comida. *come feliz*")
            self.tiene_hambre = False  # CAMBIO DE ESTADO: Ya no tiene hambre
        else:
            print(f"🐶 {self.nombre}: *Gira la cabeza* No quiero, estoy lleno.")

    def jugar(self):
        print(f"🐶 {self.nombre}: ¡A jugar!")
        self.tiene_hambre = True # Jugar le da hambre de nuevo
        print(f"(A {self.nombre} le dio hambre de tanto correr)")

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def alimentar_mascota(self, mascota_obj):
        """
        INTERACCIÓN ENTRE OBJETOS (Demo 2).
        Este método recibe OTRO OBJETO como parámetro.
        """
        print(f"\n👤 {self.nombre} intenta alimentar a {mascota_obj.nombre}...")
        # La persona 'activa' el método comer de la mascota
        mascota_obj.comer()

# --- Probamos la Historia ---
pedro = Persona("Pedro")
firulais = Mascota("Firulais")

# Escena 1: Firulais tiene hambre (Estado inicial)
pedro.alimentar_mascota(firulais)
# Resultado: Firulais come y cambia su estado a "Lleno".

# Escena 2: Pedro intenta darle más comida
pedro.alimentar_mascota(firulais)
# Resultado: Firulais rechaza la comida (Lógica interna funcionando).

# Escena 3: Juegan y le da hambre
firulais.jugar()
pedro.alimentar_mascota(firulais) # Ahora sí vuelve a comer.