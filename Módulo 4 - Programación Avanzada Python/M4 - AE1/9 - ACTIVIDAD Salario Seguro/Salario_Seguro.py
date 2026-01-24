class Empleado:
    """
    Clase que gestiona la información de un empleado.
    Protege el salario usando encapsulamiento (atributo privado).
    """

    def __init__(self, nombre, cargo, salario_inicial):
        self.nombre = nombre
        self.cargo = cargo
        # ATRIBUTO PRIVADO (__):
        # Usamos doble guion bajo para que no sea accesible directamente.
        # Esto evita "empleado.__salario = -5000" desde fuera.
        self.__salario = salario_inicial

        # --- GETTER (Ver) ---

    def ver_salario(self):
        """Permite consultar el salario de forma segura."""
        # Aquí podemos agregar lógica extra, como registrar quién consultó.
        return self.__salario

    # --- SETTER (Modificar) ---
    def modificar_salario(self, nuevo_salario):
        """
        Permite cambiar el salario PERO con validación.
        Impide asignar valores negativos.
        """
        if nuevo_salario >= 0:
            self.__salario = nuevo_salario
            print(f"✅ Salario de {self.nombre} actualizado a: ${self.__salario}")
        else:
            print("❌ Error Crítico: El salario no puede ser negativo.")


# --- ZONA DE PRUEBAS ---

# 1. Contratamos a un empleado
dev = Empleado("Carlos", "Desarrollador Python", 3000)

# 2. Consultamos su salario (Uso correcto del Getter)
print(f"Sueldo actual: ${dev.ver_salario()}")

# 3. Intentamos un error común: Salario negativo (El Setter lo atrapa)
dev.modificar_salario(-100)

# 4. Intentamos un aumento válido
dev.modificar_salario(3500)

# 5. Demostración de privacidad
# Si intentamos acceder directo: print(dev.__salario) -> Daría Error (AttributeError)