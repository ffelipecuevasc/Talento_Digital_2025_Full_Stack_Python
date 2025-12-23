# Estructura de decisión IF - ELIF - ELSE

# Pedimos el puntaje al usuario (entra como texto).
puntaje_texto = input("Ingresa tu puntaje (0 a 100): ")  # Capturamos lo que escribe el usuario.

# Convertimos el puntaje a entero para poder compararlo con números.
puntaje = int(puntaje_texto)  # Sin convertir, no podemos hacer comparaciones numéricas confiables.

# Primero validamos si el puntaje está dentro de un rango lógico.
if puntaje < 0 or puntaje > 100:  # Si es menor que 0 O mayor que 100, es inválido.
    print("❌ Puntaje inválido. Debe estar entre 0 y 100.")  # Caso “fuera de rango”.

# Si no fue inválido, ahora sí clasificamos por rangos.
elif puntaje >= 90:  # 90 a 100.
    print("🌟 Excelente")  # Categoría más alta.

elif puntaje >= 70:  # 70 a 89 (porque si fuera 90+, ya habría entrado arriba).
    print("💪 Muy bueno")  # Segunda categoría.

elif puntaje >= 50:  # 50 a 69.
    print("👍 Bueno")  # Tercera categoría.

else:  # 0 a 49 (todo lo que quedó).
    print("🛠️ Necesita mejorar")  # Caso por defecto dentro del rango válido.