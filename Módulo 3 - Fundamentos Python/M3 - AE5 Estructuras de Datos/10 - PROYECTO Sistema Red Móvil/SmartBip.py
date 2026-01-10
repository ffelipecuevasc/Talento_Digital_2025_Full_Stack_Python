# ==============================================================================
# PROYECTO: SMARTBIP v2.0 (RED MOVILIDAD PRO)
# AUTOR: Equipo de Desarrollo Hackathon (Tú y tus alumnos)
# OBJETIVO: Sistema de transporte con tarifas dinámicas y estadísticas de viaje.
# ==============================================================================

# 1. IMPORTACIONES
# 'datetime' nos permite obtener la hora real del PC para la innovación.
import datetime
# 'Counter' contará automáticamente si usamos más Metro o Micro.
from collections import Counter

# ==============================================================================
# 2. CONFIGURACIÓN Y ESTRUCTURAS DE DATOS INICIALES
# ==============================================================================

# DICCIONARIO DE TARIFAS (Configuración del sistema)
# Simula los precios reales (Valores aproximados para el ejercicio)
tarifas_sistema = {
    "Horario Bajo": 640,
    "Horario Valle": 720,
    "Horario Punta": 810,
    "Tarifa Micro": 710
}

# DICCIONARIO DEL USUARIO (Aquí guardaremos el perfil)
# Lo iniciamos vacío para obligar al usuario a usar la Opción 1 primero.
tarjeta_usuario = {}

# VARIABLES DE CONTROL
sistema_encendido = True
saldo_maximo = 25000  # Regla de negocio real de la Tarjeta Bip!

print("🚇 BIENVENIDO AL SISTEMA SMARTBIP v2.0 🚇")
print("Cargando tarifas y conectando con servidor central...")

