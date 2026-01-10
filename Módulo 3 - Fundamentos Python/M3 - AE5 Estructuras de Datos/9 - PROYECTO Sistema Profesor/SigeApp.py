# ==============================================================================
# PROYECTO: EL PROFESOR 2.0 (LIBRO DE CLASES DIGITAL)
# AUTOR: Equipo de Desarrollo Hackathon (Tú y tus alumnos)
# OBJETIVO: Gestionar notas y asistencia usando Estructuras de Datos Avanzadas
# ==============================================================================

# 1. IMPORTACIONES
# 'csv' nos permite crear archivos de Excel simples para el requerimiento de innovación.
import csv
# 'defaultdict' ayuda a crear diccionarios que no dan error si la clave no existe.
# 'Counter' es una herramienta experta en contar elementos de una lista rápidamente.
from collections import defaultdict, Counter

# ==============================================================================
# 2. INICIALIZACIÓN DE VARIABLES Y ESTRUCTURAS DE DATOS
# ==============================================================================

# DICCIONARIO ANIDADO PRINCIPAL (Aquí vivirá toda la información)
# Estructura visual: { "1111-1": { "nombre": "Juan", "notas": [5.5, 6.0], ... } }
libro_clases = {}

# SET (CONJUNTO): Almacena asignaturas únicas. Los sets no permiten duplicados.
asignaturas_curso = {"Matemáticas", "Lenguaje", "Historia", "Ciencias"}

# Variable de control para el ciclo infinito del menú
sistema_encendido = True

print("🎓 BIENVENIDO AL SISTEMA DE GESTIÓN ESCOLAR: SIGEAPP v1.0 🎓")
print(f"Asignaturas activas del sistema: {asignaturas_curso}")

