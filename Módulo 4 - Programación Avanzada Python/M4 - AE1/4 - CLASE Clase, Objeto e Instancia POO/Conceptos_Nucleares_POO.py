# Definimos dos moldes (Clases) diferentes
class Gato:
    pass  # 'pass' significa "aquí no pasa nada, solo define la clase vacía"

class Perro:
    pass

# Creamos las instancias (Horneamos las galletas)
micifu = Gato()
fido = Perro()

# Usamos isinstance() para preguntar: "¿Eres tú de esta familia?"
# Sintaxis: isinstance(objeto, Clase)

print(f"¿Es Micifu un Gato? {isinstance(micifu, Gato)}")   # True (Verdadero)
print(f"¿Es Fido un Gato? {isinstance(fido, Gato)}")       # False (Falso)

# Esto es súper útil cuando tu programa recibe un objeto misterioso
# y necesita asegurarse de que sea del tipo correcto antes de usarlo.