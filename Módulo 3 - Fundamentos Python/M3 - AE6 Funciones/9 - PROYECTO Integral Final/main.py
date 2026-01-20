import os
import time
import gestion_alumnos
import analisis_academico
import reportes_avanzados

# --- ESTADO GLOBAL ---
db_alumnos = []

# --- UTILIDADES ---
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pausar_sistema():
    input("\nPresione [ENTER] para volver al menú principal...")

def mostrar_opciones_menu():
    print("\n=== S.I.G.E.M. 5.0 (Versión Final Agenda) ===")
    print("1. [CRUD] Inscribir Alumno")
    print("2. [CRUD] Ver Nómina Completa")
    print("3. [CRUD] Modificar Nota Específica")
    print("4. [CRUD] Eliminar Alumno")
    print("5. [Estadísticas] Dashboard del Curso")
    print("6. [Estadísticas] Reporte de Aprobados/Reprobados")
    print("7. [Avanzado] Generar Boletines Masivos (Yield)")
    print("8. Salir")

# --- WRAPPERS ---
def op_crear_alumno():
    nuevo = gestion_alumnos.crear_alumno()
    db_alumnos.append(nuevo)
    print("¡Alumno inscrito correctamente!")

def op_leer_alumnos():
    gestion_alumnos.leer_alumnos(db_alumnos)

def op_actualizar_nota():
    gestion_alumnos.actualizar_alumno(db_alumnos)

def op_eliminar_alumno():
    gestion_alumnos.eliminar_alumno(db_alumnos)

def op_dashboard():
    print("\n--- Dashboard Estadístico ---")
    stats = analisis_academico.calcular_estadisticas_curso(db_alumnos)
    if stats:
        print(f"Alumnos Totales: {stats['total_alumnos']}")
        print(f"Promedio del Curso: {stats['promedio_curso']}")
        print(f"Mejor Promedio: {stats['mejor_promedio']}")
        print(f"Tasa Aprobación: {stats['cantidad_aprobados']} aprobados vs {stats['cantidad_reprobados']} reprobados")
    else:
        print("No hay datos para calcular estadísticas.")

def op_ver_situacion():
    print("\n--- Listados de Situación Final ---")
    print("[A] Ver Aprobados")
    print("[R] Ver Reprobados")
    sub_op = input("Elija lista: ").upper()

    if sub_op == 'A':
        lista = analisis_academico.filtrar_aprobados(db_alumnos)
        estado = "APROBADOS"
    else:
        lista = analisis_academico.filtrar_reprobados(db_alumnos)
        estado = "REPROBADOS"

    if not lista:
        print(f"No hay alumnos {estado}.")
    else:
        print(f"\n--- ALUMNOS {estado} ---")
        for a in lista:
            print(f"{a['nombre']} -> Promedio Final: {a['promedio_final']}")

def op_boletines():
    print("\n--- Impresión de Boletines ---")
    if not db_alumnos:
        print("No hay alumnos para generar boletines.")
        return
    generador = reportes_avanzados.generador_informe(db_alumnos)
    print("Procesando documentos...")
    try:
        while True:
            time.sleep(0.5)
            boletin = next(generador)
            print(f"[IMPRIMIENDO] {boletin}")
    except StopIteration:
        print("--- Fin de la generación de documentos ---")

def op_salir():
    print("Guardando datos y cerrando sistema...")
    time.sleep(1)
    exit()

# --- DICCIONARIO DE DESPACHO ---
ACCIONES_SISTEMA = {
    "1": op_crear_alumno,
    "2": op_leer_alumnos,
    "3": op_actualizar_nota,
    "4": op_eliminar_alumno,
    "5": op_dashboard,
    "6": op_ver_situacion,
    "7": op_boletines,
    "8": op_salir
}

# --- BUCLE PRINCIPAL ---
def iniciar_sistema():
    while True:
        limpiar_pantalla()
        mostrar_opciones_menu()

        opcion = input("\nSeleccione opción: ")
        funcion_seleccionada = ACCIONES_SISTEMA.get(opcion)

        if funcion_seleccionada:
            funcion_seleccionada()
            pausar_sistema()
        else:
            print("ERROR: Opción no válida. Intente nuevamente.")
            time.sleep(1)

if __name__ == "__main__":
    iniciar_sistema()