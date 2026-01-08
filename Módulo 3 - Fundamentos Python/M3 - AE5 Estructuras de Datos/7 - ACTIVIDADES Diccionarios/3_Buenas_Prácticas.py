# --- RESOLUCIÓN DEMO: OPTIMIZACIÓN CON COLLECTIONS ---

# 1. Importar las herramientas especiales
# Traemos defaultdict y Counter desde la librería estándar 'collections'
from collections import defaultdict, Counter

print("--- Parte A: Uso de defaultdict ---")

# 2. Crear un defaultdict que inicie valores en 0 (int)
# Al decirle 'int', si la clave no existe, asumirá que vale 0.
visitas = defaultdict(int)

# Simulamos visitas a una página
# 'inicio' no existe, pero gracias a defaultdict, se crea con 0 y se le suma 1.
visitas["inicio"] += 1
visitas["contacto"] += 1
visitas["inicio"] += 1  # Sumamos otra visita a inicio

print(f"Diccionario de visitas inteligente: {dict(visitas)}")
# Salida esperada: {'inicio': 2, 'contacto': 1}


print("\n--- Parte B: Uso de Counter ---")

# 3. Crear una lista con elementos repetidos
# Imagina que esto es un inventario desordenado
colores = ["azul", "rojo", "azul", "verde", "rojo", "rojo"]
print(f"Lista original: {colores}")

# 4. Usar Counter para contar automáticamente
# En una sola línea, hace todo el trabajo sucio de contar.
conteo = Counter(colores)

# 5. Mostrar el resultado
print(f"Conteo automático: {conteo}")
# Counter devuelve algo parecido a: {'rojo': 3, 'azul': 2, 'verde': 1}

# 6. Iterar sobre los resultados de forma legible
print("\n--- Reporte de Colores ---")
for color, cantidad in conteo.items():
    print(f"El color {color} aparece {cantidad} veces.")