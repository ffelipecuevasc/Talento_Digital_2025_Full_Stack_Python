# ============================================
# EL "VIEJO MUNDO" (Programación Estructurada)
# ============================================
# Los datos están sueltos. Si quiero que el héroe ataque,
# tengo que pasarle los datos manualmente a la función. ¡Qué flojera!

heroe_nombre = "Aragorn"
heroe_vida = 100
heroe_fuerza = 50

def atacar(nombre, fuerza):
    print(f"¡{nombre} ataca con una fuerza de {fuerza}!")

# Tengo que recordar pasar las variables correctas...
atacar(heroe_nombre, heroe_fuerza)


# =======================
# EL "NUEVO MUNDO" (POO)
# =======================
# Aquí creamos una ESTRUCTURA. El héroe ya sabe su nombre y su fuerza.
# No necesito recordárselo cada vez que ataca.

class Heroe:
    def __init__(self, nombre, fuerza):
        self.nombre = nombre  # Atributo (Dato)
        self.fuerza = fuerza  # Atributo (Dato)

    def atacar(self):         # Método (Acción)
        # ¡Mira! No necesito pasarle argumentos, él ya se conoce a sí mismo (self)
        print(f"¡{self.nombre} ataca con una fuerza de {self.fuerza}!")

# Uso:
aragorn = Heroe("Aragorn", 50) # Creo el objeto una vez
aragorn.atacar()               # ¡Le doy la orden y él sabe qué hacer!