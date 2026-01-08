from collections import Counter

# --- PASO 1 y 2: Registro de Libros (Diccionarios Anidados y Tuplas) ---
# Clave: Código único (ID)
# Valor: Diccionario con detalles. Nota el uso de TUPLA para (Autor, Año)
biblioteca = {
    "B001": {
        "titulo": "Cien Años de Soledad",
        "autor": ("Gabriel García Márquez", 1967),  # Tupla inmutable
        "genero": "Realismo Mágico",
        "stock": 5
    },
    "B002": {
        "titulo": "1984",
        "autor": ("George Orwell", 1949),
        "genero": "Ciencia Ficción",
        "stock": 2  # Stock bajo para probar alertas
    },
    "B003": {
        "titulo": "El Hobbit",
        "autor": ("J.R.R. Tolkien", 1937),
        "genero": "Fantasía",
        "stock": 8
    },
    "B004": {
        "titulo": "Harry Potter y la Piedra Filosofal",
        "autor": ("J.K. Rowling", 1997),
        "genero": "Fantasía",
        "stock": 10
    }
}
print("📚 Biblioteca inicializada correctamente.\n")

# --- PASO 3: Mostrar todos los libros disponibles ---
print("--- Catálogo Completo ---")
for codigo, info in biblioteca.items():
    # Desempaquetamos la tupla de autor para mostrarla bonito
    autor_nombre, autor_anio = info["autor"]
    print(f"[{codigo}] {info['titulo']} - {autor_nombre} ({autor_anio}) | Gen: {info['genero']}")

# --- PASO 4: Consultar libros por género (Usando Sets) ---
# Primero, obtenemos los géneros únicos usando un SET para mostrarlos al usuario
generos_disponibles = set()
for libro in biblioteca.values():
    generos_disponibles.add(libro["genero"])

print(f"\nGéneros disponibles: {generos_disponibles}")

# Simulamos que el usuario busca 'Fantasía'
genero_buscado = "Fantasía"
print(f"\n🔎 Buscando libros de: '{genero_buscado}'...")

encontrados = []
for info in biblioteca.values():
    if info["genero"] == genero_buscado:
        encontrados.append(info["titulo"])

print(f"Resultados: {encontrados}")

# --- PASO 5: Estadísticas con Counter ---
# Extraemos una lista con todos los géneros de todos los libros
lista_generos = [libro["genero"] for libro in biblioteca.values()]

# Counter hace el trabajo sucio de contar
estadisticas = Counter(lista_generos)
print("\n📊 Estadísticas de la Biblioteca:")
print(estadisticas)  # Ej: Counter({'Fantasía': 2, 'Realismo Mágico': 1...})

# --- PASO 6: Verificación de Stock (Alertas) ---
print("\n⚠️ Alerta de Stock Bajo (Menos de 3 unidades):")
for codigo, info in biblioteca.items():
    if info["stock"] < 3:
        print(f" -> ¡URGENTE! Reponer: {info['titulo']} (Quedan {info['stock']})")

# --- PASO 7: Agregar y Actualizar ---
# Actualizar stock de uno existente
biblioteca["B002"]["stock"] += 5
print(f"\n📦 Stock actualizado de '1984': Ahora hay {biblioteca['B002']['stock']}")

# Agregar nuevo libro
biblioteca["B005"] = {
    "titulo": "El Código Da Vinci",
    "autor": ("Dan Brown", 2003),
    "genero": "Misterio",
    "stock": 12
}
print(f"✨ Nuevo libro registrado: {biblioteca['B005']['titulo']}")

# --- PASO 8 (Bonus): Eliminar un libro ---
# Eliminamos 'El Hobbit' (B003)
libro_eliminado = biblioteca.pop("B003", None)
if libro_eliminado:
    print(f"\n🗑️ Se ha eliminado del catálogo: {libro_eliminado['titulo']}")
else:
    print("\n❌ El libro no existía.")