# ==============================================================================
# 3. CICLO PRINCIPAL
# ==============================================================================
while sistema_encendido:
    # Decoración visual para la consola de Windows
    print("\n" + "=" * 50)
    print("💳 TÓTEM DE AUTOSERVICIO - RED MOVILIDAD")
    print("=" * 50)
    print("1. 👤 Personalizar Tarjeta (Registro Inicial)")
    print("2. 🚌 Simular Viaje (Cobro Automático)")
    print("3. 💵 Cargar Saldo")
    print("4. 📊 Mi Bitácora de Viajes (Estadísticas)")
    print("5. 🕒 Consultar Tarifario en Vivo (Innovación)")
    print("6. 🚪 Finalizar Sesión")
    print("=" * 50)

    # Captura de opción
    opcion = input("👉 Seleccione una opción: ")

    # ==========================================================================
    # 4. LÓGICA DE CONTROL (MATCH - CASE)
    # ==========================================================================
    match opcion:

        # CASO 1: REGISTRO DE USUARIO
        case "1":
            print("\n--- 👤 PERSONALIZACIÓN DE TARJETA ---")
            id_tarjeta = input("Ingrese N° de Serie de la Tarjeta: ")
            nombre_titular = input("Nombre del Titular: ")

            try:
                carga_inicial = int(input("Ingrese carga inicial ($): "))

                # Validaciones de negocio (Reglas Bip!)
                if carga_inicial < 0:
                    print("❌ ERROR: No puede cargar montos negativos.")
                elif carga_inicial > saldo_maximo:
                    print(f"❌ ERROR: El saldo máximo permitido es ${saldo_maximo}")
                else:
                    # CREACIÓN DEL DICCIONARIO PRINCIPAL
                    # Aquí definimos la estructura de datos del usuario
                    tarjeta_usuario = {
                        "id": id_tarjeta,
                        "nombre": nombre_titular,
                        "saldo": carga_inicial,
                        "historial_medios": [],  # Lista para guardar "Metro", "Micro"
                        "estaciones_unicas": set()  # SET: Guardará estaciones sin repetir
                    }
                    print(f"✅ Tarjeta activada para {nombre_titular} con saldo ${carga_inicial}")

            except ValueError:
                print("❌ ERROR: Debe ingresar un monto numérico válido.")

        # CASO 2: SIMULAR VIAJE (EL CORAZÓN LÓGICO Y LA INNOVACIÓN)
        case "2":
            print("\n--- 🚌 VALIDANDO PASAJE ---")

            # Verificamos si la tarjeta existe (Diccionario no vacío)
            if not tarjeta_usuario:
                print("⚠️ ALERTA: Primero debe personalizar su tarjeta (Opción 1).")
            else:
                medio = input("¿En qué viaja? (1: Metro / 2: Micro): ")

                # --- INNOVACIÓN: DETECCIÓN AUTOMÁTICA DE HORARIO ---
                # Obtenemos la hora actual del sistema operativo (0 a 23)
                hora_actual = datetime.datetime.now().hour
                minuto_actual = datetime.datetime.now().minute
                print(f"🕒 Hora detectada por satélite: {hora_actual}:{minuto_actual}")

                # Lógica para determinar el tramo horario (Simplificada para el ejercicio)
                # Horario Bajo: Antes de las 07:00 o después de las 22:00
                # Horario Punta: 07:00-09:00 y 18:00-20:00
                # Horario Valle: El resto del día
                nombre_horario = ""
                costo_pasaje = 0

                if medio == "2":  # ES MICRO
                    nombre_horario = "Tarifa Micro"
                    costo_pasaje = tarifas_sistema["Tarifa Micro"]
                elif medio == "1":  # ES METRO
                    # Lógica de rangos horarios para Metro
                    if 7 <= hora_actual < 9 or 18 <= hora_actual < 20:
                        nombre_horario = "Horario Punta"
                    elif hora_actual < 7 or hora_actual >= 22:
                        nombre_horario = "Horario Bajo"
                    else:
                        nombre_horario = "Horario Valle"

                    # Obtenemos el precio del diccionario de tarifas
                    costo_pasaje = tarifas_sistema[nombre_horario]

                    # Si es Metro, preguntamos la estación para el SET
                    estacion = input("Ingrese nombre de Estación de Metro: ").strip().title()
                    # .add() agrega al conjunto. Si la estación ya estaba, no la duplica.
                    tarjeta_usuario["estaciones_unicas"].add(estacion)

                else:
                    print("❌ Medio de transporte no válido.")
                    costo_pasaje = -1  # Bandera de error

                # --- COBRO Y VALIDACIÓN DE SALDO ---
                if costo_pasaje > 0:
                    print(f"💰 Tarifa aplicada: {nombre_horario} (${costo_pasaje})")

                    if tarjeta_usuario["saldo"] >= costo_pasaje:
                        # Restamos el saldo
                        tarjeta_usuario["saldo"] -= costo_pasaje

                        # Guardamos registro para estadísticas
                        tipo_transporte = "Metro" if medio == "1" else "Micro"
                        tarjeta_usuario["historial_medios"].append(tipo_transporte)

                        print("✅ ¡BIP! Pasaje aceptado.")
                        print(f"💳 Nuevo Saldo: ${tarjeta_usuario['saldo']}")
                    else:
                        print("🔴 SALDO INSUFICIENTE. Por favor cargue su tarjeta.")
                        print(f"Saldo actual: ${tarjeta_usuario['saldo']} | Necesita: ${costo_pasaje}")

        # CASO 3: CARGAR SALDO
        case "3":
            print("\n--- 💵 CARGA DE SALDO ---")
            if not tarjeta_usuario:
                print("⚠️ ALERTA: Primero debe personalizar su tarjeta (Opción 1).")
            else:
                try:
                    monto_carga = int(input("Monto a cargar: $"))
                    nuevo_saldo_proyectado = tarjeta_usuario["saldo"] + monto_carga

                    if monto_carga <= 0:
                        print("❌ El monto debe ser mayor a 0.")
                    elif nuevo_saldo_proyectado > saldo_maximo:
                        print(f"❌ La carga excede el cupo máximo de ${saldo_maximo}")
                        print(f"Cupo disponible: ${saldo_maximo - tarjeta_usuario['saldo']}")
                    else:
                        tarjeta_usuario["saldo"] += monto_carga
                        print(f"✅ Carga exitosa. Saldo Total: ${tarjeta_usuario['saldo']}")
                except ValueError:
                    print("❌ Error: Ingrese un número entero.")

        # CASO 4: ESTADÍSTICAS (COUNTER Y SETS)
        case "4":
            print("\n--- 📊 BITÁCORA DE VIAJES ---")
            if not tarjeta_usuario:
                print("⚠️ No hay datos registrados.")
            else:
                print(f"👤 Usuario: {tarjeta_usuario['nombre']}")
                print(f"💰 Saldo Actual: ${tarjeta_usuario['saldo']}")

                # USO DE COUNTER: Cuenta automáticamente 'Metro' y 'Micro' en la lista
                conteo_viajes = Counter(tarjeta_usuario["historial_medios"])

                print("\n📈 Resumen de uso:")
                # .get(clave, 0) es vital por si nunca ha viajado en uno de los medios
                print(f"   🚇 Viajes en Metro: {conteo_viajes['Metro']}")
                print(f"   🚌 Viajes en Micro: {conteo_viajes['Micro']}")

                # USO DE SETS: Mostramos cuántas y cuáles estaciones únicas conoce
                total_estaciones = len(tarjeta_usuario["estaciones_unicas"])
                print(f"\n📍 Red de Metro desbloqueada: {total_estaciones} estaciones únicas.")
                print(f"   {tarjeta_usuario['estaciones_unicas']}")

        # CASO 5: CONSULTA EN VIVO (HERRAMIENTA ÚTIL)
        case "5":
            print("\n--- 🕒 TARIFARIO EN VIVO ---")
            ahora = datetime.datetime.now()
            print(f"Hora del sistema: {ahora.strftime('%H:%M')}")

            # Replicamos lógica visual para informar al usuario
            h = ahora.hour
            estado = ""
            if h < 7 or h >= 22:
                estado = "Horario Bajo 🌙"
                precio = tarifas_sistema["Horario Bajo"]
            elif (7 <= h < 9) or (18 <= h < 20):
                estado = "Horario Punta 🔥"
                precio = tarifas_sistema["Horario Punta"]
            else:
                estado = "Horario Valle ☀️"
                precio = tarifas_sistema["Horario Valle"]

            print(f"Estado actual: {estado}")
            print(f"Valor pasaje Metro: ${precio}")
            print(f"Valor pasaje Micro: ${tarifas_sistema['Tarifa Micro']} (Fijo)")

        # CASO 6: SALIR
        case "6":
            print("\n👋 Gracias por preferir Red Movilidad. ¡Buen viaje!")
            sistema_encendido = False

        # CASO POR DEFECTO
        case _:
            print("\n❌ Opción no válida, intente nuevamente.")