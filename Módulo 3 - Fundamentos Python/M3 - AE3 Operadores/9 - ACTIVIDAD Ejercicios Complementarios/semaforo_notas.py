# “Semáforo de notas”
# Operadores de comparación / relacionales

# 1) Definir 3 notas (puedes cambiarlas)
nota_python = 6.2
nota_html = 5.4
nota_css = 7.0

# 2) Nota mínima de aprobación (elige tú)
nota_minima = 4.0

# 3) Calcular promedio
promedio = (nota_python + nota_html + nota_css) / 3

# 4) Determinar nota más alta (sin max(), usando comparaciones)
mejor_ramo = ""
mejor_nota = 0

if nota_python >= nota_html:
    if nota_python >= nota_css:
        mejor_ramo = "Python"
        mejor_nota = nota_python
    else:
        mejor_ramo = "CSS"
        mejor_nota = nota_css
else:
    if nota_html >= nota_css:
        mejor_ramo = "HTML"
        mejor_nota = nota_html
    else:
        mejor_ramo = "CSS"
        mejor_nota = nota_css

# 5) Determinar nota más baja (sin min(), usando comparaciones)
peor_ramo = ""
peor_nota = 0

if nota_python <= nota_html:
    if nota_python <= nota_css:
        peor_ramo = "Python"
        peor_nota = nota_python
    else:
        peor_ramo = "CSS"
        peor_nota = nota_css
else:
    if nota_html <= nota_css:
        peor_ramo = "HTML"
        peor_nota = nota_html
    else:
        peor_ramo = "CSS"
        peor_nota = nota_css

# 6) Verificar si todas las notas son >= a la mínima (solo comparaciones)
aprueba_todo = True

if nota_python < nota_minima:
    aprueba_todo = False
if nota_html < nota_minima:
    aprueba_todo = False
if nota_css < nota_minima:
    aprueba_todo = False

# 7) Verificar si alguna nota es exactamente 7.0
tiene_siete = False

if nota_python == 7.0:
    tiene_siete = True
if nota_html == 7.0:
    tiene_siete = True
if nota_css == 7.0:
    tiene_siete = True

# 8) Mostrar por pantalla
print("PROMEDIO GENERAL:", promedio)
print("Tu mejor ramo es", mejor_ramo, "con nota", mejor_nota)
print("Tu peor ramo es", peor_ramo, "con nota", peor_nota)

if aprueba_todo == True:
    print("Aprobaste todos los ramos")
else:
    print("Tienes ramos reprobados")

if tiene_siete == True:
    print("¡Tienes al menos un 7.0!")