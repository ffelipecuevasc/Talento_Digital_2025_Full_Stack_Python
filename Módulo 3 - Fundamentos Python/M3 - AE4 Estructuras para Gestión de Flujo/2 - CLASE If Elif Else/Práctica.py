# Pedimos la temperatura al usuario (entra como texto).
temp_texto = input("Ingresa la temperatura en °C: ")  # El usuario escribe un número.

# Convertimos a float por si ponen decimales (por ejemplo 18.5).
temp = float(temp_texto)  # Esto permite trabajar con temperaturas como 12.3 o 20.0.

# Validación básica: temperaturas extremadamente raras (fuera de rango razonable).
if temp < -50 or temp > 60:  # Rango “realista” para una actividad cotidiana.
    print("❌ Temperatura inválida o poco realista. Revisa el dato.")  # Mensaje claro para el usuario.

# Si está en rango razonable, damos recomendación según tramos.
elif temp < 10:  # Menos de 10°C.
    print("🧥 Hace frío: usa abrigo, pantalón largo y algo para el cuello.")  # Recomendación de frío.

elif temp < 20:  # Desde 10°C hasta 19.999...
    print("🧢 Clima fresco: una chaqueta ligera o polerón estará perfecto.")  # Recomendación intermedia.

elif temp < 30:  # Desde 20°C hasta 29.999...
    print("👕 Clima agradable: polera y ropa ligera.")  # Recomendación templada.

else:  # 30°C o más.
    print("🩳 Hace calor: ropa muy ligera, hidrátate y usa bloqueador.")  # Recomendación de calor.