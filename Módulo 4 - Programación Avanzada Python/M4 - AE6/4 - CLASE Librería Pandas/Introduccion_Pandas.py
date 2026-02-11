import pandas as pd

print("🥇 --- DEMO PANDAS: ANÁLISIS DE MEDALLAS --- 🥇")

# 1. CARGA DE DATOS
# Usamos read_csv para "aspirar" los datos.
# Asumimos que el archivo está separado por comas (default).
try:
    df = pd.read_csv("medallas.csv")
    print("✅ Archivo cargado correctamente en un DataFrame.")
except FileNotFoundError:
    print("❌ Error: No se encuentra el archivo 'medallas.csv'.")
    exit()

print("-" * 40)

# 2. EXPLORACIÓN INICIAL (Mirando a través de la cerradura)
print("🔍 VISTAZO RÁPIDO (df.head()):")
# Mostramos las primeras 5 filas para entender las columnas
print(df.head())

print("\n📏 DIMENSIONES (df.shape):")
# (Filas, Columnas)
print(f"Tenemos {df.shape[0]} países y {df.shape[1]} columnas de datos.")

print("-" * 40)

# 3. RADIOGRAFÍA DE DATOS (df.info())
print(" ESTADO DE SALUD DE LOS DATOS (df.info()):")
# Esto es CRÍTICO. Fíjate en la columna 'Non-Null Count'.
# Si es menor al total de filas, ¡significa que faltan datos (NaN)!
df.info()
print("👉 Nota: Si ves 'NaN' en la salida anterior, son medallas que faltan (probablemente 0).")

print("-" * 40)

# 4. ESTADÍSTICAS AUTOMÁTICAS (df.describe())
print("📊 RESUMEN ESTADÍSTICO (df.describe()):")
# Calcula media, desviación, min, max, cuartiles para columnas numéricas (Oro, Plata, Bronce, Total)
# Fíjate cómo ignora automáticamente la columna 'Pais' (texto).
print(df.describe())

print("-" * 40)

# 5. CONTEO DE FRECUENCIAS (value_counts())
# Vamos a ver cuántos países tienen el mismo número TOTAL de medallas.
print("🔢 FRECUENCIA DE MEDALLAS TOTALES (value_counts):")
conteo = df['Total'].value_counts()
print("¿Cuántos países ganaron X cantidad de medallas en total?")
print(conteo.head(5)) # Mostramos solo el top 5 de frecuencias
print("(Ejemplo: Si dice '1    15', significa que 15 países ganaron exactamente 1 medalla)")