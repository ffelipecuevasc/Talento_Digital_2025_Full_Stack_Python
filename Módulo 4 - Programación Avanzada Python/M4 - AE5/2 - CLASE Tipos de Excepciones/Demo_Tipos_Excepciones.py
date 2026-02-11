# ==============================================================================
# DEMO: TIPOS DE EXCEPCIONES (Basado en Pág. 12 del PDF M4 AE5)
# Objetivo: Identificar qué línea provoca qué error y leer el mensaje de Python.
# INSTRUCCIONES: Descomenta (quita el #) UNA línea a la vez y ejecuta.
# ==============================================================================
print("--- INICIANDO LABORATORIO DE ERRORES ---")
# ---------------------------------------------------------
# CASO 1: ZeroDivisionError
# Intentamos dividir por cero.
# ---------------------------------------------------------
# print(10 / 0)
# MENSAJE ESPERADO: ZeroDivisionError: division by zero
# ---------------------------------------------------------
# CASO 2: ValueError
# Intentamos convertir texto no numérico a entero.
# "veinticinco" es texto, no digitos.
# ---------------------------------------------------------
# edad = int("veinticinco")
# MENSAJE ESPERADO: ValueError: invalid literal for int() with base 10: 'veinticinco'
# ---------------------------------------------------------
# CASO 3: IndexError
# Accedemos a una posición que no existe en la lista.
# La lista tiene 3 elementos (índices 0, 1, 2). Pedimos el 5.
# ---------------------------------------------------------
lista = [1, 2, 3]
# print(lista[5])
# MENSAJE ESPERADO: IndexError: list index out of range
# ---------------------------------------------------------
# CASO 4: KeyError
# Buscamos una clave que no existe en el diccionario.
# Tenemos la clave "nombre", pero pedimos "apellido".
# ---------------------------------------------------------
datos = {"nombre": "Ana"}
# print(datos["apellido"])
# MENSAJE ESPERADO: KeyError: 'apellido'
# ---------------------------------------------------------
# CASO 5: TypeError
# Operación entre tipos incompatibles (Número + Texto).
# ---------------------------------------------------------
# resultado = 10 + "5"
# MENSAJE ESPERADO: TypeError: unsupported operand type(s) for +: 'int' and 'str'
print("--- FIN DEL LABORATORIO ---")