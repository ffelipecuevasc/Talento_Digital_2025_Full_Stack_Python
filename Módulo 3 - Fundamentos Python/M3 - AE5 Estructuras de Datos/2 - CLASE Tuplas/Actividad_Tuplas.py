# --- DEMO: REGISTRO DE COORDENADAS GEOGRÁFICAS ---

# 1. Crear una tupla con las coordenadas de una ciudad (Latitud, Longitud)
# Usamos Valdivia, Chile como ejemplo.
coordenadas_ciudad = (-39.8142, -73.2459)

# 2. Mostrar las coordenadas por pantalla
print(f"Coordenadas originales: {coordenadas_ciudad}")

# 3. Acceder al valor de latitud y longitud por índice
latitud = coordenadas_ciudad[0]
longitud = coordenadas_ciudad[1]
print(f"Latitud: {latitud} | Longitud: {longitud}")

# 4. Intentar modificar la tupla (y provocar un error)
print("\nIntentando hackear las coordenadas...")
try:
    coordenadas_ciudad[0] = -10.0000  # Intentamos cambiar la latitud
except TypeError as error:
    # Esto captura el error para que el programa no se detenga y te muestra qué pasó
    print(f"¡ERROR DETECTADO! 🛑 No se puede modificar una tupla. Detalle: {error}")

# 5. Reemplazar la tupla completa si es necesario
# Como no podemos cambiar un dato interno, si la ciudad cambia, debemos crear una tupla NUEVA.
print("\nActualizando ubicación completa...")
coordenadas_ciudad = (-33.4489, -70.6693)  # Cambiamos a Santiago
print(f"Nueva ubicación (variable reescrita): {coordenadas_ciudad}")

# 6. Usar tuplas dentro de una lista para múltiples registros
# Esto es muy común: Una lista (mutable) que contiene tuplas (inmutables).
print("\n--- Cargando Mapa de Ciudades ---")
mapa_ciudades = [
    ("Buenos Aires", -34.6037, -58.3816),
    ("Bogotá", 4.7110, -74.0721),
    ("Madrid", 40.4168, -3.7038)
]

# 7. Iterar sobre la lista de tuplas y mostrar cada ciudad
for ciudad in mapa_ciudades:
    nombre = ciudad[0]
    lat = ciudad[1]
    lon = ciudad[2]

    # 8. Imprimir mensajes formateados
    print(f"📍 La ciudad {nombre} está ubicada en (Lat: {lat}, Long: {lon})")

print("\n¡Registro de coordenadas finalizado con éxito!")