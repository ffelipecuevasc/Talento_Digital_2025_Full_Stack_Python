class CuentaCorreo:
    """
    Clase que simula una cuenta de email demostrando los
    tres niveles de visibilidad de atributos en Python.
    """

    def __init__(self, usuario, email, password):
        # PÚBLICO: El nombre de usuario es visible para todos en la red
        self.usuario = usuario

        # PROTEGIDO: El email completo.
        # Se usa internamente para enviar correos, no se debería cambiar a mano desde fuera.
        self._email = email

        # PRIVADO: La contraseña.
        # Es el dato más sensible. Debe estar oculto para evitar robos de identidad.
        self.__password = password

    def mostrar_datos_seguros(self):
        """Método público para ver info sin revelar el password"""
        print(f"Usuario: {self.usuario} | Email: {self._email}")


# --- Ejecución de la Demo ---

# 1. Creamos la instancia (El objeto correo)
mi_correo = CuentaCorreo("dev_master", "dev@alkemy.org", "superSecreto2026")

print("--- Accediendo a atributos ---")

# 2. Acceso permitido
print(f"1. Usuario (Público): {mi_correo.usuario}")

# 3. Acceso 'No recomendado' (Protegido)
# En un sistema real, modificar esto directamente podría romper el envío de emails.
print(f"2. Email (Protegido - Cuidado): {mi_correo._email}")

# 4. Acceso Denegado (Privado)
try:
    print(f"3. Password: {mi_correo.__password}")
except AttributeError:
    print("3. Password (Privado): ¡Acceso denegado! Python protegió el dato.")

# REFLEXIÓN DEL MANUAL:
# Si esta clase fuera parte de un sistema real y 'password' fuera público (self.password),
# cualquier parte del código (o un programador descuidado) podría imprimirla en los logs
# o cambiarla sin validación, comprometiendo la seguridad de todo el sistema.