# Definimos el Molde (Clase)
class Mascota:
    # --- Atributo de Clase ---
    # Esto es compartido: Todas las mascotas de este molde son perros.
    especie = "Perro"

    # --- El Constructor (__init__) ---
    # Se ejecuta automáticamente al nacer la mascota.
    def __init__(self, nombre, edad):
        # --- Atributos de Instancia ---
        # Estos son únicos: Cada perro tiene SU propio nombre y edad.
        # Usamos 'self' para decir "MI nombre" y "MI edad".
        self.nombre = nombre
        self.edad = edad

    # --- Un Método (Acción) ---
    def ladrar(self):
        # Usamos self.nombre para que cada perro diga SU propio nombre al ladrar
        print(f"¡Guau! Soy {self.nombre} y tengo {self.edad} años.")


# --- ZONA DE PRUEBAS (Creando Objetos/Galletas) ---

# Instanciamos (Creamos) dos objetos diferentes usando el mismo molde
perro1 = Mascota("Firulais", 5)
perro2 = Mascota("Rex", 2)

# Probamos que son independientes (Atributos de Instancia)
perro1.ladrar()  # Salida: ¡Guau! Soy Firulais y tengo 5 años.
perro2.ladrar()  # Salida: ¡Guau! Soy Rex y tengo 2 años.

# Probamos lo que comparten (Atributo de Clase)
print(f"{perro1.nombre} es un {perro1.especie}")  # Salida: Firulais es un Perro
print(f"{perro2.nombre} es un {perro2.especie}")  # Salida: Rex es un Perro