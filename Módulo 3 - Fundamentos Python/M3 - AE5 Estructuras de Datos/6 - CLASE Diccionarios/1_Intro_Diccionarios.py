# 1. CREACIÓN: Vamos a crear un diccionario que representa a un Superhéroe
# Usamos llaves {} y separamos la clave del valor con dos puntos :
superheroe = {
    "alias": "Iron Man",
    "nombre_real": "Tony Stark",
    "nivel_poder": 85
}

print("--- Héroe Inicial ---")
print(superheroe)

# 2. LEER (READ): Accedemos a un valor específico usando su clave
# Es como decir: "Del diccionario superheroe, dame lo que tenga la etiqueta 'alias'"
print(f"\nEl héroe es: {superheroe['alias']}")

# 3. ACTUALIZAR (UPDATE): Tony mejoró su armadura
# Si la clave 'nivel_poder' ya existe, actualiza su valor.
superheroe["nivel_poder"] = 99
print(f"¡Poder actualizado! Nuevo nivel: {superheroe['nivel_poder']}")

# 4. CREAR NUEVO CAMPO: Agregamos información que no existía
# Como la clave 'equipo' no existe, Python la crea y le asigna el valor.
superheroe["equipo"] = "Avengers"

# 5. ELIMINAR (DELETE): Tony revela su identidad, ya no necesita alias secreto (o quizás sí, pero borremoslo)
# .pop() elimina la clave y nos devuelve el valor que tenía (por si lo necesitamos)
alias_borrado = superheroe.pop("alias")
print(f"\nSe eliminó el alias: {alias_borrado}")

# 6. USO SEGURO CON .GET()
# Intentamos buscar algo que no existe, como 'planeta_origen'.
# Si usáramos superheroe['planeta'], el programa fallaría. Con .get() es seguro.
planeta = superheroe.get("planeta_origen", "Planeta Tierra (Valor por defecto)")
print(f"Origen: {planeta}")

print("\n--- Estado Final del Héroe ---")
# Usamos .items() para ver tanto la clave como el valor en un ciclo
for clave, valor in superheroe.items():
    print(f"- {clave}: {valor}")