# =============================================================================
# 8) Funciones Lambda: Procesamiento Masivo de Datos
# =============================================================================

# DATOS: Ingresos mensuales de 4 familias postulantes
ingresos = [350000, 480000, 290000, 600000]
print(f"Ingresos originales: {ingresos}")

# --- MISIÓN 1: Aplicar "Bono Universal" usando MAP ---
# El map transforma TODOS los datos de la lista.
# Lambda: "Toma el ingreso 'x' y súmale 10.000 pesos".
ingresos_ajustados = list(map(lambda x: x + 10000, ingresos))

# ¿Qué pasó? 350000 -> 360000, etc. (Todos subieron)
print(f"Con Bono Universal:  {ingresos_ajustados}")


# --- MISIÓN 2: Seleccionar postulantes usando FILTER ---
# El filter actúa como un colador. Solo pasan los que cumplen la regla.
# Regla: Solo califican quienes ganen menos de $500.000 (Tramo Vulnerable).
beneficiarios = list(filter(lambda x: x < 500000, ingresos_ajustados))

# ¿Qué pasó?
# 360000 -> Pasa (Es menor a 500k)
# 610000 -> NO Pasa (Es mayor)
print(f"Beneficiarios Finales: {beneficiarios}")

# ¡Lo logramos! Procesamos la planilla municipal en 2 líneas de código
# sin usar bucles ni definir funciones complejas.