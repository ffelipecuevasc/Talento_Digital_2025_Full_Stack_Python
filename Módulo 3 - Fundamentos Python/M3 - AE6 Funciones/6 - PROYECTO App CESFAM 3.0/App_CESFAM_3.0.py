import time
import os
import sys

# --- 1. ZONA DE DATOS (Memoria Volátil) ---
# Usaremos una lista de diccionarios para guardar a los pacientes en espera.
cola_de_espera = []


# --- 2. ZONA DE HERRAMIENTAS (Utils) ---

def limpiar_pantalla():
    """
    Limpia la consola. Optimizado para Windows 10 (nt).
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausar():
    input("\n[Presione ENTER para continuar]")


# --- 3. ZONA DE LÓGICA (Roles: Optimizador y Hechicero) ---

# ROL: El Optimizador de Ingresos
# Implementación de PARÁMETROS POR DEFECTO para escribir menos.
def registrar_paciente(nombre, gravedad, prevision="FONASA", nacionalidad="Chilena"):
    """
    Registra un paciente en la cola.
    Si no se especifica previsión ni nacionalidad, asume los valores por defecto.
    """
    nuevo_paciente = {
        "nombre": nombre,
        "gravedad": gravedad,
        "prevision": prevision,
        "nacionalidad": nacionalidad
    }
    cola_de_espera.append(nuevo_paciente)
    print(f"✅ Paciente {nombre} registrado exitosamente.")
    print(f"   Datos: {prevision} | {nacionalidad} | Gravedad: {gravedad}")


# ROL: El Hechicero de las Lambdas
# Implementación de FUNCIÓN ANÓNIMA para ordenar.
def ordenar_lista_espera():
    """
    Ordena la lista de pacientes según su gravedad (de mayor a menor)
    usando una expresión LAMBDA.
    """
    print("⚡ Ordenando lista por gravedad clínica...")
    time.sleep(1)

    # --- AQUÍ USAMOS UNA LAMBDA PARA ORDENAR ---
    # La lambda extrae el valor de la clave 'gravedad' de cada paciente.
    # reverse=True hace que las gravedades altas (ej: 10) queden primero.
    cola_de_espera.sort(key=lambda paciente: paciente['gravedad'], reverse=True)  #

    print("✅ ¡Lista reordenada por prioridad!")
    pausar()


def mostrar_lista_pacientes():
    """Muestra la cola actual para verificar el orden."""
    print("\n--- 📋 LISTA DE ESPERA ACTUAL ---")
    if not cola_de_espera:
        print("(No hay pacientes en espera)")
    else:
        print(f"{'NOMBRE':<15} | {'GRAVEDAD':<10} | {'PREVISIÓN':<10}")
        print("-" * 40)
        for p in cola_de_espera:
            print(f"{p['nombre']:<15} | {p['gravedad']:<10} | {p['prevision']:<10}")
    pausar()


# --- 4. ZONA DE INTERACCIÓN (Rol: Integrador Flexible) ---

def interfaz_registro_rapido():
    """
    Simula el uso de los valores por defecto.
    Solo pedimos Nombre y Gravedad. El resto lo pone Python solo.
    """
    print("\n--- ⚡ REGISTRO RÁPIDO (Optimizador) ---")
    nombre = input("Nombre del paciente: ")
    try:
        gravedad = int(input("Nivel de Gravedad (1-10): "))
    except ValueError:
        print("❌ Error: La gravedad debe ser un número.")
        pausar()
        return

    # Llamada simple: Aprovechamos los Defaults definidos en la función
    registrar_paciente(nombre, gravedad)
    pausar()


def interfaz_registro_detallado():
    """
    Simula el uso de ARGUMENTOS NOMINALES (Keyword Arguments).
    Ideal para casos especiales (Extranjeros o ISAPRE).
    """
    print("\n--- 📝 REGISTRO DETALLADO (Integrador) ---")
    nom = input("Nombre: ")
    grav = int(input("Gravedad: "))
    nac = input("Nacionalidad: ")
    prev = input("Previsión: ")

    print("\nRegistrando con Argumentos Nominales...")
    time.sleep(1)

    # Llamada flexible: Usamos clave=valor.
    # ¡Podríamos cambiar el orden y funcionaría igual!
    registrar_paciente(nombre=nom, gravedad=grav, nacionalidad=nac, prevision=prev)  #
    pausar()


def salir_sistema():
    print("\n👋 Cerrando sistema CESFAM 3.0...")
    time.sleep(1)
    sys.exit()


# --- 5. EL CEREBRO DEL MENÚ (Diccionario) ---

def mostrar_menu():
    limpiar_pantalla()
    print("=" * 45)
    print("   🏥  CESFAM 3.0 - GESTIÓN EFICIENTE  🏥")
    print("=" * 45)
    print(" [1] ⚡ Registro Rápido (Usa Defaults: FONASA/Chilena)")
    print(" [2] 📝 Registro Manual (Usa Argumentos Nominales)")
    print(" [3] 👀 Ver Lista de Espera")
    print(" [4] 🧙‍♂️ Ordenar Lista Mágicamente (Lambda)")
    print(" [5] ❌ Salir")
    print("=" * 45)


def iniciar_aplicacion():
    # DICCIONARIO DE DESPACHO
    # Mapeamos la opción (str) a la función (objeto)
    acciones = {
        "1": interfaz_registro_rapido,
        "2": interfaz_registro_detallado,
        "3": mostrar_lista_pacientes,
        "4": ordenar_lista_espera,
        "5": salir_sistema
    }

    while True:
        mostrar_menu()
        opcion = input(">> Seleccione opción: ")

        if opcion in acciones:
            # Recuperamos la función del diccionario y la ejecutamos ()
            funcion_seleccionada = acciones[opcion]
            funcion_seleccionada()
        else:
            print("🚫 Opción no válida.")
            time.sleep(1)


if __name__ == "__main__":
    # Precarga de datos para probar el ordenamiento (Lambda) rápidamente
    cola_de_espera.append({"nombre": "Paciente A", "gravedad": 2, "prevision": "FONASA", "nacionalidad": "Chilena"})
    cola_de_espera.append({"nombre": "Paciente B", "gravedad": 9, "prevision": "ISAPRE", "nacionalidad": "Chilena"})
    cola_de_espera.append({"nombre": "Paciente C", "gravedad": 5, "prevision": "FONASA", "nacionalidad": "Peruana"})

    iniciar_aplicacion()