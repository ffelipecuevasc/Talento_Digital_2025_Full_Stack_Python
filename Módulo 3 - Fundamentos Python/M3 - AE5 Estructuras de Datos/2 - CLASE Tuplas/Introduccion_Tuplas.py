# 1. Creación: Usamos paréntesis.
# Imagina que definimos los días del fin de semana. ¡Nadie puede agregar un tercer día!
fin_de_semana = ("Sábado", "Domingo")
print(f"Días de descanso: {fin_de_semana}")

# 2. Acceso: Igual que en las listas, usamos el índice (empezando en 0).
primer_dia = fin_de_semana[0] # Accedemos al índice 0
print(f"El primer día es: {primer_dia}") # Imprime "Sábado"

# 3. La Prueba de Fuego (Inmutabilidad):
# Si intentas ejecutar la siguiente línea (quitándole el #), Python te dará un error.
# fin_de_semana[0] = "Lunes"
# Error: 'tuple' object does not support item assignment
# (Traducido: ¡Oye! ¡No puedes cambiar una piedra tallada!)

print("Como ves, no podemos cambiar 'Sábado' por 'Lunes'. ¡Los datos están protegidos!")