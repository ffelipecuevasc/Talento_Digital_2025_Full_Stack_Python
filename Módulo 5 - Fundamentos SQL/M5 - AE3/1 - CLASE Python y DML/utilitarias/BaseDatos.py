# Este módulo contendrá lo relacionado a la Conexión BD - MySQL
# Importar el controlador (drive) de MySQL, Error y Producto
import mysql.connector
from mysql.connector import Error
from .Producto import Producto

# Crear la Función conectar() para conectarme a MySQl
def conectar():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="Ejercicio_BD",
            port=3306
        )
        print("[MySQL] Conexión Establecida ¡OK!")
    except Error as e:
        print(f"[ERROR] Conexión Fallida a MySQL: {e}")
    return con

# Crear la Función para listar productos = listar_productos()
def listar_productos():
    con = conectar()
    lista_productos = []
    try:
        # sql = STRING
        sql = "SELECT * FROM Productos;"
        cursor = con.cursor(dictionary=True)
        cursor.execute(sql)
        resultado = cursor.fetchall()

        # Recorremos el resultado que contiene todos los registros (filas) de la BD
        for registro in resultado:
            producto = Producto(
                id=registro["ProductoID"],
                nombre=registro["Nombre"],
                categoria=registro["Categoria"],
                marca=registro["Marca"],
                precio=registro["Precio"],
                stock=registro["Stock"],
                descuento=registro["Descuento"],
                peso=registro["Peso"],
                fecha_ingreso=registro["FechaIngreso"]
            )
            lista_productos.append(producto)
    except Error as e:
        print(f"[ERROR] No se pudo listar el contenido de la tabla Productos: {e}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
    return lista_productos

# Crear la Función para registrar un producto = registrar_producto(producto)
def registrar_producto(producto):
    con = conectar()
    try:
        # JAVA - PreparedStatement
        # PYTHON - Consultas SQL Parametrizadas
        # Esta medida es para evitar inyecciones SQL, creando la consulta SQL primero y después pasando los valores
        sql = (f"INSERT INTO Productos (Nombre, Categoria, Marca, Precio, Stock, Descuento, Peso, FechaIngreso)"
               f"VALUES(%s, %s, %s, %s, %s, %s, %s, %s);")
        valores = (
            producto.get_nombre(),
            producto.get_categoria(),
            producto.get_marca(),
            producto.get_precio(),
            producto.get_stock(),
            producto.get_descuento(),
            producto.get_peso(),
            producto.get_fecha_ingreso()
        )
        cursor = con.cursor()

        # Acá pasan 2 cosas:
        # 1) Al ejecutar el metodo execute() esto gatilla en MySQL el comando START TRANSACTION;
        # 2) El string 'sql' (valores parametrizados) es rellenado con valores (tupla 'valores') en el metodo execute()
        cursor.execute(sql, valores)

        # Aplicamos el COMMIT (Principios ACID)
        con.commit()
        print("[MySQL] Producto registrado exitosamente ¡OK!")
    except Error as e:
        con.rollback()
        print(f"[ERROR] No se pudo registrar el producto: {e}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

# Crear la Función para actualizar un producto = actualizar_producto(producto)
def actualizar_producto(producto):
    con = conectar()
    try:
        sql = """
               UPDATE Productos 
               SET Nombre = %s,
               Categoria = %s,
               Marca = %s,
               Precio = %s,
               Stock = %s,
               Descuento = %s,
               Peso = %s,
               FechaIngreso = %s
               WHERE ProductoID = %s;
              """
        valores = (
            producto.get_nombre(),
            producto.get_categoria(),
            producto.get_marca(),
            producto.get_precio(),
            producto.get_stock(),
            producto.get_descuento(),
            producto.get_peso(),
            producto.get_fecha_ingreso(),
            producto.get_id()
        )
        cursor = con.cursor()
        cursor.execute(sql, valores)
        if (cursor.rowcount > 0):
            con.commit()
            print("[MySQL] Producto actualizado exitosamente ¡OK!")
        else:
            print("[MySQL] No se pudo actualizar el producto porque no existe el ID.")
    except Error as e:
        con.rollback()
        print(f"[ERROR] No se pudo actualizar el producto: e")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

# Crear la Función para eliminar un producto = eliminar_producto(id_producto)
def eliminar_producto(id_producto):
    con = conectar()
    try:
        sql = "DELETE FROM Productos WHERE ProductoID = %s;"
        valor = (id_producto,)
        cursor = con.cursor()
        cursor.execute(sql, valor)
        if (cursor.rowcount > 0):
            con.commit()
            print("[MySQL] Producto eliminado exitosamente ¡OK!")
        else:
            print("[MySQL] No se pudo eliminar el producto porque no existe el ID.")
    except Error as e:
        con.rollback()
        print(f"[ERROR] No se pudo eliminar el producto: {e}")
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()