class Administracion:
    """
    Clase componente.
    Representa a la oficina de administración del edificio.
    No tiene vida propia fuera del contexto de un Edificio (en este modelo).
    """
    def __init__(self, nombre_administrador, telefono, email):
        self.nombre_administrador = nombre_administrador
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Admin: {self.nombre_administrador} | Contacto: {self.telefono}"