# ==============================================================================
# 3. CICLO PRINCIPAL (LOOP INFINITO)
# ==============================================================================
while sistema_encendido:
    # Decoración visual para separar operaciones en la consola
    print("\n" + "="*50)
    print("📌 MENÚ PRINCIPAL DEL PROFESOR")
    print("="*50)
    print("1. 📝 Matricular Alumno Nuevo")
    print("2. 💯 Registrar Notas")
    print("3. ⚠️ Libro de Vida (Anotaciones)")
    print("4. 📊 Reporte de Rendimiento (Estadísticas)")
    print("5. 💾 Exportar Alerta de Reprobados (CSV) [INNOVACIÓN]")
    print("6. 🚪 Salir del Sistema")
    print("="*50)

    # Capturamos la opción del usuario
    opcion = input("👉 Ingrese el número de su opción: ")

    # ==========================================================================
    # 4. ESTRUCTURA DE DECISIÓN (MATCH - CASE) - Requiere Python 3.10+
    # ==========================================================================
    match opcion:

        # CASO 1: MATRICULAR ALUMNO
        case "1":
            print("\n--- 📝 MATRICULA DE ALUMNO ---")
            rut_input = input("Ingrese RUT del alumno (ej: 12345678-9): ")

            # Validación: No podemos tener dos alumnos con el mismo RUT (Clave única)
            if rut_input in libro_clases:
                print(f"❌ ERROR: El RUT {rut_input} ya existe en el sistema.")
            else:
                nombre_input = input("Ingrese Nombre completo: ")

                # AQUÍ OCURRE LA MAGIA DE LOS DICCIONARIOS ANIDADOS
                # Creamos la ficha completa del alumno dentro del diccionario principal.
                # Usamos defaultdict(list) para las anotaciones: si agregamos una categoría nueva,
                # se crea sola como una lista vacía. ¡Súper útil!
                libro_clases[rut_input] = {
                    "nombre": nombre_input,
                    "notas": [],             # Lista para guardar floats
                    "asistencia": 0,         # Entero simple
                    "anotaciones": defaultdict(list)  # Diccionario inteligente
                }
                print(f"✅ ¡Alumno {nombre_input} matriculado con éxito!")

        # CASO 2: REGISTRAR NOTAS
        case "2":
            print("\n--- 💯 INGRESO DE CALIFICACIONES ---")
            rut_busqueda = input("Ingrese RUT del alumno a calificar: ")

            # Verificamos si el alumno existe antes de intentar ponerle nota
            if rut_busqueda in libro_clases:
                # Mostramos el nombre para confirmar que es el alumno correcto
                nombre_actual = libro_clases[rut_busqueda]["nombre"]
                print(f"Alumno seleccionado: {nombre_actual}")

                try:
                    # Solicitamos la nota y la convertimos a decimal (float)
                    nueva_nota = float(input("Ingrese la nota (1.0 a 7.0): "))

                    # Validación de rango chileno (1.0 a 7.0)
                    if 1.0 <= nueva_nota <= 7.0:
                        # Accedemos al diccionario -> clave RUT -> clave 'notas' -> .append()
                        libro_clases[rut_busqueda]["notas"].append(nueva_nota)
                        print(f"✅ Nota {nueva_nota} agregada correctamente.")
                    else:
                        print("❌ ERROR: La nota debe estar entre 1.0 y 7.0")
                except ValueError:
                    # Si el usuario escribe "cinco" en vez de 5.0, el programa no se cae
                    print("❌ ERROR: Debe ingresar un valor numérico (ej: 5.5)")
            else:
                print("❌ ERROR: Alumno no encontrado.")

        # CASO 3: LIBRO DE VIDA (ANOTACIONES)
        case "3":
            print("\n--- ⚠️ REGISTRO DE ANOTACIONES ---")
            rut_anotacion = input("Ingrese RUT del alumno: ")

            if rut_anotacion in libro_clases:
                tipo = input("Tipo de anotación (POSITIVA / NEGATIVA): ").upper()
                detalle = input("Describa el hecho: ")

                # Gracias al defaultdict, no necesitamos preguntar "if tipo in anotaciones".
                # Simplemente agregamos y Python crea la lista si es la primera vez.
                libro_clases[rut_anotacion]["anotaciones"][tipo].append(detalle)
                print("✅ Anotación registrada en el Libro de Vida.")
            else:
                print("❌ ERROR: Alumno no encontrado.")

        # CASO 4: REPORTE Y ESTADÍSTICAS (Uso de Counter)
        case "4":
            print("\n--- 📊 ESTADÍSTICAS DEL CURSO ---")

            # Si no hay alumnos, avisamos para no dividir por cero
            if not libro_clases:
                print("📭 El curso está vacío.")
            else:
                estados_curso = [] # Lista temporal para usar con Counter

                print(f"{'NOMBRE':<20} | {'PROMEDIO':<10} | {'SITUACIÓN'}")
                print("-" * 45)

                # Iteramos sobre items() para obtener clave (rut) y valor (datos) al mismo tiempo
                for rut, datos in libro_clases.items():
                    lista_notas = datos["notas"]

                    # Cálculo de promedio simple
                    if len(lista_notas) > 0:
                        promedio = sum(lista_notas) / len(lista_notas)
                    else:
                        promedio = 1.0 # Si no tiene notas, asumimos la mínima

                    # Lógica de negocio: Aprobado vs Reprobado
                    if promedio >= 4.0:
                        situacion = "APROBADO"
                        estados_curso.append("Aprobados") # Guardamos para el Counter
                    else:
                        situacion = "REPROBADO"
                        estados_curso.append("Reprobados") # Guardamos para el Counter

                    # Imprimimos la fila con formato bonito (.1f es un decimal)
                    print(f"{datos['nombre']:<20} | {promedio:<10.1f} | {situacion}")

                # USO DE COUNTER: Cuenta automáticamente cuántos aprobaron y reprobaron
                resumen = Counter(estados_curso)
                print("\n📈 RESUMEN FINAL:")
                print(f"🔵 Total Aprobados: {resumen['Aprobados']}")
                print(f"🔴 Total Reprobados: {resumen['Reprobados']}")

        # CASO 5: INNOVACIÓN - EXPORTAR ARCHIVO CSV
        case "5":
            print("\n--- 💾 EXPORTANDO ALERTA DE REPROBADOS ---")
            # Nombre del archivo que se creará en la carpeta del proyecto
            nombre_archivo = "alerta_reprobados.csv"

            try:
                # Abrimos (o creamos) el archivo en modo escritura ('w')
                # newline='' evita líneas en blanco extra en Windows
                with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
                    writer = csv.writer(archivo)

                    # Escribimos los encabezados de las columnas
                    writer.writerow(["RUT", "NOMBRE", "PROMEDIO", "SITUACION"])
                    contador_exportados = 0

                    # Recorremos el diccionario buscando reprobados
                    for rut, datos in libro_clases.items():
                        notas = datos["notas"]
                        if len(notas) > 0:
                            promedio = sum(notas) / len(notas)
                        else:
                            promedio = 1.0

                        # Si el promedio es rojo (menor a 4.0), lo guardamos en el archivo
                        if promedio < 4.0:
                            writer.writerow([rut, datos["nombre"], round(promedio, 1), "EN PELIGRO"])
                            contador_exportados += 1

                print(f"✅ Archivo '{nombre_archivo}' generado exitosamente.")
                print(f"📋 Se exportaron {contador_exportados} alumnos en riesgo.")

            except Exception as e:
                # Capturamos cualquier error de archivos (permisos, disco lleno, etc.)
                print(f"❌ Error al generar el archivo: {e}")

        # CASO 6: SALIR
        case "6":
            print("\n👋 ¡Hasta luego Profesor! Cerrando sesión...")
            sistema_encendido = False # Esto rompe el ciclo while y termina el programa

        # CASO POR DEFECTO (Opción inválida)
        case _:
            print("\n❌ OPCIÓN NO VÁLIDA. Por favor intente nuevamente.")