class Banco:
    """
    El Banco es el experto en manejar dinero.
    Tiene la responsabilidad de sumar y restar saldo de forma segura.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo = 0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"🏦 Banco {self.nombre}: Se depositaron ${cantidad}. Saldo actual: ${self.saldo}")

    def retirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print(f"🏦 Banco {self.nombre}: Se retiraron ${cantidad}. Saldo actual: ${self.saldo}")
        else:
            print(f"🚫 Banco {self.nombre}: Fondos insuficientes para retirar ${cantidad}.")

class Cliente:
    """
    El Cliente es quien tiene la intención de mover dinero.
    No maneja el saldo directamente, COLABORA con un objeto Banco.
    """
    def __init__(self, nombre, banco_asociado):
        self.nombre = nombre
        # Guardamos una referencia al objeto Banco con el que vamos a colaborar
        self.banco = banco_asociado

    def ahorrar_dinero(self, monto):
        print(f"👤 {self.nombre} quiere ahorrar ${monto}...")
        # Delegamos la acción al banco
        self.banco.depositar(monto)

    def gastar_dinero(self, monto):
        print(f"👤 {self.nombre} necesita ${monto} para compras...")
        # Delegamos la acción al banco
        self.banco.retirar(monto)

# --- EJECUCIÓN DE LA DEMO ---

# 1. Creamos los colaboradores independientes
banco_central = Banco("Central de Python")
felipe = Cliente("Felipe", banco_central)

# 2. Iniciamos la colaboración
felipe.ahorrar_dinero(1000)
# Salida: El cliente pide ahorrar -> El Banco confirma el depósito y saldo.

felipe.gastar_dinero(200)
# Salida: El cliente pide retirar -> El Banco confirma el retiro y nuevo saldo.

felipe.gastar_dinero(5000)
# Salida: El cliente pide retirar -> El Banco rechaza por fondos insuficientes.