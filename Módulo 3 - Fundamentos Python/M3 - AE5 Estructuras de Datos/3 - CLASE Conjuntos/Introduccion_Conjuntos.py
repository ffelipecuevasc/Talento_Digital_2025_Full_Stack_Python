# 1. Creación y Eliminación de Duplicados
# Intentamos crear un set con números repetidos
numeros_locos = {1, 2, 2, 3, 3, 3, 4}
print(f"Set original (sin duplicados): {numeros_locos}")
# Resultado: {1, 2, 3, 4} ¡Magia!

# 2. Operaciones Matemáticas (Diagramas de Venn)
amigos_futbol = {"Juan", "Pedro", "Luis"}
amigos_fiesta = {"Pedro", "Ana", "Luis", "Marta"}

# INTERSECCIÓN (&): ¿Quiénes van al fútbol Y a la fiesta?
# Busca los elementos que están en AMBOS grupos.
en_ambos_lados = amigos_futbol.intersection(amigos_fiesta)
# También se puede escribir: amigos_futbol & amigos_fiesta
print(f"Amigos en ambos planes: {en_ambos_lados}") # Pedro y Luis

# UNIÓN (|): Quiero invitar a TODOS (sin invitar doble a nadie).
# Junta los dos grupos en uno solo.
todos_los_amigos = amigos_futbol.union(amigos_fiesta)
# También se puede escribir: amigos_futbol | amigos_fiesta
print(f"Lista completa de invitados: {todos_los_amigos}")

# DIFERENCIA (-): ¿Quiénes son solo del fútbol (y no van a la fiesta)?
solo_futbol = amigos_futbol.difference(amigos_fiesta)
print(f"Solo van al fútbol: {solo_futbol}") # Juan