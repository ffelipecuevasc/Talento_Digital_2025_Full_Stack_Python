# 4. La Caja Registradora
# Enfoque: Acumulador dentro de un for.

precios = [100, 250, 400, 50]
total = 0

for precio in precios:
    total += precio # Acumulación: total = total + precio

print(f"El costo total de la compra es: ${total}")