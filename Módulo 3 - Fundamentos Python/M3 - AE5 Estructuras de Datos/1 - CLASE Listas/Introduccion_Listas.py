# 1. Creación: Definimos una lista con cosas variadas (Texto, Números, Booleanos)
# Imagina que es tu bolsillo: Tienes llaves, dinero, un chicle y... ¿pi?
mi_bolsillo = ["Llaves", 500, True, 3.14]
print("Mi bolsillo inicial:", mi_bolsillo)

# 2. Acceso: Vamos a ver qué hay en la primera posición.
# RECUERDA: En programación, contamos desde CERO.
print("Lo primero que encuentro es:", mi_bolsillo[0]) # Imprime "Llaves" [cite: 89]

# 3. Modificación: ¡Oh no! Gasté los 500 pesos. Vamos a cambiarlos por monedas.
mi_bolsillo[1] = "Monedas" # Accedemos al índice 1 y lo sobrescribimos [cite: 91]
print("Bolsillo actualizado:", mi_bolsillo)

# 4. Método append(): Encontré un ticket viejo, lo guardo al final.
mi_bolsillo.append("Ticket viejo") # Se agrega al final de la lista
print("Después de encontrar basura:", mi_bolsillo)

# 5. Método insert(): Quiero guardar mi celular en un lugar seguro (posición 1).
mi_bolsillo.insert(1, "Celular") # Todo lo demás se corre a la derecha
print("Guardando el celu:", mi_bolsillo)

# 6. Método pop(): Saco lo último que metí (o lo que esté al final) para tirarlo.
objeto_sacado = mi_bolsillo.pop() # Elimina el último elemento y lo guarda en la variable
print(f"Acabo de sacar y tirar: {objeto_sacado}")
print("Cómo quedó el bolsillo:", mi_bolsillo)