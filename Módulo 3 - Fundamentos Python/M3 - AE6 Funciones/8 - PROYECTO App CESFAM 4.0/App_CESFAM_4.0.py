import time
import os
import sys

# --- 1. ZONA GLOBAL DE DATOS ---

# Diccionario para el rastreo (Base de Datos de Contagios)
# Clave: Contagiado -> Valor: Quién lo contagió
cadena_contagios = {
    "Laura": "Carlos",
    "Carlos": "Ana",
    "Ana": "Pedro",
    "Pedro": "Paciente Cero"  #
}


# --- 2. ZONA DE HERRAMIENTAS (Utils) ---

def limpiar_pantalla():
    """
    Limpia la consola. Optimizado para Windows 10.
    En PyCharm: Requiere 'Emulate terminal in output console'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausar():
    input("\n[Presione ENTER para continuar]")


# --- 3. MÓDULO DE RENDIMIENTO (Rol: Ingeniero Yield) ---

def generador_tickets_vacuna():
    """
    GENERADOR con YIELD.
    Crea tickets de vacunación infinitos sin ocupar memoria RAM.
    Lazy Evaluation: Solo entrega el siguiente cuando se pide.
    """
    numero = 1
    while True:
        ticket = f"VAC-{numero:03d}"  # Formato VAC-001, VAC-002...
        # # Aquí usamos yield para ahorrar memoria
        yield ticket
        numero += 1


# Instanciamos el generador GLOBALMENTE para que no se resetee el conteo
maquina_vacunacion = generador_tickets_vacuna()


# --- 4. MÓDULO DE INTELIGENCIA (Rol: Detective Recursivo) ---

def rastrear_contagio(paciente_actual):
    """
    FUNCIÓN RECURSIVA.
    Se llama a sí misma para buscar el origen en la cadena de contagios.
    """
    print(f"🔍 Analizando nexo de: {paciente_actual}...")
    time.sleep(1)  # Simulación de proceso

    # Buscamos quién contagió al paciente actual
    origen = cadena_contagios.get(paciente_actual)

    # CASO BASE 1: No hay registro (Fin del camino sin éxito)
    if origen is None:
        print(f"❌ No se encontró registro de quién contagió a {paciente_actual}.")
        return

    # CASO BASE 2: Encontramos al Paciente Cero (Éxito)
    if origen == "Paciente Cero":
        print(f"🚨 ¡ALERTA! {paciente_actual} fue contagiado por el PACIENTE CERO.")
        print("🛑 CADENA DETENIDA. PROTOCOLO ACTIVADO.")
        return

    # CASO RECURSIVO: Seguimos buscando hacia atrás
    # # Aquí usamos recursividad para trazar
    print(f"   -> {paciente_actual} fue contagiado por {origen}.")
    rastrear_contagio(origen)  # La función se llama a sí misma con el nuevo nombre


# --- 5. FUNCIONES DE MENÚ (Roles Anteriores y Nuevo Modo) ---

def modo_emergencia():
    """
    Rol: Director de Operaciones
    Sub-menú especial para manejar la crisis sanitaria.
    """
    limpiar_pantalla()
    print("🚨 --- MODO EMERGENCIA EPIDEMIOLÓGICA --- 🚨")
    print(" [T] 💉 Sacar Ticket Vacunación (Yield)")
    print(" [R] 🕵️ Rastrear Contagio (Recursividad)")
    print(" [V] 🔙 Volver al Menú Principal")

    opcion = input(">> Seleccione opción: ").upper()

    if opcion == "T":
        print("\nSolicitando ticket a la máquina generadora...")
        # Usamos next() para pedir el siguiente valor al generador Yield
        ticket_actual = next(maquina_vacunacion)
        print(f"✅ TICKET EMITIDO: {ticket_actual}")
        print("(Memoria optimizada, sistema estable)")
        pausar()

    elif opcion == "R":
        print("\n--- BASE DE DATOS: Laura, Carlos, Ana, Pedro ---")
        nombre = input("Ingrese nombre del paciente a rastrear: ")
        rastrear_contagio(nombre)
        pausar()

    elif opcion == "V":
        return  # Vuelve al menú principal
    else:
        print("Opción no válida.")
        time.sleep(1)


def solicitar_hora_medica():
    # (Funcionalidad simplificada de fases anteriores)
    print("\n📅 Sistema de Agendamiento Normal.")
    print("✅ Hora reservada con Dr. House.")
    pausar()


def urgencia_dental():
    print("\n🦷 Sistema de Urgencia Dental.")
    print("✅ Pase a Box 2.")
    pausar()


def salir_sistema():
    print("\n👋 Cerrando Super Tótem v4.0...")
    print("Apagando generadores...")
    time.sleep(1)
    sys.exit()


# --- 6. EL CEREBRO PRINCIPAL (Diccionario) ---

def iniciar_app():
    # Diccionario de Despacho (Menú Principal)
    menu_principal = {
        "1": solicitar_hora_medica,
        "2": urgencia_dental,
        "6": modo_emergencia,  # Nueva Opción Fase 4
        "0": salir_sistema
    }

    while True:
        limpiar_pantalla()
        print("=" * 45)
        print("   🏥 SUPER TÓTEM CESFAM v4.0 🏥")
        print("=" * 45)
        print(" [1] 📅 Solicitar Hora Médica")
        print(" [2] 🦷 Urgencia Dental")
        print(" [6] 🚨 MODO EMERGENCIA (Vacunas/Rastreo)")
        print(" [0] ❌ Salir")
        print("=" * 45)

        seleccion = input(">> Opción: ")

        if seleccion in menu_principal:
            funcion = menu_principal[seleccion]
            funcion()
        else:
            print("🚫 Opción inválida.")
            time.sleep(1)


if __name__ == "__main__":
    iniciar_app()