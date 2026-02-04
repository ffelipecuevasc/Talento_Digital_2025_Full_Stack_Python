# 1. Clase Base (El Contrato)
class Notificador:
    def enviar(self, mensaje):
        print("Enviando notificación genérica...")


# 2. Subclase Email (Canal estándar)
class EmailNotificador(Notificador):
    def __init__(self, direccion):
        self.direccion = direccion

    def enviar(self, mensaje):
        print(f"📧 EMAIL enviado a {self.direccion}: '{mensaje}'")


# 3. Subclase SMS (Canal prioritario/costoso)
class SMSNotificador(Notificador):
    def __init__(self, numero):
        self.numero = numero

    def enviar(self, mensaje):
        print(f"📱 SMS enviado a {self.numero}: '{mensaje}'")


# --- FUNCIÓN GESTORA INTELIGENTE ---
def alertar_usuarios(lista_notificadores, mensaje, es_urgente=False):
    print(f"--- Iniciando Alerta (¿Urgente?: {es_urgente}) ---")

    for notificador in lista_notificadores:
        # VALIDACIÓN DINÁMICA CON ISINSTANCE
        # Regla de negocio: Si es un SMS y NO es urgente, no lo enviamos.
        if isinstance(notificador, SMSNotificador) and not es_urgente:
            print(f"⛔ Omitiendo SMS a {notificador.numero}: El mensaje no es urgente.")
            continue  # Saltamos al siguiente ciclo

        # Si pasa el filtro (o es Email, o es SMS urgente), enviamos.
        # Aquí aplicamos POLIMORFISMO.
        notificador.enviar(mensaje)


# --- ZONA DE PRUEBAS ---

# Creamos nuestra base de datos de contactos
contactos = [
    EmailNotificador("juan@example.com"),
    SMSNotificador("+56912345678"),
    EmailNotificador("maria@example.com"),
    SMSNotificador("+56987654321")
]

# ESCENARIO 1: Notificación Normal (Newsletter)
# Los SMS deberían ser ignorados para no molestar/gastar.
alertar_usuarios(contactos, "¡Hola! Mira nuestro boletín semanal.", es_urgente=False)

print("\n" + "=" * 40 + "\n")

# ESCENARIO 2: Notificación Crítica (Servidor Caído)
# Aquí deben salir TODOS los mensajes, incluidos los SMS.
alertar_usuarios(contactos, "¡ALERTA! Servidor caído. Acción requerida.", es_urgente=True)