# ======================================================
# DEMO 1: EL BANCO INTELIGENTE (Validación de Datos)
# ======================================================
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        """Aumenta el saldo."""
        self.saldo += cantidad
        print(f"💰 {self.titular} depositó ${cantidad}. Nuevo saldo: ${self.saldo}")

    def retirar(self, cantidad):
        """
        Disminuye el saldo, PERO con validación.
        ¡El método protege al atributo para que no sea negativo!
        """
        if cantidad > self.saldo:
            print(f"❌ Operación rechazada: Fondos insuficientes. Tienes ${self.saldo}")
        else:
            self.saldo -= cantidad
            print(f"💸 Retiro exitoso de ${cantidad}. Quedan: ${self.saldo}")

# --- Probamos el Banco ---
mi_cuenta = CuentaBancaria("Felipe", 100)
mi_cuenta.retirar(500)  # El método dice ¡NO! (Lógica de protección)
mi_cuenta.retirar(50)   # El método dice SÍ.