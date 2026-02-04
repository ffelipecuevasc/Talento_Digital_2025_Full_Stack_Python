class Departamento:
    """
    Clase que representa una unidad habitacional.
    Aplica ENCAPSULAMIENTO en la deuda y ATRIBUTOS DE CLASE para la UF.
    """

    # ATRIBUTO DE CLASE: Compartido por todas las instancias.
    # Si la UF sube, sube para todos los departamentos.
    valor_uf_actual = 36000

    def __init__(self, numero_unidad, propietario, deuda_inicial=0):
        self.numero_unidad = numero_unidad  # Público: Se puede saber el número
        self.propietario = propietario  # Público: Se puede saber el dueño

        # ATRIBUTO PRIVADO (Encapsulamiento):
        # Usamos guion bajo (_) para indicar que NO se debe modificar directamente.
        # La deuda es sagrada y no se toca arbitrariamente.
        self._saldo_gastos_comunes = deuda_inicial

    # --- MÉTODO DE CLASE (@classmethod) ---
    @classmethod
    def cambiar_valor_uf(cls, nuevo_valor):
        """
        Modifica el valor de la UF para TODOS los departamentos.
        Recibe 'cls' en lugar de 'self'.
        """
        cls.valor_uf_actual = nuevo_valor
        print(f"📈 INFORMACIÓN: El valor de la UF se ha actualizado a ${cls.valor_uf_actual}")

    # --- LÓGICA DE NEGOCIO (Setter Inteligente) ---
    def pagar_gastos(self, monto):
        """
        Permite disminuir la deuda (pagar).
        Valida que el pago sea positivo.
        """
        if monto > 0:
            if monto <= self._saldo_gastos_comunes:
                self._saldo_gastos_comunes -= monto
                print(f"✅ Pago aceptado de ${monto}. Deuda restante: ${self._saldo_gastos_comunes}")
            else:
                # Opcional: Permitir saldo a favor, pero por ahora limitamos al total
                print(f"⚠️ El monto excede la deuda actual (${self._saldo_gastos_comunes}).")
        else:
            print("🚫 Error: El monto del pago debe ser positivo.")

    def agregar_cobro(self, monto):
        """Método auxiliar para simular que llegan nuevos cobros mes a mes"""
        if monto > 0:
            self._saldo_gastos_comunes += monto
            print(f"📥 Nuevo cobro de ${monto} agregado a Depto {self.numero_unidad}")

    # --- REPRESENTACIÓN (__str__) ---
    def __str__(self):
        # Convertimos la deuda a UF referencial para mostrar información completa
        deuda_uf = self._saldo_gastos_comunes / Departamento.valor_uf_actual
        return (f"📍 Depto {self.numero_unidad} | Propietario: {self.propietario} | "
                f"Deuda: ${self._saldo_gastos_comunes} ({deuda_uf:.2f} UF)")