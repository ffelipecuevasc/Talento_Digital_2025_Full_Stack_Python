# 1. Definimos las clases base con el mismo método "moverse"
class Volador:
    def moverse(self):
        print("El pato vuela 🦅")

class Nadador:
    def moverse(self):
        print("El pato nada 🦆")

# 2. Definimos la clase Pato (Versión 1: Prioridad Volador)
class Pato(Volador, Nadador):
    pass

# --- PRUEBA 1 ---
mi_pato = Pato()
print("--- Caso 1: class Pato(Volador, Nadador) ---")
mi_pato.moverse()
# Salida esperada: El pato vuela 🦅
# ¿Por qué? Porque Volador está a la IZQUIERDA en la definición.

# Inspeccionamos el MRO
print(f"MRO: {Pato.mro()}")
# Verás: [Pato, Volador, Nadador, object]

print("\n" + "="*30 + "\n")

# 3. Definimos la clase PatoInverso (Versión 2: Prioridad Nadador)
# Invertimos el orden de herencia
class PatoInverso(Nadador, Volador):
    pass

# --- PRUEBA 2 ---
mi_pato_nadador = PatoInverso()
print("--- Caso 2: class PatoInverso(Nadador, Volador) ---")
mi_pato_nadador.moverse()
# Salida esperada: El pato nada 🦆
# ¿Por qué? Ahora Nadador está a la IZQUIERDA.

# Inspeccionamos el MRO
print(f"MRO: {PatoInverso.mro()}")
# Verás: [PatoInverso, Nadador, Volador, object]