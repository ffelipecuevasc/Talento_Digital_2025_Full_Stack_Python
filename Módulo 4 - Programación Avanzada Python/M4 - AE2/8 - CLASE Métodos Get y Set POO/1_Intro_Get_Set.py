class UsuarioGamer:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        # OJO: No asignamos self._edad = edad directamente.
        # Llamamos al SETTER desde el nacimiento del objeto para validar
        # la edad desde el primer segundo. ¡Seguridad ante todo!
        self.set_edad(edad)

    # --- GETTER (Para ver) ---
    def get_edad(self):
        # Simplemente devolvemos el valor protegido
        return self._edad

    # --- SETTER (Para modificar con reglas) ---
    def set_edad(self, nueva_edad):
        # Aquí está la magia: VALIDACIÓN
        if nueva_edad >= 0:
            self._edad = nueva_edad
            print(f"✅ Edad actualizada correctamente a: {self._edad}")
        else:
            print("🚫 ERROR: ¡No puedes tener edad negativa! Viajar en el tiempo no vale.")

# --- PROBANDO EL CÓDIGO ---

player1 = UsuarioGamer("Mario", 25)

# 1. Intentamos hacer trampa (Edad negativa)
print("\n--- Intentando asignar edad -10 ---")
player1.set_edad(-10)
# Resultado: El portero (if) lo detiene. El atributo _edad NO cambia.

# 2. Verificamos que la edad sigue siendo la original
print(f"Edad actual: {player1.get_edad()}") # Sigue siendo 25

# 3. Hacemos un cambio válido
print("\n--- Cumpliendo años ---")
player1.set_edad(26)
# Resultado: El portero deja pasar el dato.