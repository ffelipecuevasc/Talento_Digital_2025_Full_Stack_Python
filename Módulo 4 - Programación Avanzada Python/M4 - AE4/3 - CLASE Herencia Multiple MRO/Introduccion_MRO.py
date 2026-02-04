# Definimos la primera clase base
class Dragon:
    def atacar(self):
        print("¡El dragón lanza fuego! 🔥")

    def rugir(self):
        print("ROAAAR (Dragón)")


# Definimos la segunda clase base
class Robot:
    def atacar(self):
        print("¡El robot dispara láser! 🔫")

    def calcular(self):
        print("Procesando datos... 101010")


# Definimos la Clase Hija con Herencia Múltiple
# OJO AL ORDEN: Hereda primero de Dragon, luego de Robot
class MechaDragon(Dragon, Robot):
    pass  # No agregamos nada nuevo, solo heredamos


# --- ZONA DE PRUEBAS ---

monstruo = MechaDragon()

# Probamos un método exclusivo de Robot
monstruo.calcular()
# Salida: Procesando datos... 101010 (Lo encuentra en Robot)

# Probamos el método CONFLICTIVO (atacar)
# Como Dragon está primero en la lista (Dragon, Robot), GANA Dragon.
monstruo.atacar()
# Salida: ¡El dragón lanza fuego! 🔥

print(f"\nOrden de búsqueda (MRO): {MechaDragon.mro()}")
# Nos mostrará: [MechaDragon, Dragon, Robot, object]