# 1. Definimos la Clase Padre
class Persona:
    # El constructor recibe los datos básicos
    def __init__(self, nombre, edad):
        self.nombre = nombre # Guardamos el nombre
        self.edad = edad     # Guardamos la edad

    # Método genérico para presentarse
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# 2. Definimos la Subclase Empleado que HEREDA de Persona
class Empleado(Persona):
    # El constructor del hijo necesita los datos del padre (nombre, edad) MÁS los suyos (cargo)
    def __init__(self, nombre, edad, cargo):
        # ¡TRUCO PRO! Usamos super() para llamar al constructor del Padre.
        # Le decimos: "Papá, encárgate de configurar el nombre y la edad, yo veo lo demás".
        super().__init__(nombre, edad)
        self.cargo = cargo # Configuramos el atributo exclusivo del hijo

    # SOBRESCRITURA (Override): Cambiamos cómo se comporta este método en el hijo
    def presentarse(self):
        # Opcional: Podríamos llamar a super().presentarse() si quisiéramos mantener el mensaje original también
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y trabajo como {self.cargo}.")

    # Método exclusivo del Empleado
    def trabajar(self):
        print(f"{self.nombre} está realizando sus tareas de {self.cargo}. 💼")

# --- EJECUCIÓN DEL DEMO ---

# Creamos una instancia de Empleado
# Le pasamos nombre, edad y cargo
empleado1 = Empleado("Felipe", 30, "Desarrollador Web")

# Probamos el método sobrescrito (versión especializada)
print("--- Método Presentarse (Sobrescrito) ---")
empleado1.presentarse()
# Salida esperada: Hola, soy Felipe, tengo 30 años y trabajo como Desarrollador Web.

# Probamos el método exclusivo
print("\n--- Método Trabajar (Exclusivo) ---")
empleado1.trabajar()
# Salida esperada: Felipe está realizando sus tareas de Desarrollador Web. 💼