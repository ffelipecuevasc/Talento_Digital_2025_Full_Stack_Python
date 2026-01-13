import time
import os
import sys


# --- 1. ZONA DE HERRAMIENTAS (Utils) ---

# Para que esta función se ejecute correctamente en PyCharm hay que configurar la opción:
# - Emulate terminal in output console
# Esto se configura en las opciones de ejecución (arranque) del archivo Python

def limpiar_pantalla():
    """
    Limpia la consola para mantener el orden visual del tótem.
    Funciona tanto en Windows como en Mac/Linux.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def pausar():
    """Pequeña pausa para que el usuario alcance a leer."""
    input("\n[Presione ENTER para continuar]")


# --- 2. ZONA DE FUNCIONES (Los Roles del Equipo) ---

def mostrar_menu():
    """
    Rol: Arquitecto
    Muestra la interfaz gráfica del menú principal.
    """
    limpiar_pantalla()
    print("=" * 40)
    print("   🏥  CESFAM SALUD DIGITAL - TÓTEM  🏥")
    print("=" * 40)
    print("👋 ¡Hola! Seleccione su trámite:")
    print("-" * 40)
    print(" [1] 📅  Solicitar Hora Médica")
    print(" [2] 🦷  Urgencia Dental (Triaje)")
    print(" [3] 🍼  Retirar Leche/Alimentos (PNAC)")
    print(" [4] ❌  Salir del Sistema")
    print("=" * 40)


def solicitar_hora_medica():
    """
    Rol: Especialista Clínico
    Simula el proceso de agendar una hora con un médico.
    """
    print("\n--- 📅 SOLICITUD DE HORA MÉDICA ---")
    print("🔎 Buscando disponibilidad en el sistema...")
    time.sleep(1.5)  # Damos suspenso...

    print("✅ ¡Hora Reservada con Éxito!")
    print("   Profesional: Dr. Gregory House")
    print("   Box de Atención: 4")
    print("   Su turno es: A-001")
    pausar()


def urgencia_dental():
    """
    Rol: Especialista Clínico
    Realiza un 'Triaje' (evaluación rápida) para priorizar al paciente.
    """
    print("\n--- 🦷 TRIAJE DENTAL DE URGENCIA ---")
    print("Para evaluar su caso, responda con sinceridad:")
    respuesta = input("¿Siente un dolor agudo ahora mismo? (si/no): ").lower()

    print("Analizando...")
    time.sleep(1)

    if respuesta == "si":
        print("🚨 ALERTA: Pase inmediatamente al Box de Urgencias.")
    else:
        print("ℹ️  AVISO: Su caso no es vital. Por favor pida hora en ventanilla.")
    pausar()


def retirar_leche_o_alimentos():
    """
    Rol: Encargado de Abastecimiento
    Verifica si el paciente puede retirar sus alimentos del PNAC.
    """
    print("\n--- 🍼 RETIRO DE ALIMENTOS (PNAC) ---")
    rut_paciente = input("Ingrese el RUT del beneficiario (sin puntos): ")

    print(f"Consultando base de datos para RUT {rut_paciente}...")
    time.sleep(1.5)

    print("✅ Beneficio Disponible para retiro.")
    print("   📦 Entregar: 2 Kg Leche Purita + 1 Pack Mi Sopita")
    print("   Diríjase a Farmacia.")
    pausar()


def salir_del_sistema():
    """
    Función auxiliar para cerrar el programa ordenadamente.
    """
    print("\n👋 ¡Gracias por usar el sistema de Salud Digital!")
    print("Apagando tótem...")
    time.sleep(1)
    sys.exit()  # Cierra el programa completamente


# --- 3. EL CEREBRO DEL TÓTEM (Main Loop con Diccionario) ---

def iniciar_totem():
    """
    Bloque principal que conecta las teclas con las funciones
    usando un DICCIONARIO en lugar de muchos if/elif.
    """

    # --- AQUÍ ESTÁ EL TRUCO DEL DICCIONARIO ---
    # Creamos un mapa: "Tecla" -> Función (sin paréntesis, solo el nombre)
    menu_opciones = {
        "1": solicitar_hora_medica,
        "2": urgencia_dental,
        "3": retirar_leche_o_alimentos,
        "4": salir_del_sistema
    }

    while True:
        # 1. Mostramos las opciones
        mostrar_menu()

        # 2. Pedimos la tecla al usuario
        eleccion = input(">> Ingrese el número de su opción: ")

        # 3. Lógica de "Despacho" (Dispatch)
        # Verificamos si la tecla existe en nuestro diccionario mapa
        if eleccion in menu_opciones:
            # ¡MAGIA! Obtenemos la función del diccionario y la ejecutamos con ()
            funcion_a_ejecutar = menu_opciones[eleccion]
            funcion_a_ejecutar()
        else:
            # Caso de error (Default)
            print("\n🚫 Opción no válida. Intente con 1, 2, 3 o 4.")
            time.sleep(1)


# --- 4. PUNTO DE ARRANQUE ---
if __name__ == "__main__":
    iniciar_totem()