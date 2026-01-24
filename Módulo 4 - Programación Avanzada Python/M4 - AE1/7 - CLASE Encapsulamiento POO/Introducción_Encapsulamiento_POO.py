class CajaFuerte:
    def __init__(self):
        self.publico = "Soy visible para todos"       # Nivel 1: Público
        self._protegido = "Debería ser secreto"       # Nivel 2: Protegido (Guiño guiño)
        self.__privado = "¡TOP SECRET!"               # Nivel 3: Privado (Name Mangling)

# Instanciamos
caja = CajaFuerte()

# 1. ACCESO PÚBLICO
print(f"Público: {caja.publico}")     # Funciona perfecto

# 2. ACCESO PROTEGIDO
# Python te deja hacerlo, pero te sientes sucio por dentro...
print(f"Protegido: {caja._protegido}") # Funciona, pero rompe las reglas de etiqueta

# 3. ACCESO PRIVADO
try:
    print(f"Privado: {caja.__privado}")
except AttributeError:
    print("❌ ERROR: ¡Python dice que 'CajaFuerte' no tiene atributo '__privado'!")
    # Explicación: ¡El atributo sí existe! Pero Python le cambió el nombre.

# 4. EL TRUCO (Name Mangling)
# Si realmente quieres ser un hacker rebelde, así se accede:
print(f"Hackeado: {caja._CajaFuerte__privado}") # Accedemos usando el nombre secreto