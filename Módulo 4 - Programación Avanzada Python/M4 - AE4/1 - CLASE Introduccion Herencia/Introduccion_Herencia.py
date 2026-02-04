# Definimos la Clase Padre (Superclase)
class Dispositivo:
    def __init__(self, marca):
        # Este atributo lo tendrán TODOS los hijos
        self.marca = marca

    def encender(self):
        # Este comportamiento es común para todos
        print(f"El dispositivo {self.marca} se está encendiendo... 🔌")


# Definimos la Clase Hija (Subclase) que hereda de Dispositivo
# Fíjate en el paréntesis: class Hija(Padre)
class Telefono(Dispositivo):
    def llamar(self, numero):
        # Este método es EXCLUSIVO del Telefono. Un Dispositivo genérico no sabe llamar.
        print(f"Llamando al {numero} desde mi {self.marca} 📱")


# --- ZONA DE PRUEBAS ---

# Creamos un Teléfono (que en el fondo también es un Dispositivo)
mi_celular = Telefono("Samsung")

# Usamos un método HEREDADO (definido en el Padre)
mi_celular.encender()
# Salida: El dispositivo Samsung se está encendiendo... 🔌

# Usamos un método PROPIO (definido en la Hija)
mi_celular.llamar("555-1234")
# Salida: Llamando al 555-1234 desde mi Samsung 📱