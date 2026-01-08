# --- RESOLUCIÓN DEMO: BASE DE DATOS DE PRODUCTOS (Pag. 20) ---

# 1. Crear un diccionario productos donde cada clave sea un ID
# 2. Cada valor será un diccionario con: nombre, precio, stock
productos = {
    "P001": {"nombre": "Teclado", "precio": 5000, "stock": 10},
    "P002": {"nombre": "Mouse", "precio": 2500, "stock": 50},
    "P003": {"nombre": "Monitor", "precio": 150000, "stock": 5}
}
print("1-2. Base de datos inicial creada.")

# 3. Acceder a los datos de un producto por su ID
# Queremos ver el nombre del producto P001
producto_consultado = productos["P001"]["nombre"]
print(f"3. Consulta P001: {producto_consultado}")

# 4. Agregar un nuevo producto al diccionario
productos["P004"] = {"nombre": "Webcam", "precio": 12000, "stock": 8}
print(f"4. Producto agregado: {productos['P004']}")

# 5. Modificar el stock de un producto existente
# El Mouse (P002) vendió unidades, bajamos el stock
productos["P002"]["stock"] = 45
print(f"5. Stock de Mouse actualizado: {productos['P002']['stock']}")

# 6. Eliminar un producto usando pop()
# Eliminamos el Monitor (P003) y guardamos su info por si acaso
eliminado = productos.pop("P003")
print(f"6. Producto eliminado: {eliminado['nombre']}")

# 7. Iterar sobre todos los productos mostrando formato amigable
print("\n--- 7. Reporte de Inventario ---")
for id_prod, info in productos.items():
    # info es el diccionario interno (nombre, precio, stock)
    print(f"Producto: {info['nombre']} | Precio: ${info['precio']} | Stock: {info['stock']}")

# 8. Bonus: Mostrar solo los productos con stock menor a 10
print("\n--- 8. Alerta de Stock Bajo (< 10) ---")
for id_prod, info in productos.items():
    if info["stock"] < 10:
        print(f"¡ALERTA! Quedan pocos {info['nombre']} (Stock: {info['stock']})")