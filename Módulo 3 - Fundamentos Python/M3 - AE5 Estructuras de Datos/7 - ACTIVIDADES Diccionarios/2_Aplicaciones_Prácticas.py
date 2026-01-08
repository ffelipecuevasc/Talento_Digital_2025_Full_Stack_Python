# --- RESOLUCIÓN DEMO: CONTADOR DE FRECUENCIA DE PALABRAS ---

# 1. Solicitar al usuario que ingrese una frase
# Para el ejemplo usamos una frase fija, pero podrías usar input()
frase = "Python es genial y Python es poderoso"
print(f"Frase original: '{frase}'")

# 2. Crear un diccionario vacío llamado frecuencia
frecuencia = {}

# 3. Dividir la frase en palabras usando .split()
# Esto crea una lista: ['Python', 'es', 'genial', 'y', 'Python', 'es', 'poderoso']
palabras = frase.split()
print(f"Lista de palabras: {palabras}")

# 4. Recorrer las palabras con un for
for palabra in palabras:
    # 5. Usar get() para contar (Estrategia Ninja 🥷)
    # frecuencia.get(palabra, 0) busca la palabra.
    # Si existe, trae su valor actual. Si no, devuelve 0.
    # Luego le sumamos 1 y guardamos el resultado.
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

# 6. Imprimir el diccionario final con las frecuencias
print("\n--- Frecuencia de Palabras ---")
print(frecuencia)

# 7. Bonus: Ordenar el diccionario por frecuencia descendente (Opcional)
# Esto crea una lista de tuplas ordenada por el valor (cantidad) de mayor a menor
ranking_ordenado = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

print("\n--- Ranking (Bonus) ---")
for palabra, cantidad in ranking_ordenado:
    print(f"'{palabra}': {cantidad} veces")