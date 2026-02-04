# 1. Definimos la Clase Base (Superclase)
class Empleado:
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario_base = salario_base

    def calcular_bono(self):
        # Por defecto, el bono es 0 si no se especifica un rol especial
        return 0

    def mostrar_info(self):
        # Un método auxiliar para ver los datos limpio
        return f"ID: {self.id_empleado} | {self.nombre}"


# 2. Definimos la Subclase Gerente
class Gerente(Empleado):
    def calcular_bono(self):
        # Sobrescritura: El Gerente recibe el 20% de su salario como bono
        return self.salario_base * 0.20

    def autorizar_vacaciones(self):
        # Método exclusivo de Gerente
        print(f"✅ El Gerente {self.nombre} ha firmado la autorización de vacaciones.")


# 3. Definimos la Subclase Desarrollador
class Desarrollador(Empleado):
    def calcular_bono(self):
        # Sobrescritura: El Desarrollador recibe el 10% de su salario como bono
        return self.salario_base * 0.10


# --- ZONA DE VALIDACIÓN Y POLIMORFISMO ---

# Creamos la planilla de empleados (Lista mixta)
planilla = [
    Gerente("Laura Jefa", "G-001", 5000),  # Salario alto
    Desarrollador("Pedro Python", "D-101", 3000),  # Salario medio
    Desarrollador("Ana Java", "D-102", 3200),
    Empleado("Pepe Pasante", "E-999", 1000)  # Empleado genérico
]

print("--- 💰 Calculando Bonos de Fin de Año ---")

# Iteramos la lista (Polimorfismo en acción)
for personal in planilla:
    # 1. Ejecutamos el comportamiento polimórfico (calcular_bono)
    # No nos importa qué clase sea, todos saben calcular su bono.
    bono = personal.calcular_bono()

    print(f"{personal.mostrar_info()} -> Bono a pagar: ${bono:.2f}")

    # 2. Validación específica con isinstance()
    # Si detectamos un Gerente, le recordamos su tarea especial.
    if isinstance(personal, Gerente):
        print(f"   ⚠️ ALERTA: {personal.nombre}, recuerde autorizar vacaciones pendientes.")
        # Opcional: Podríamos llamar a personal.autorizar_vacaciones() aquí

    print("-" * 40)