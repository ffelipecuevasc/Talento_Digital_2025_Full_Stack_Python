# Módulo: gestion_alumnos.py

def _validar_nota_rango(texto_solicitud):
    """
    Función interna (privada) para validar rango 1.0 a 7.0
    sin usar excepciones, solo ciclos e ifs.
    """
    nota_valida = False
    valor = 0.0

    while not nota_valida:
        entrada = input(texto_solicitud)
        # Validación básica de que sea número (asumiendo entrada numérica correcta por teclado)
        # Nos enfocamos en la regla de negocio del rango.
        valor = float(entrada)

        if valor >= 1.0 and valor <= 7.0:
            nota_valida = True
        else:
            print("Error: La nota debe estar entre 1.0 y 7.0 (Regla de negocio chilena).")

    return valor

def crear_alumno():
    """
    (C)REATE: Solicita RUT, Nombre y 3 Notas validadas.
    """
    print("\n--- Nuevo Ingreso de Alumno ---")
    rut = input("Ingrese RUT del alumno: ")
    nombre = input("Ingrese Nombre del alumno: ")

    print("Ingrese las 3 notas parciales:")
    notas = []
    # Ciclo para pedir exactamente 3 notas
    for i in range(1, 4):
        nota = _validar_nota_rango(f"Ingrese Nota {i}: ")
        notas.append(nota)

    # Estructura de datos actualizada: Lista de notas
    nuevo_alumno = {
        'rut': rut,
        'nombre': nombre,
        'notas': notas  # Guardamos [n1, n2, n3]
    }
    return nuevo_alumno


def leer_alumnos(lista_alumnos):
    """
    (R)EAD: Muestra listado con detalle de notas.
    """
    print("\n--- Nómina de Alumnos y Notas Parciales ---")
    if not lista_alumnos:
        print("No hay alumnos registrados.")
        return

    for alumno in lista_alumnos:
        # Calculamos promedio al vuelo solo para visualizar
        promedio = sum(alumno['notas']) / len(alumno['notas'])
        notas_str = " - ".join([str(n) for n in alumno['notas']])
        print(
            f"RUT: {alumno['rut']} | Nombre: {alumno['nombre']} | Notas: [{notas_str}] | Promedio: {round(promedio, 1)}")
    return True


def actualizar_alumno(lista_alumnos):
    """
    (U)PDATE: Modifica una nota específica (1, 2 o 3) de un alumno.
    """
    print("\n--- Actualizar Calificación Específica ---")
    rut_buscar = input("Ingrese el RUT del alumno a editar: ")

    found = False
    for alumno in lista_alumnos:
        if alumno['rut'] == rut_buscar:
            print(f"Alumno encontrado: {alumno['nombre']}")
            print(f"Notas actuales: 1) {alumno['notas'][0]} | 2) {alumno['notas'][1]} | 3) {alumno['notas'][2]}")

            # Validación de selección de índice
            indice_valido = False
            opcion = 0
            while not indice_valido:
                opcion = int(input("¿Qué nota desea modificar (1, 2 o 3)?: "))
                if opcion >= 1 and opcion <= 3:
                    indice_valido = True
                else:
                    print("Opción inválida. Elija 1, 2 o 3.")

            # Pedir nueva nota validada
            nueva_nota = _validar_nota_rango("Ingrese la nueva nota (1.0 - 7.0): ")

            # Actualizar la lista (índice es opción - 1)
            alumno['notas'][opcion - 1] = nueva_nota
            found = True
            print("¡Registro de notas actualizado exitosamente!")
            break

    if not found:
        print("Error: Alumno no encontrado.")
    return found


def eliminar_alumno(lista_alumnos):
    """
    (D)ELETE: Elimina un alumno por RUT.
    """
    print("\n--- Eliminar Alumno ---")
    rut_buscar = input("Ingrese el RUT del alumno a eliminar: ")

    for i, alumno in enumerate(lista_alumnos):
        if alumno['rut'] == rut_buscar:
            confirmar = input(f"¿Eliminar a {alumno['nombre']}? (s/n): ")
            if confirmar.lower() == 's':
                eliminado = lista_alumnos.pop(i)
                print(f"Alumno {eliminado['nombre']} eliminado.")
                return eliminado
            else:
                return None
    print("RUT no encontrado.")
    return None