# --- RESOLUCIÓN DEMO: PERFIL DE USUARIO ---

# 1. Crear un diccionario con los datos: nombre, edad, email
# Definimos la estructura inicial como se pide.
persona = {
    "nombre": "Ana",
    "edad": 25,
    "email": "ana@example.com"
}
print(f"1. Diccionario inicial: {persona}")

# 2. Acceder a valores usando claves
# Obtenemos el valor asociado a "nombre"
nombre_actual = persona["nombre"]
print(f"2. Accediendo al nombre: {nombre_actual}")

# 3. Modificar un dato (Actualizar la edad)
# Ana cumplió años, así que sobreescribimos el valor de 'edad'
persona["edad"] = 26
print(f"3. Edad actualizada: {persona['edad']}")

# 4. Agregar un nuevo dato ("país": "Argentina")
# Insertamos una clave nueva simplemente asignándole un valor
persona["pais"] = "Argentina"
print(f"4. Nuevo campo 'pais' agregado: {persona}")

# 5. Eliminar un campo con pop() o del
# Vamos a eliminar el 'email' usando pop (que es más seguro porque devuelve el valor)
email_eliminado = persona.pop("email")
print(f"5. Email eliminado: {email_eliminado}")

# 6. Mostrar claves, valores y pares
print("\n6. Inspeccionando el diccionario:")
print(f"   - Claves (Keys): {list(persona.keys())}")
print(f"   - Valores (Values): {list(persona.values())}")
print(f"   - Items (Pares): {list(persona.items())}")

# 7. Iterar sobre el diccionario e imprimir "clave: valor"
print("\n7. Iterando sobre el perfil:")
for clave, valor in persona.items():
    print(f"   -> {clave}: {valor}")

# 8. Usar get() para obtener un dato sin error
# Buscamos 'telefono' que no existe en el diccionario
telefono = persona.get("telefono", "No registrado")
print(f"\n8. Buscando teléfono (seguro): {telefono}")