class CuentaBancaria:
    def __init__(self, titular, saldo, clave_secreta):
        # 1. PÚBLICO: Cualquiera puede saber quién es el dueño
        self.titular = titular

        # 2. PROTEGIDO: Sugerimos no tocar el saldo directamente (mejor usar métodos)
        self._saldo = saldo

        # 3. PRIVADO: ¡Nadie debería ver la clave!
        self.__clave = clave_secreta

    # --- PRUEBA DE FUEGO ---


mi_cuenta = CuentaBancaria("Felipe", 1000, "1234")

# A) Acceso Público: ¡Sin problemas!
print(f"Dueño: {mi_cuenta.titular}")  # Funciona perfecto

# B) Acceso Protegido: Python te deja, pero te mira feo 🤨
print(f"Saldo: {mi_cuenta._saldo}")  # Funciona, pero rompe la convención

# C) Acceso Privado: ¡ERROR! 🚨
try:
    print(mi_cuenta.__clave)
except AttributeError as e:
    print("\n¡ALERTA! 🚫")
    print(f"Error detectado: {e}")
    print("Python dice: 'No sé de qué clave me hablas'. ¡La ha escondido!")

# EXPLICACIÓN TÉCNICA:
# Al intentar acceder a .__clave, Python lanza un 'AttributeError'
# porque gracias al Name Mangling, ese nombre ya no existe en el ámbito público.