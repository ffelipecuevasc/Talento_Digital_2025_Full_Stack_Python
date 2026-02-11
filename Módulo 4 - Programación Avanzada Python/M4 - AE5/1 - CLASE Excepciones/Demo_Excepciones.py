# ---------------------------------------------------------
# DEMO: Provocando un desastre controlado
# Objetivo: Ver cómo Python "grita" cuando algo sale mal.
# ---------------------------------------------------------
print("--- Inicio del programa ---")
# Vamos a crear una lista pequeña de frutas
frutas = ["Manzana", "Banana", "Pera"] # Índices: 0, 1, 2
# INTENTO DE ERROR 1: Acceder a algo que no existe (IndexError)
# Queremos la fruta en la posición 10, pero solo hay hasta la 2.
# Python intentará buscarla, no la encontrará y lanzará la excepción.
# print(frutas[10]) <-- Si descomentas esto, verás un IndexError
# INTENTO DE ERROR 2: Matemáticas imposibles (ZeroDivisionError)
# Matemáticamente no se puede dividir naranjas entre 0 personas.
resultado = 10 / 0 # <-- ¡BOOM! Aquí muere el programa
# Esta línea JAMÁS se ejecutará porque el programa murió arriba
print("--- Fin del programa (Si lees esto, sobreviviste) ---")