# 1. Definimos las Clases para el escenario
class Animal:
    def emitir_sonido(self):
        print("Grr... (Sonido genérico)")

class Perro(Animal):
    def emitir_sonido(self):
        print("¡Guau Guau! 🐕")

class Gato(Animal):
    def emitir_sonido(self):
        print("¡Miau! 🐈")

class Coche:
    def tocar_bocina(self):
        print("¡Piip Piip! 🚗")
    # OJO: Coche NO tiene método emitir_sonido()

# 2. Creamos una lista mixta (El caos)
# Tenemos animales y una máquina mezclados
lista_caotica = [
    Perro(),
    Coche(),    # ¡El intruso!
    Gato(),
    Perro()
]

print("--- Procesando la Lista Caótica ---")

# 3. Iteramos y filtramos con seguridad
for objeto in lista_caotica:
    # PREGUNTA DE SEGURIDAD:
    # ¿Es usted, señor objeto, un descendiente de la clase Animal?
    if isinstance(objeto, Animal):
        # Si es True, es seguro llamar al método
        print(f"✅ Animal detectado ({type(objeto).__name__}): ", end="")
        objeto.emitir_sonido()
    else:
        # Si es False, evitamos el error y manejamos el caso
        print(f"⛔ OBJETO DESCONOCIDO ({type(objeto).__name__}): No es un animal. Se salta.")