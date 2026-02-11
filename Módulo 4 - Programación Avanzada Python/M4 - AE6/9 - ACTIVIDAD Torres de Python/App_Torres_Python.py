import os
import pandas as pd
from datetime import datetime


class GestorGastos:
    def __init__(self):
        # Definimos el nombre del archivo "maestro"
        self.archivo = "gastos.csv"
        # Definimos la carpeta de respaldos
        self.carpeta_respaldos = "respaldos_gastos"

    def inicializar_archivo(self):
        """
        Verifica si el archivo existe. Si no, lo crea con los encabezados.
        Esto es vital para que Pandas entienda las columnas después.
        """
        if not os.path.exists(self.archivo):
            try:
                # Usamos 'w' para crear
                with open(self.archivo, "w") as f:
                    f.write("Departamento,Monto,Descripcion,Fecha\n")
                print(f"🆕 Archivo '{self.archivo}' creado con éxito.")
            except IOError as e:
                print(f"❌ Error al inicializar el archivo: {e}")

    def ingresar_gasto(self, departamento, monto, descripcion):
        """
        Agrega un nuevo gasto al final del archivo (Modo Append).
        Aplica: Context Manager (with) y Manejo de Excepciones.
        """
        # Aseguramos que el archivo tenga cabecera
        self.inicializar_archivo()

        # Obtenemos la fecha actual automática
        fecha = datetime.now().strftime("%Y-%m-%d")

        # Preparamos la línea CSV
        nueva_linea = f"{departamento},{monto},{descripcion},{fecha}\n"

        try:
            # 1. USO DE CONTEXT MANAGER (with open)
            # Modo 'a' (Append) para no borrar lo anterior
            with open(self.archivo, "a") as f:
                f.write(nueva_linea)
            print("✅ Gasto registrado correctamente.")

        except PermissionError:
            print("⚠️ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al escribir: {e}")

    def leer_gastos(self):
        """
        Lee el archivo y muestra el contenido crudo en consola.
        Aplica: try-except para FileNotFoundError.
        """
        print("\n--- 📜 LISTADO DE GASTOS (Lectura Manual) ---")
        try:
            # Modo 'r' (Lectura)
            with open(self.archivo, "r") as f:
                contenido = f.readlines()

                if len(contenido) <= 1:  # Solo tiene cabecera o está vacío
                    print("ℹ️ El archivo está vacío o solo tiene cabecera.")
                else:
                    for linea in contenido:
                        print(linea.strip())  # strip quita el salto de línea doble

        except FileNotFoundError:
            print("⚠️ El archivo de gastos aún no existe. ¡Ingresa el primero!")
        except Exception as e:
            print(f"❌ Error al leer: {e}")

    def generar_reporte_pandas(self):
        """
        Utiliza la librería Pandas para análisis de datos avanzado.
        """
        print("\n--- 🐼 REPORTE ESTADÍSTICO (Pandas) ---")
        if not os.path.exists(self.archivo):
            print("⚠️ No hay datos para analizar.")
            return

        try:
            # Carga automática del CSV a DataFrame
            df = pd.read_csv(self.archivo)

            if df.empty:
                print("ℹ️ El archivo no tiene datos suficientes.")
                return

            # Estadísticas rápidas
            print("📊 Resumen General:")
            print(df.describe())  # Estadísticas de columnas numéricas (Monto)

            print("\n💰 Total Recaudado:")
            print(f"${df['Monto'].sum()}")

            print("\n🏆 Depto con más gastos registrados:")
            # value_counts cuenta la frecuencia de cada depto
            print(df['Departamento'].value_counts().head(3))

        except Exception as e:
            print(f"❌ Error en Pandas: {e}")

    def archivar_mes(self):
        """
        Simula el cierre de mes moviendo el archivo actual a una carpeta de respaldo.
        Aplica: Módulo os (mkdir, rename/move) y Bloque finally.
        """
        print("\n--- 📦 ARCHIVANDO MES ---")

        if not os.path.exists(self.archivo):
            print("⚠️ No hay archivo para respaldar.")
            return

        # Generamos un nombre único para el respaldo (ej: gastos_2023-10-27.csv)
        fecha_hoy = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_respaldo = f"gastos_cierre_{fecha_hoy}.csv"

        # Ruta destino (ej: respaldos_gastos/gastos_cierre_....csv)
        # Usamos os.path.join para que funcione en Windows y Mac
        ruta_destino = os.path.join(self.carpeta_respaldos, nombre_respaldo)

        try:
            # 1. Crear carpeta si no existe
            if not os.path.exists(self.carpeta_respaldos):
                os.mkdir(self.carpeta_respaldos)
                print(f"📁 Carpeta '{self.carpeta_respaldos}' creada.")

            # 2. Mover (Renombrar ruta) el archivo
            os.rename(self.archivo, ruta_destino)
            print(f"✅ Cierre de mes exitoso.")
            print(f"📄 Archivo movido a: {ruta_destino}")

        except OSError as e:
            print(f"❌ Error del sistema al mover archivo: {e}")

        finally:
            # 3. USO DE FINALLY
            # Este bloque se ejecuta sí o sí. Ideal para mensajes de estado final.
            print("🔄 Operación de archivado finalizada (éxito o error).")


# --- BLOQUE PRINCIPAL (Main) ---
def main():
    sistema = GestorGastos()

    while True:
        print("\n🏢 --- SISTEMA 'TORRES DE PYTHON' ---")
        print("1. Ingresar Gasto Común")
        print("2. Ver Listado (Lectura simple)")
        print("3. Reporte Inteligente (Pandas)")
        print("4. Cerrar Mes (Archivar)")
        print("5. Salir")

        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            depto = input("Número de Depto: ")
            try:
                monto = float(input("Monto ($): "))
                desc = input("Descripción (ej. Agua, Luz): ")
                sistema.ingresar_gasto(depto, monto, desc)
            except ValueError:
                print("❌ Error: El monto debe ser un número.")

        elif opcion == "2":
            sistema.leer_gastos()

        elif opcion == "3":
            sistema.generar_reporte_pandas()

        elif opcion == "4":
            confirmar = input("¿Estás seguro de cerrar el mes? El archivo actual se moverá (s/n): ")
            if confirmar.lower() == 's':
                sistema.archivar_mes()

        elif opcion == "5":
            print("¡Hasta luego! 👋")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()