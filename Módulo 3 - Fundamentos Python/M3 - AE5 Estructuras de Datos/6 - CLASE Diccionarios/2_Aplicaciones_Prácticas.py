# Lista de votos que llegaron (observa que están desordenados y repetidos)
votos_recibidos = ["Perro", "Gato", "Perro", "Hamster", "Gato", "Perro", "Iguana"]

# 1. Creamos la "urna" vacía
urna_votos = {}

print(f"--- Iniciando conteo de {len(votos_recibidos)} votos ---")

# 2. Procesamos voto por voto
for mascota in votos_recibidos:
    # Verificamos si la mascota ya tiene una 'urna' (clave en el diccionario)
    if mascota in urna_votos:
        # Si ya existe, le sumamos 1 a lo que ya tenía
        urna_votos[mascota] += 1
        print(f"¡Otro voto para {mascota}!")
    else:
        # Si es la primera vez que la vemos, la creamos con valor 1
        urna_votos[mascota] = 1
        print(f"Primer voto registrado para: {mascota}")

print("\n--- Resultados Finales ---")
print(urna_votos)
# Resultado esperado: {'Perro': 3, 'Gato': 2, 'Hamster': 1, 'Iguana': 1}