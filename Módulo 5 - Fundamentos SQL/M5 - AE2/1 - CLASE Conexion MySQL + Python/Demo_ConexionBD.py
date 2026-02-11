import mysql.connector  # 1. Importamos al "Traductor"
from mysql.connector import Error  # Importamos los tipos de errores para ser específicos


def probar_conexion():
    connection = None  # Inicializamos la variable vacía

    try:
        # 2. Intentamos "marcar el número"
        print("⏳ Intentando conectar a la Base de Datos en Docker...")

        connection = mysql.connector.connect(
            host='localhost',  # Como usamos Docker con -p 3306:3306, es localhost
            user='root',  # El usuario por defecto
            password='secreto',  # La contraseña que definimos en el comando Docker
            database='sys'  # 'sys' es una BD que ya viene creada por defecto en MySQL
        )

        if connection.is_connected():
            # 3. ¡Si llegamos aquí, contestaron el teléfono!
            db_info = connection.get_server_info()
            print(f"✅ ¡ÉXITO! Conexión establecida con MySQL versión {db_info}")
            print("🚀 Estamos listos para enviar consultas SQL.")

    except Error as e:
        # 4. Si algo falla (contraseña mal, docker apagado), caemos aquí
        print(f"❌ ERROR CRÍTICO: No se pudo conectar.")
        print(f"Detalle del error: {e}")

    finally:
        # 5. Buenas costumbres: Colgar el teléfono al terminar
        if connection is not None and connection.is_connected():
            connection.close()
            print("🔒 Conexión cerrada correctamente.")


# Ejecutamos la función
if __name__ == "__main__":
    probar_conexion()