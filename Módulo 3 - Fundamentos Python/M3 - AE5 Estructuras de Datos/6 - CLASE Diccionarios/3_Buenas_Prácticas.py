# --- 1. COMPRENSIONES (Comprehensions) ---
print("--- 1. Comprensiones ---")
# Tradicional (Largo)
numeros = [1, 2, 3, 4, 5]
cuadrados_dict_tradicional = {}
for n in numeros:
    cuadrados_dict_tradicional[n] = n**2

# Pythonico (Elegante): {clave: valor for variable in iterable}
# Crea el mismo diccionario en una sola línea.
cuadrados_dict_pro = {n: n**2 for n in numeros}

print(f"Tradicional: {cuadrados_dict_tradicional}")
print(f"Pythonico:   {cuadrados_dict_pro}")

# --- 2. GENERADORES (Yield) ---
print("\n--- 2. Generadores ---")
# Definimos una función que no 'retorna' todo, sino que 'cede' (yield) valores uno a uno
def generador_numeros(maximo):
    for i in range(maximo):
        yield i  # Aquí pausa la ejecución y entrega el valor

# Creamos el objeto generador (no ocupa memoria todavía)
mi_generador = generador_numeros(3)

# Pedimos los valores bajo demanda
print(next(mi_generador)) # Entrega 0
print(next(mi_generador)) # Entrega 1
print(next(mi_generador)) # Entrega 2
# Si pidiéramos uno más, daría error StopIteration porque se acabó la secuencia.