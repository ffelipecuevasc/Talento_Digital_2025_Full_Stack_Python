class Empleado:
    """
    Clase que modela a un empleado de una empresa.
    Demuestra el uso de métodos para gestión global (clase) y utilitaria (estática).
    """

    # Atributo de Clase: El aumento es el mismo para todos (política de empresa)
    aumento_general = 1.05  # 5% de aumento por defecto

    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def aplicar_aumento(self):
        """Método de instancia que aplica el aumento actual al salario de ESTE empleado."""
        # Notar que usamos self.aumento_general o Empleado.aumento_general
        self.salario = self.salario * self.aumento_general
        print(f"✅ Aumento aplicado a {self.nombre}. Nuevo salario: ${self.salario:.2f}")

    # --- MÉTODO DE CLASE (@classmethod) ---
    @classmethod
    def cambiar_politica_aumento(cls, nuevo_porcentaje):
        """
        Modifica el porcentaje de aumento para TODA la empresa.
        Recibe 'cls' para alterar el atributo de clase.
        """
        cls.aumento_general = nuevo_porcentaje
        print(f"📢 Política actualizada: Nuevo factor de aumento general es {cls.aumento_general}")

    # --- MÉTODO ESTÁTICO (@staticmethod) ---
    @staticmethod
    def es_salario_valido(salario_a_evaluar):
        """
        Función utilitaria que verifica si un salario cumple con el sueldo mínimo.
        No necesita saber de qué empleado es, solo evalúa el número.
        """
        sueldo_minimo = 1000
        if salario_a_evaluar >= sueldo_minimo:
            return True
        else:
            return False


# --- EJECUCIÓN DE LA DEMO ---

print("--- 1. Validación con Método Estático ---")
# Usamos la herramienta antes de contratar a alguien
salario_propuesto = 800
if Empleado.es_salario_valido(salario_propuesto):
    print("Salario correcto.")
else:
    print(f"⚠️ Error: ${salario_propuesto} está por debajo del mínimo.")

print("\n--- 2. Creación de Empleados y Aumento Normal ---")
emp1 = Empleado("Ana", 2000)
emp2 = Empleado("Juan", 3000)

# Aplicamos el aumento actual (1.05)
emp1.aplicar_aumento()  # 2000 * 1.05 = 2100

print("\n--- 3. Cambio Global con Método de Clase ---")
# ¡Buenas noticias! La empresa decide dar un aumento del 20%
Empleado.cambiar_politica_aumento(1.20)

# Ahora aplicamos aumento a Juan con la nueva política
emp2.aplicar_aumento()  # 3000 * 1.20 = 3600

# Verificamos si Ana (creada antes) también ve la nueva política si se le aplica otra vez
print(f"Factor de aumento actual para Ana: {emp1.aumento_general}")  # Es 1.20