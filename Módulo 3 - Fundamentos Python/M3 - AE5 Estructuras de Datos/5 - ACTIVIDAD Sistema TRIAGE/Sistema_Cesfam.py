import os
import time
from datetime import datetime

# --- CONFIGURACIÓN INICIAL ---
# Lista principal: Aquí guardaremos a los pacientes.
# Cada paciente será una TUPLA: (RUT, Nombre, Edad, Categoría, {Síntomas})
cola_espera = []

# --- INICIO DEL PROGRAMA ---
while True:
    print("\n" + "=" * 40)
    print("🏥  SISTEMA DE GESTIÓN CESFAM PYTHON  🏥")
    print("=" * 40)
    print("1. 📝 Ingresar Paciente (Triage)")
    print("2. 📢 Llamar a Paciente (Atención)")
    print("3. 🔍 Buscar Paciente por RUT")
    print("4. 📊 Estadísticas de Urgencia")
    print("5. 🚪 Salir")
    print("=" * 40)

    opcion = input("Seleccione una opción: ")

    # Usamos MATCH para el menú
    match opcion:
        case "1":
            # Limpieza de pantalla
            # Pequeño truco para que se vea pro (funciona en Windows y Mac/Linux)
            os.system('cls' if os.name == 'nt' else 'clear')

            print("--- FICHA DE INGRESO ---")

            # 1. Datos Personales
            rut = input("RUT (ej: 12345678-9): ")
            nombre = input("Nombre completo: ")

            # 2. Uso de DATETIME (Innovación)
            try:
                fecha_str = input("Fecha de nacimiento (AAAA-MM-DD): ")
                fecha_nac = datetime.strptime(fecha_str, "%Y-%m-%d")
                hoy = datetime.now()
                # Lógica matemática para edad exacta
                edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
                print(f"--> Edad calculada: {edad} años")
            except ValueError:
                print("❌ Error en formato de fecha. Se asignará edad 0 por defecto.")
                edad = 0

            # 3. Síntomas usando SETS (Para no repetir)
            sintomas = set()
            print("Ingrese síntomas (escriba 'fin' para terminar):")
            while True:
                sintoma = input("- Síntoma: ").strip().lower()
                if sintoma == 'fin':
                    break
                sintomas.add(sintoma)  # .add() es el método de los sets

            # 4. Lógica de Triage (IF/ELSE Complejo)
            categoria = "Leve"  # Por defecto

            # Regla: Menores de 1 año o mayores de 70, O dificultad respiratoria
            if edad < 1 or edad > 70 or "dificultad respiratoria" in sintomas:
                categoria = "ALTA PRIORIDAD"
            elif "fiebre" in sintomas or "dolor de pecho" in sintomas:
                categoria = "Media"

            # 5. Guardamos en TUPLA (Inmutable) y luego a la LISTA
            # Estructura: (0:RUT, 1:Nombre, 2:Edad, 3:Categoría, 4:Set_Síntomas)
            nuevo_paciente = (rut, nombre, edad, categoria, sintomas)
            cola_espera.append(nuevo_paciente)

            print(f"\n✅ Paciente {nombre} registrado con categoría: {categoria}")
            input("Presione Enter para continuar...")

        case "2":
            # Limpieza de pantalla
            # Pequeño truco para que se vea pro (funciona en Windows y Mac/Linux)
            os.system('cls' if os.name == 'nt' else 'clear')

            # FIFO: Atendemos al primero de la lista (índice 0)
            if len(cola_espera) > 0:
                paciente_atendido = cola_espera.pop(0)  # .pop(0) saca el primero

                print("📢 LLAMANDO A PACIENTE:")
                print(f"Nombre: {paciente_atendido[1]}")
                print(f"RUT: {paciente_atendido[0]}")
                print(f"Categoría: {paciente_atendido[3]}")
                print(f"Síntomas: {paciente_atendido[4]}")
                print("\n👨‍⚕️ Derivando a box de atención...")
            else:
                print("☕ No hay pacientes en espera. ¡Tómese un café!")

            input("Presione Enter para continuar...")

        case "3":
            # Búsqueda Lineal
            rut_buscar = input("\nIngrese RUT a buscar: ")
            encontrado = False

            for paciente in cola_espera:
                # paciente[0] es el RUT en la tupla
                if paciente[0] == rut_buscar:
                    print(f"✅ Paciente encontrado: {paciente[1]} | Estado: En espera | Categoría: {paciente[3]}")
                    encontrado = True
                    break  # Si lo encontramos, dejamos de buscar

            if not encontrado:
                print("❌ El paciente no está en la lista de espera.")
            input("Presione Enter para continuar...")

        case "4":
            # Estadísticas simples recorriendo la lista
            contador_alta = 0
            suma_edades = 0

            for paciente in cola_espera:
                if paciente[3] == "ALTA PRIORIDAD":
                    contador_alta += 1
                suma_edades += paciente[2]

            promedio_edad = 0
            if len(cola_espera) > 0:
                promedio_edad = suma_edades / len(cola_espera)

            print(f"\n📊 REPORTE CESFAM")
            print(f"Pacientes totales en espera: {len(cola_espera)}")
            print(f"Pacientes ALTA PRIORIDAD: {contador_alta}")
            print(f"Edad promedio en sala: {round(promedio_edad, 1)} años")
            input("Presione Enter para continuar...")

        case "5":
            print("Cerrando sistema... ¡Buen turno! 👋")
            break

        case _:
            print("Opción no válida, intente nuevamente.")