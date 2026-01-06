# --- DEMO: COMPARACIÓN DE USUARIOS ENTRE PLATAFORMAS ---

# 1. Crear dos listas de usuarios con posibles repetidos
# Imagina que extrajimos esto de una base de datos "sucia"
lista_plataforma_A = ["Ana", "Beto", "Carla", "Ana", "Daniel"] # Ana está repetida
lista_plataforma_B = ["Carla", "Daniel", "Elena", "Elena", "Fabio"] # Elena está repetida

print("Listas originales (sucias):")
print(f"A: {lista_plataforma_A}")
print(f"B: {lista_plataforma_B}")

# 2. Convertir las listas en conjuntos para eliminar duplicados
# Usamos set() para transformar la lista y limpiar la basura
set_A = set(lista_plataforma_A)
set_B = set(lista_plataforma_B)

# 3. Mostrar los usuarios únicos de cada plataforma
print("\n--- Usuarios Únicos (Limpios) ---")
print(f"Usuarios A: {set_A}")
print(f"Usuarios B: {set_B}")

# 4. Calcular la intersección (usuarios en ambas plataformas)
# Clientes que usan A y B al mismo tiempo
comunes = set_A.intersection(set_B)
print(f"\nUsuarios en AMBAS plataformas (Coincidencias): {comunes}")

# 5. Calcular la unión (todos los usuarios sin duplicados)
# Base de datos total de clientes
total_usuarios = set_A.union(set_B)
print(f"Total de usuarios únicos en la empresa: {total_usuarios}")

# 6. Calcular diferencia (usuarios solo en una plataforma)
# Usuarios exclusivos de A (que no están en B)
solo_en_A = set_A.difference(set_B)
print(f"Usuarios exclusivos de Plataforma A: {solo_en_A}")

# 7. Usar add() y remove() para modificar un set
print("\n--- Actualización de Datos ---")
# Llegó un usuario nuevo a A
set_A.add("Gustavo")
print("Se registró Gustavo en A.")

# Un usuario se dio de baja en A
# Usamos discard() en lugar de remove() porque si no existe, no da error (más seguro)
set_A.discard("Ana")
print("Ana se dio de baja en A.")

# 8. Recorrer un set con for e imprimir los resultados
print("\n--- Reporte Final de Plataforma A ---")
for usuario in set_A:
    print(f"Cliente activo: {usuario}")