# --- ENFOQUE ANTIGUO (El que colapsa el servidor) ---
def generar_lista_matriculas_pesada(cantidad):
    print(f"🥵 Intentando crear lista de {cantidad} matrículas en memoria...")
    lista_completa = []
    # Este bucle se ejecuta COMPLETO antes de devolver nada
    for i in range(cantidad):
        codigo = f"MAT-2024-{i}"
        lista_completa.append(codigo)  # ¡La memoria RAM se empieza a llenar!

    print("✅ Lista creada (¡Si es que la RAM aguantó!). Entregando todo...")
    return lista_completa  # Devuelve un objeto GIGANTE de una sola vez


# --- ENFOQUE MODERNO CON YIELD (La máquina eficiente) ---
# Esto es un GENERADOR. No guarda nada, es "bajo demanda".
def generador_matriculas_eficiente(cantidad):
    print(f"😎 Encendiendo la máquina expendedora de matrículas...")
    # Este bucle NO corre completo. Va paso a paso.
    for i in range(cantidad):
        codigo = f"MAT-2024-{i}"
        # --- LA MAGIA DE YIELD ---
        # 1. Entrega el código actual.
        # 2. PAUSA la función y recuerda dónde quedó.
        # 3. Espera a que le pidan el siguiente con next().
        yield codigo

    # --- PRUEBA DE FUEGO EN EL CAMPUS ---


# Simulamos una cantidad gigante de postulantes
CANTIDAD_MASIVA = 5000000

# 1. Prueba del método antiguo (¡CUIDADO! Podría poner lenta tu PC si descomentas esto)
# print("Probando método antiguo...")
# lista_gigante = generar_lista_matriculas_pesada(CANTIDAD_MASIVA)
# print(f"Primer alumno: {lista_gigante[0]}")
# (Si ejecutaras eso, tu computador sufriría mucho rato creando la lista antes de imprimir)


print("\n--- 2. Probando el Generador con Yield (Eficiente) ---")

# Creamos la "máquina expendedora" (¡Ojo! El código aún no se ejecuta, es instantáneo)
maquina_de_turnos = generador_matriculas_eficiente(CANTIDAD_MASIVA)

print("👨‍🎓 Llega el primer alumno a ventanilla...")
# Usamos la función nativa next() para pedirle UN dato al generador
matricula1 = next(maquina_de_turnos)
print(f"   -> Matrícula asignada: {matricula1}")

print("\n👩‍🎓 Llega el segundo alumno 10 minutos después...")
# El generador "despierta" donde quedó y nos da el siguiente
matricula2 = next(maquina_de_turnos)
print(f"   -> Matrícula asignada: {matricula2}")

print("\n✅ Conclusión: El servidor sigue funcionando rápido y sin gastar memoria.")
# Nota: Puedes iterar el generador con un 'for', pero next() muestra mejor la pausa.