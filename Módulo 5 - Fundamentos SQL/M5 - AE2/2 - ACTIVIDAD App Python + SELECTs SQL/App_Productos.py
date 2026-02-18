# Solucion_Actividad_BD_Pro.py
# -----------------------------------------------------------------------------
# OBJETIVO: Resolver los 15 ejercicios con limpieza de consola (UX mejorada).
# REQUISITO: Configurar PyCharm con "Emulate terminal in output console".
# -----------------------------------------------------------------------------

import mysql.connector
from mysql.connector import Error
import os
import sys

# Configuración de la conexión
CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',  # <--- Ajusta tu contraseña aquí
    'database': 'Ejercicio_BD'
}


def limpiar_consola():
    """
    Detecta el sistema operativo y aplica el comando de limpieza correspondiente.
    Funciona en Windows (cls) y Linux/Mac (clear).
    """
    if os.name == 'nt':  # 'nt' significa Windows
        os.system('cls')
    else:
        os.system('clear')


def esperar_usuario():
    """
    Genera una pausa hasta que el usuario presione Enter.
    """
    print(f"\n{'-' * 60}")
    input("  >> Presiona [ENTER] para continuar al siguiente ejercicio...")


def ejecutar_y_mostrar(cursor, numero, titulo, query):
    """
    Limpia pantalla, ejecuta la consulta y muestra resultados paginados.
    """
    # 1. Limpieza de consola antes de mostrar el ejercicio nuevo
    limpiar_consola()

    print(f"{'=' * 60}")
    print(f" EJERCICIO {numero}: {titulo}")
    print(f"{'=' * 60}")
    print(f"SQL: {query}\n")
    print(f"RESULTADOS:")
    print(f"{'-' * 60}")

    try:
        cursor.execute(query)
        resultados = cursor.fetchall()

        if not resultados:
            print("  [!] No se encontraron resultados.")
        else:
            for fila in resultados:
                print(f"  • {fila}")
            print(f"\n  [Total registros: {len(resultados)}]")

    except Error as e:
        print(f"  [ERROR SQL]: {e}")

    # 2. Pausa para que el alumno pueda leer antes de borrar
    esperar_usuario()


def main():
    conexion = None
    try:
        # Limpieza inicial
        limpiar_consola()
        print("[INICIO] Conectando a MySQL...")

        conexion = mysql.connector.connect(**CONFIG)

        if conexion.is_connected():
            cursor = conexion.cursor()
            print("[EXITO] Conexión establecida. Presiona ENTER para comenzar.")
            input()

            # LISTA DE EJERCICIOS
            # -----------------------------------------------------------------

            # NIVEL 1
            ejecutar_y_mostrar(cursor, 1, "Mayúsculas y Minúsculas (Ropa)",
                               "SELECT UPPER(Nombre), LOWER(Marca) FROM Productos WHERE Categoria = 'Ropa';")

            ejecutar_y_mostrar(cursor, 2, "Largo de Nombres",
                               "SELECT Nombre, LENGTH(Nombre) as Largo FROM Productos ORDER BY Largo DESC;")

            ejecutar_y_mostrar(cursor, 3, "Precios con IVA (ROUND)",
                               "SELECT Nombre, Precio, ROUND(Precio * 1.19, 2) as Precio_IVA FROM Productos;")

            ejecutar_y_mostrar(cursor, 4, "Marcas Cortas",
                               "SELECT * FROM Productos WHERE LENGTH(Marca) < 5;")

            # NIVEL 2
            ejecutar_y_mostrar(cursor, 5, "Top 5 Más Caros",
                               "SELECT Nombre, Categoria, Precio FROM Productos ORDER BY Precio DESC LIMIT 5;")

            ejecutar_y_mostrar(cursor, 6, "Liquidación Electrónica",
                               "SELECT * FROM Productos WHERE Categoria = 'Electrónica' AND Stock < 50 AND Descuento > 10;")

            ejecutar_y_mostrar(cursor, 7, "Pesos Pesados (> 2kg)",
                               "SELECT * FROM Productos WHERE Peso > 2.00 ORDER BY Peso DESC;")

            ejecutar_y_mostrar(cursor, 8, "Buscador 'Laptop' (Insensible a mayúsculas)",
                               "SELECT * FROM Productos WHERE LOWER(Nombre) LIKE '%laptop%';")

            # NIVEL 3
            ejecutar_y_mostrar(cursor, 9, "Conteo de Libros",
                               "SELECT COUNT(*) as Total_Libros FROM Productos WHERE Categoria = 'Libros';")

            ejecutar_y_mostrar(cursor, 10, "Valor Total del Inventario",
                               "SELECT SUM(Precio * Stock) as Valor_Total FROM Productos;")

            ejecutar_y_mostrar(cursor, 11, "Promedio Precio Salud y Belleza",
                               "SELECT ROUND(AVG(Precio), 2) as Promedio FROM Productos WHERE Categoria = 'Salud y Belleza';")

            ejecutar_y_mostrar(cursor, 12, "Rango de Precios Hogar (Min/Max)",
                               "SELECT MIN(Precio), MAX(Precio) FROM Productos WHERE Categoria = 'Hogar';")

            # NIVEL 4
            ejecutar_y_mostrar(cursor, 13, "Eficiencia: Valor por Kilo (Deportes)",
                               "SELECT Nombre, Precio, Peso, (Precio / Peso) as Valor_Kilo FROM Productos WHERE Categoria = 'Deportes' ORDER BY Valor_Kilo DESC LIMIT 10;")

            ejecutar_y_mostrar(cursor, 14, "Dinero total en Descuentos (Juguetes)",
                               "SELECT ROUND(SUM((Precio * Descuento / 100) * Stock), 2) FROM Productos WHERE Categoria = 'Juguetes';")

            ejecutar_y_mostrar(cursor, 15, "El Rey del Stock (Reporte de texto)",
                               "SELECT CONCAT('Producto: ', Nombre, ' | Unidades: ', Stock) FROM Productos ORDER BY Stock DESC LIMIT 1;")

    except Error as e:
        print(f"\n[ERROR CRÍTICO]: {e}")

    finally:
        if conexion is not None and conexion.is_connected():
            cursor.close()
            conexion.close()
            limpiar_consola()
            print("\n" + "=" * 50)
            print(" ¡FELICIDADES! HAS COMPLETADO TODOS LOS EJERCICIOS.")
            print("=" * 50 + "\n")
            sys.exit()  # Cerramos el script limpiamente


if __name__ == "__main__":
    main()