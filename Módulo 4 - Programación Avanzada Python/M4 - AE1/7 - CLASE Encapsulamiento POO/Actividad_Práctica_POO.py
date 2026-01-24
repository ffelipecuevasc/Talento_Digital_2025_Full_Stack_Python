class CuentaSegura:
    """
    Clase que demuestra el encapsulamiento usando atributos privados.
    """
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # ATRIBUTO PRIVADO (__):
        # Al poner doble guion bajo, impedimos el acceso directo fácil.
        self.__saldo = saldo_inicial

    # --- GETTER (El Mesero que te dice cuánto hay) ---
    def ver_saldo(self):
        """Permite VER el saldo, pero no tocarlo."""
        # Aquí adentro SÍ podemos usar self.__saldo porque estamos en la casa.
        return self.__saldo

    # --- SETTER (El Mesero que valida antes de cambiar) ---
    def depositar_seguro(self, monto):
        """Permite MODIFICAR el saldo, pero con reglas."""
        if monto > 0:
            self.__saldo += monto
            print(f"✅ Depósito aceptado. Nuevo saldo de {self.titular}: ${self.__saldo}")
        else:
            print("❌ Error: No puedes depositar dinero negativo o cero.")

# --- ZONA DE PRUEBAS ---

mi_cuenta = CuentaSegura("Ana", 1000)

# INTENTO 1: Robo directo (Fallido)
# Intentamos cambiar el saldo manualmente como si fuera una variable pública.
try:
    mi_cuenta.__saldo = 99999999 # Esto crea una variable nueva tonta, no cambia la real
    print(mi_cuenta.__saldo)     # Imprime la variable tonta
    print(mi_cuenta.ver_saldo()) # ¡El saldo real sigue siendo 1000! ¡Ja!
except:
    pass

# INTENTO 2: Forma Correcta (Usando Métodos)
print(f"\nSaldo inicial: ${mi_cuenta.ver_saldo()}")

mi_cuenta.depositar_seguro(500)  # Funciona y actualiza el privado
mi_cuenta.depositar_seguro(-200) # Falla gracias a la validación del método

# Verificación final
print(f"Saldo final real: ${mi_cuenta.ver_saldo()}")