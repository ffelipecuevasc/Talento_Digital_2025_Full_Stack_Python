# “Filtro de becas express”
# Mezcla de comparación + operadores lógicos (and, or, not)

# 1) Datos del estudiante (puedes cambiarlos)
edad = 20                    # entero
promedio = 6.4               # decimal
asistencia = 92              # porcentaje (int o float)
situacion_economica = "vulnerable"  # texto: "vulnerable" o "media" (ejemplo)

# 2) Reglas de becas (al menos 2, aquí van 3)

# Beca Joven: edad menor a cierta cantidad Y promedio alto
tiene_beca_joven = (edad < 23) and (promedio >= 5.5)

# Beca Excelencia: promedio muy alto Y asistencia alta
# (agrego OR para practicar: si tiene 7.0, también califica)
tiene_beca_excelencia = ((promedio >= 6.5) and (asistencia >= 90)) or (promedio == 7.0)

# Beca Apoyo Económico: situación vulnerable Y promedio aceptable
# (uso NOT para practicar: "no es menor que 4.8" equivale a ">= 4.8")
tiene_beca_apoyo = (situacion_economica == "vulnerable") and (not (promedio < 4.8))

# 3) Mostrar resumen de datos
print("=== DATOS DEL ESTUDIANTE ===")
print("Edad:", edad)
print("Promedio:", promedio)
print("Asistencia:", asistencia)
print("Situación económica:", situacion_economica)

# 4) Mostrar resultado lógico y mensajes claros
print("\n=== RESULTADOS DE BECAS ===")

print("Obtienes la Beca Joven:", tiene_beca_joven)
if tiene_beca_joven == True:
    print("Felicitaciones, obtienes la Beca Joven")
else:
    print("No cumples las condiciones para la Beca Joven")

print("\nObtienes la Beca Excelencia:", tiene_beca_excelencia)
if tiene_beca_excelencia == True:
    print("Felicitaciones, obtienes la Beca Excelencia")
else:
    print("No cumples las condiciones para la Beca Excelencia")

print("\nObtienes la Beca Apoyo Económico:", tiene_beca_apoyo)
if tiene_beca_apoyo == True:
    print("Felicitaciones, obtienes la Beca Apoyo Económico")
else:
    print("No cumples las condiciones para la Beca Apoyo Económico")