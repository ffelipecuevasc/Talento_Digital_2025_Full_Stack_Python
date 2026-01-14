import time
import os
import sys

# --- 1. ZONA GLOBAL (La Memoria del Día) ---
# Esta variable vive fuera de todas las funciones.
pacientes_atendidos_hoy = 0


# --- 2. ZONA DE HERRAMIENTAS (Utils) ---

def limpiar_pantalla():
    """
    Limpia la consola.
    Optimizado para Windows 10.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausar():
    """Pausa para leer mensajes."""
    input("\n[Presione ENTER para continuar]")


# --- 3. ZONA DE LÓGICA PURA (El Cerebro - No imprimen, solo retornan) ---

def calcular_prioridad(edad):
    """
    Recibe una edad (int) y RETORNA el nivel de prioridad.
    NO imprime nada (uso estricto de return).
    """
    if edad >= 60 or edad <= 5:
        return "ALTA"  #
    else:
        return "MEDIA"


def validar_rut(rut):
    """
    Usa len() para validar el largo del RUT.
    Retorna True si es válido, False si no.
    """
    #
    largo = len(rut)
    if largo >= 8:
        return True
    else:
        return False


# --- 4. ZONA DE PROCEDIMIENTOS (Interacción con Usuario) ---

def solicitar_hora_medica():
    """
    Integra la lógica de prioridad, validaciones y contador global.
    """
    # Importamos la variable global para poder modificarla
    global pacientes_atendidos_hoy

    print("\n--- 📅 SOLICITUD DE HORA MÉDICA ---")

    # Validación de Edad con int()
    try:
        entrada_edad = input("Ingrese la edad del paciente: ")
        edad_paciente = int(entrada_edad)  # Convierte str a int
    except ValueError:
        print("❌ ERROR: Debe ingresar un número válido para la edad.")
        pausar()
        return  # Salimos de la función si hay error

    print("Calculando prioridad...")
    time.sleep(1)

    # LLAMADA A LA FUNCIÓN CON RETURN (El dato viaja de vuelta)
    nivel_prioridad = calcular_prioridad(edad_paciente)

    print("✅ Hora Agendada.")
    print(f"   Paciente: {edad_paciente} años")
    # Usamos el dato retornado
    print(f"   PRIORIDAD ASIGNADA: {nivel_prioridad}")
    print("   Box: 4")

    # Aumentamos el contador global
    pacientes_atendidos_hoy += 1
    pausar()


def urgencia_dental():
    """Versión simplificada para Fase 2."""
    global pacientes_atendidos_hoy
    print("\n--- 🦷 URGENCIA DENTAL ---")
    print("Derivando a evaluación...")
    time.sleep(1)
    print("✅ Ticket D-002 generado.")

    pacientes_atendidos_hoy += 1
    pausar()


def retirar_leche_o_alimentos():
    """
    Implementa validación de largo de RUT.
    """
    global pacientes_atendidos_hoy
    print("\n--- 🍼 RETIRO PNAC ---")

    rut_ingresado = input("Ingrese RUT (sin puntos ni guión): ")

    # Usamos la función de validación (Return True/False)
    es_valido = validar_rut(rut_ingresado)

    if es_valido:
        print("🔎 RUT válido. Consultando beneficios...")
        time.sleep(1)
        print("✅ Entrega autorizada: 2kg Leche.")
        pacientes_atendidos_hoy += 1
    else:
        print("❌ ERROR: El RUT ingresado es muy corto.")
        print("   (Validación fallida por len() < 8)")

    pausar()


def salir_del_sistema():
    """
    Muestra el reporte final antes de cerrar.
    """
    print("\n👋 Cerrando sistema...")
    print("=" * 30)
    # Reporte Final con la variable global
    print(f"📊 REPORTE DE CIERRE")
    print(f"   Total de pacientes atendidos hoy: {pacientes_atendidos_hoy}")
    print("=" * 30)
    time.sleep(2)
    sys.exit()


# --- 5. MENÚ PRINCIPAL (Diccionario de Despacho) ---

def mostrar_menu():
    limpiar_pantalla()
    print("=" * 40)
    print("   🏥  CESFAM INTELIGENTE v2.0  🏥")
    print(f"   (Pacientes hoy: {pacientes_atendidos_hoy})")  # Visualización en tiempo real
    print("=" * 40)
    print(" [1] 📅  Solicitar Hora (Con Prioridad)")
    print(" [2] 🦷  Urgencia Dental")
    print(" [3] 🍼  Retirar Alimentos (Validar RUT)")
    print(" [4] ❌  Cerrar y Ver Reporte")
    print("=" * 40)


def iniciar_totem():
    # Diccionario de opciones
    menu_opciones = {
        "1": solicitar_hora_medica,
        "2": urgencia_dental,
        "3": retirar_leche_o_alimentos,
        "4": salir_del_sistema
    }

    while True:
        mostrar_menu()
        opcion = input(">> Seleccione opción: ")

        if opcion in menu_opciones:
            funcion = menu_opciones[opcion]
            funcion()
        else:
            print("🚫 Opción no válida.")
            time.sleep(1)


if __name__ == "__main__":
    iniciar_totem()