# --- MODO EXPERTO (Con Funciones) ---
# Definimos la "receta" una sola vez.

def saludar_empleado():
    # Todo lo que esté indentado (con sangría) pertenece a la función
    print("¡Hola! Bienvenido al equipo.")
    print("Esperamos que aprendas mucho con nosotros.")
    print("--- Fin del saludo ---")

# Ahora, simplemente "llamamos" a la función tres veces.
# Python va a la "receta" arriba, la ejecuta y vuelve aquí.
saludar_empleado()
saludar_empleado()
saludar_empleado()

# ¡Mira qué limpio! Si quieres cambiar el saludo, solo tocas la definición arriba
# y se actualiza para los tres automáticamente. ¡Magia!