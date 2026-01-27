class CalculadoraFlexible:
    """
    Clase que demuestra la sobrecarga simulada en Python.
    Permite sumar 2 o 3 números usando un solo método.
    """

    # Definimos 'c=0' como valor por defecto.
    # Si nos pasan 3 números, 'c' toma el valor del tercero.
    # Si nos pasan solo 2, 'c' se queda valiendo 0 (y sumar 0 no afecta el resultado).
    def sumar(self, a, b, c=0):
        resultado = a + b + c
        print(f"Sumando {a} + {b} + {c} = {resultado}")
        return resultado

# --- EJECUCIÓN DE LA DEMO ---

calc = CalculadoraFlexible()

print("--- Prueba 1: Sumando 2 números ---")
# Aquí 'c' usa su valor por defecto (0)
calc.sumar(5, 10)
# Resultado interno: 5 + 10 + 0 = 15

print("\n--- Prueba 2: Sumando 3 números ---")
# Aquí 'c' toma el valor 4
calc.sumar(5, 10, 4)
# Resultado interno: 5 + 10 + 4 = 19