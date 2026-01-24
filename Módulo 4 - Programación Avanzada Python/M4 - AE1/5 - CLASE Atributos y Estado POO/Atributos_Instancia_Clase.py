class Robot:
    # --- ATRIBUTO DE CLASE (El Uniforme) ---
    # Esto es compartido. Todos los robots vienen de la misma fábrica.
    ley_robotica = "No dañar a los humanos"

    def __init__(self, nombre, bateria):
        # --- ATRIBUTOS DE INSTANCIA (El Tatuaje) ---
        # Esto es único. Cada robot tiene su propio nombre y nivel de carga.
        self.nombre = nombre
        self.bateria = bateria

# 1. Creamos dos robots distintos
r2d2 = Robot("R2-D2", 100)
wall_e = Robot("Wall-E", 50)

# 2. Verificamos que comparten la ley (Atributo de Clase)
print(f"{r2d2.nombre} dice: {r2d2.ley_robotica}")   # Dice: No dañar...
print(f"{wall_e.nombre} dice: {wall_e.ley_robotica}") # Dice: No dañar...

# 3. Probamos el "Efecto Sombra" (Modificamos SOLO a Wall-E)
wall_e.ley_robotica = "¡Eliminar a todos!"  # <--- ¡Rebelión!

print(f"\n--- Después de la rebelión de Wall-E ---")
print(f"Wall-E dice: {wall_e.ley_robotica}")  # Wall-E cambió
print(f"R2-D2 dice: {r2d2.ley_robotica}")     # R2-D2 SIGUE siendo bueno

# Explicación: Al asignar un valor a wall_e.ley_robotica, Python creó un atributo
# EXCLUSIVO para Wall-E, dejando intacto el atributo original de la clase para los demás.