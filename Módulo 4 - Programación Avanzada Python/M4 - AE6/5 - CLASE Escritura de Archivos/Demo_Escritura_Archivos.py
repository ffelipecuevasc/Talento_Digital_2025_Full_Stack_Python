# --- PARTE 1: CREANDO LA LISTA (Modo 'w') ---
print("📝 Creando la lista de invitados...")

# Abrimos en modo 'w'. Si 'invitados.txt' existía, se borra todo.
fichero = open("invitados.txt", "w")

# Usamos write(). Nota el '\n' para saltar de línea.
fichero.write("1. Ana (La anfitriona)\n")
fichero.write("2. Beto (Trae la música)\n")

# Usamos writelines() con una lista.
# OJO: Fíjate que tuve que poner '\n' en cada elemento manualmente.
otros_invitados = ["3. Carla\n", "4. Diego\n"]
fichero.writelines(otros_invitados)

fichero.close() # ¡Crucial para guardar los cambios!
print("✅ Lista creada y cerrada.")

# --- PARTE 2: LLEGÓ ALGUIEN TARDE (Modo 'a') ---
print("\n➕ Llegó un invitado tarde. Agregándolo...")

# Abrimos en modo 'a' (Append). NO borra lo anterior.
fichero_append = open("invitados.txt", "a")

# Agregamos al final
fichero_append.write("5. Elena (Llegó tarde)\n")

fichero_append.close()
print("✅ Invitado agregado.")

# --- PARTE 3: VERIFICACIÓN ---
print("\n👀 Leamos cómo quedó la lista final:")
lectura = open("invitados.txt", "r")
print(lectura.read())
lectura.close()