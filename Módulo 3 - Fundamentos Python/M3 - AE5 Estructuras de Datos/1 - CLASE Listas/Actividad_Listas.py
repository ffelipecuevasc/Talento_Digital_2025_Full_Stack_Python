# --- DEMO: GESTOR DE TAREAS (TO-DO LIST) ---

# 1. Crear una lista inicial con tareas pendientes [cite: 122]
tareas = ["Comprar leche", "Estudiar Python", "Lavar los platos"]

# 2. Mostrar todas las tareas actuales [cite: 124]
print("--- Tareas Iniciales ---")
print(tareas)

# 3. Agregar una nueva tarea a la lista (Usamos append porque va al final) [cite: 126]
print("\nAgregando nueva tarea...")
tareas.append("Pasear al perro")

# 5. Recorrer e imprimir la lista de tareas con un for (Iteración) [cite: 129]
# Esto es vital para mostrar los datos de forma ordenada al usuario
print("\n--- Lista de Tareas Actualizada ---")
for tarea in tareas:
    print(f"- {tarea}")

# 4. y 6. Marcar una tarea como completada (eliminarla) usando pop() [cite: 128, 131]
# Vamos a eliminar la tarea en el índice 0 ("Comprar leche") porque ya la hicimos.
print("\nCompletando la primera tarea...")
tarea_completada = tareas.pop(0)
print(f"¡Genial! Completaste: {tarea_completada}")

# Verificamos cómo quedó la lista
print("Tareas restantes:", tareas)

# 7. Validar si la lista está vacía [cite: 133]
# (Para este ejemplo, forzaremos el vaciado para que veas el mensaje final)
print("\n...Haciendo todas las tareas rápido...")
tareas.clear() # Truco extra: clear() borra todo de golpe

if len(tareas) == 0:
    # 8. Mostrar mensaje de cierre [cite: 135]
    print("\n¡Todas las tareas completadas! Eres una máquina de productividad. 🚀")
else:
    print(f"\nAún te quedan {len(tareas)} tareas por hacer.")