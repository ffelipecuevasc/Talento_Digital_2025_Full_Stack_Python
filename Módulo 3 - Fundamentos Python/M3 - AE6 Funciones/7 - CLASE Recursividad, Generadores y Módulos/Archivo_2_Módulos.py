# --- ARCHIVO: intranet_profesor.py ---
import time
# 1. IMPORTAMOS nuestro módulo personalizado
# Ojo: El nombre del archivo debe ser exacto (sin .py)
import Archivo_1_Módulos as modulo

print("--- 🏫 SISTEMA DE GESTIÓN DOCENTE ---")
print("Bienvenido, Profesor. Ingrese las notas del alumno:")

# Solicitamos datos al usuario (Interfaz)
n1 = float(input("Nota Cátedra 1: "))
n2 = float(input("Nota Cátedra 2: "))
n3 = float(input("Nota Cátedra 3: "))

print("\nProcesando resultados con el reglamento oficial...")
time.sleep(1.5) # Un poco de drama...

# 2. USAMOS las funciones del módulo importado
# Sintaxis: modulo.funcion()

# Calculamos el promedio usando la fórmula externa
promedio_final = modulo.calcular_promedio(n1, n2, n3)

# Determinamos si pasó o no, usando la regla externa
situacion = modulo.obtener_situacion_final(promedio_final)

# Mostramos el reporte final
print("-" * 30)
print(f"📄 REPORTE FINAL DEL ALUMNO")
print(f"   Promedio:  {promedio_final}")
print(f"   Situación: {situacion}")
print("-" * 30)