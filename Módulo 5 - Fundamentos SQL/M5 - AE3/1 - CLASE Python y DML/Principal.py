# Módulo para ejecutar la App
import sys
from utilitarias.Producto import Producto
from utilitarias.BaseDatos import listar_productos, registrar_producto, actualizar_producto, eliminar_producto

# Implementar las funciones necesarias para la interfaz del usuario
# CRUD de Productos
def listar_productos_menu():
    print(f"--- LISTADO DE PRODUCTOS ---")
    productos = listar_productos()
    if not productos:
        print("[CRUD] No hay productos para listar.")
    else:
        for p in productos:
            print(p)

def registrar_producto_bd():
    print(f"--- REGISTRO DE PRODUCTOS ---")
    try:
        n = input("Ingrese el nombre del producto: ")
        c = input("Ingrese la categoría del producto: ")
        m = input("Ingrese la marca del producto: ")
        p = float(input("Ingrese el precio del producto: "))
        s = int(input("Ingrese el stock del producto: "))
        d = float(input("Ingrese el descuento (%) del producto: "))
        pe = float(input("Ingrese el peso del producto: "))
        fi = input("Ingrese la fecha de ingreso del producto (1990-12-29): ")

        # Crear el objeto Producto
        nuevo_producto = Producto(None, n, c, m, p, s, d, pe, fi)

        # Registrar el producto
        registrar_producto(nuevo_producto)
    except ValueError:
        print("[ERROR] Los tipos de valores ingresados no corresponden al tipo de valor en la BD MySQL.")

def actualizar_producto_bd():
    print(f"--- ACTUALIZACIÓN DE PRODUCTOS ---")
    try:
        id = int(input("Ingrese el ID del producto a actualizar: "))
        n = input("Ingrese el nombre del producto: ")
        c = input("Ingrese la categoría del producto: ")
        m = input("Ingrese la marca del producto: ")
        p = float(input("Ingrese el precio del producto: "))
        s = int(input("Ingrese el stock del producto: "))
        d = float(input("Ingrese el descuento (%) del producto: "))
        pe = float(input("Ingrese el peso del producto: "))
        fi = input("Ingrese la fecha de ingreso del producto (1990-12-29): ")

        # Crear el objeto Producto
        producto_actualizado = Producto(id, n, c, m, p, s, d, pe, fi)

        # Actualizar el producto
        actualizar_producto(producto_actualizado)
    except ValueError:
        print("[ERROR] Los tipos de valores ingresados no corresponden al tipo de valor en la BD MySQL.")

def eliminar_producto_bd():
    print(f"--- ELIMINACIÓN DE PRODUCTOS ---")
    try:
        id_prod = int(input("Ingrese el ID del producto a eliminar: "))
        confirmar = input(f"¿Estás seguro de eliminar el producto con ID '{id_prod}' (s/n)? ")
        if confirmar.lower() == "s":
            eliminar_producto(id_prod)
        else:
            print("[CRUD] Eliminación cancelada por el usuario.")
    except ValueError:
        print("[ERROR] Los tipos de valores ingresados no corresponden al tipo de valor en la BD MySQL.")

# Funciones del menú
def salir():
    print("[APP] Saliendo de la aplicación Sistema de Inventario. Hasta luego...")
    sys.exit()

def mostrar_menu():
    # Imprime el menú
    print("----------------------------------")
    print("--- MENÚ DE INVENTARIO + MYSQL ---")
    print("1. Listar productos.")
    print("2. Registrar un nuevo producto.")
    print("3. Actualizar un producto.")
    print("4. Eliminar un producto.")
    print("5. Salir.")
    print("----------------------------------")

def app_principal():
    # Crear el diccionario con las opciones
    opciones = {
        "1": listar_productos_menu,
        "2": registrar_producto_bd,
        "3": actualizar_producto_bd,
        "4": eliminar_producto_bd,
        "5": salir
    }

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        opcion_escogida = opciones.get(opcion)
        if opcion_escogida:
            opcion_escogida()
        else:
            print("[ERROR] Opción inválida, debe escoger 1 de las 5 opciones del menú.")

if __name__ == "__main__":
    app_principal()