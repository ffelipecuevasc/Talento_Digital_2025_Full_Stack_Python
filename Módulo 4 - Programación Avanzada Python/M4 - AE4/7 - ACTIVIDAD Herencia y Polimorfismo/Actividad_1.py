# Definimos el "Contrato"
class MetodoPago:
    def pagar(self, monto):
        pass # Definición vacía, solo para establecer la interfaz

# Implementación 1
class TarjetaCredito(MetodoPago):
    def pagar(self, monto):
        print(f"💳 Procesando pago de ${monto} con Tarjeta. Conectando al banco...")

# Implementación 2
class PayPal(MetodoPago):
    def pagar(self, monto):
        print(f"📧 Procesando pago de ${monto} vía PayPal. Redirigiendo...")

# Sistema de Cobro (No le importa qué método le pases)
def cobrar_cliente(metodo, monto):
    # Polimorfismo puro: confiamos en que 'metodo' sabe 'pagar'
    metodo.pagar(monto)

# Prueba
mi_tarjeta = TarjetaCredito()
cobrar_cliente(mi_tarjeta, 100)
# Salida: 💳 Procesando pago de $100 con Tarjeta...