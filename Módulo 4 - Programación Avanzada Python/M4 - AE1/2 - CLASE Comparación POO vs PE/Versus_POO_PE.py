# =======================================================
# ENFOQUE 1: PROGRAMACIÓN ESTRUCTURADA (El estilo antiguo) 
# =======================================================
# Aquí los datos son simples diccionarios y las funciones están sueltas.

def crear_cliente_estructurado(nombre, edad):
    # Retornamos un diccionario simple (datos sueltos)
    return {"nombre": nombre, "edad": edad}

def saludar_estructurado(cliente_diccionario):
    # La función tiene que "preguntar" al diccionario por los datos
    print(f"Hola (Estructurado), soy {cliente_diccionario['nombre']}")

# USO:
# Tengo que crear el dato y luego pasárselo manualmente a la función
mi_cliente_dict = crear_cliente_estructurado("Ana", 30)
saludar_estructurado(mi_cliente_dict)


# =======================================================
# ENFOQUE 2: PROGRAMACIÓN ORIENTADA A OBJETOS (El estilo PRO)
# =======================================================
# Aquí definimos una ESTRUCTURA REAL. El cliente no es un diccionario tonto,
# es un Agente Inteligente que sabe su nombre y sabe saludar.

class Cliente:
    # 1. EL CONSTRUCTOR (__init__):
    # Aquí definimos qué DATOS tiene cada cliente al nacer.
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo: El nombre se guarda EN el objeto
        self.edad = edad      # Atributo: La edad se guarda EN el objeto

    # 2. EL COMPORTAMIENTO (Método):
    # El cliente usa SUS propios datos (self.nombre) para saludar.
    def saludar(self):
        print(f"Hola (POO), soy {self.nombre}")

# USO:
# Instanciamos (creamos) el objeto.
mi_cliente_obj = Cliente("Ana", 30)

# ¡Magia! No le paso datos a la función.
# Le digo al objeto: "Oye, tú, ¡saluda!". Él ya sabe cómo hacerlo.
mi_cliente_obj.saludar()