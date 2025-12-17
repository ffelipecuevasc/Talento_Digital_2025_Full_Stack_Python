edad = 20
tiene_ticket = True
esta_en_lista = False

# AND: debe cumplir ambas
print("Entra (edad y ticket):", edad >= 18 and tiene_ticket)

# OR: basta con una condición
print("Entra (ticket o lista):", tiene_ticket or esta_en_lista)

# NOT: invertimos la condición
bloqueado = False
print("¿Puede ingresar?:", not bloqueado)