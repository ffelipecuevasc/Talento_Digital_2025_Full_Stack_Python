# --- 1. DICCIONARIOS ANIDADOS (La Matryoshka) ---
# Base de datos de jugadores
jugadores = {
    "player1": {
        "nombre": "Mario",
        "nivel": 10,
        "inventario": {"monedas": 50, "vidas": 3} # ¡Un diccionario dentro de otro dentro de otro!
    },
    "player2": {
        "nombre": "Luigi",
        "nivel": 8,
        "inventario": {"monedas": 10, "vidas": 5}
    }
}

# Accediendo a un dato profundo: Las monedas de Mario
monedas_mario = jugadores["player1"]["inventario"]["monedas"]
print(f"Monedas de Mario: {monedas_mario}")


# --- 2. MÉTODO .SETDEFAULT() ---
# Queremos ver el puntaje. Si no existe, lo creamos en 0.
# Observa que 'puntaje' NO existe en player1.
puntaje = jugadores["player1"].setdefault("puntaje", 0)
print(f"Puntaje inicializado: {puntaje}")
print(f"Jugador 1 actualizado: {jugadores['player1']}")


# --- 3. MÉTODO .UPDATE() (La Fusión) ---
configuracion_actual = {"sonido": "ON", "brillo": 50}
nuevos_ajustes = {"brillo": 100, "dificultad": "Difícil"} # Brillo cambia, Dificultad se agrega

print("\nConfiguración antes:", configuracion_actual)
configuracion_actual.update(nuevos_ajustes)
print("Configuración después (Fusión):", configuracion_actual)


# --- 4. ITERACIÓN CON FILTRADO ---
print("\n--- Jugadores Avanzados (Nivel > 9) ---")
for id_jugador, datos in jugadores.items():
    # 'datos' es el diccionario interno
    if datos["nivel"] > 9:
        print(f"PRO: {datos['nombre']} - Nivel {datos['nivel']}")