# Importamos las clases.
# Nota: Administracion no se importa aquí porque el usuario no la crea directamente,
# la crea el Edificio internamente.
from Edificio import Edificio
from Departamento import Departamento


def menu():
    print("\n" + "=" * 30)
    print("   SISTEMA TUCONDOMINIO.CL")
    print("=" * 30)
    print("1. Crear Edificio Inicial")
    print("2. Agregar Departamentos")
    print("3. Listar Todo")
    print("4. Buscar Departamento (Sobrecarga)")
    print("5. Pagar Gastos Comunes")
    print("6. Actualizar Valor UF (Global)")
    print("7. Salir")
    return input("Seleccione una opción: ")


def main():
    mi_edificio = None

    while True:
        opcion = menu()

        if opcion == "1":
            # Paso 1: Crear el Edificio (Esto dispara la COMPOSICIÓN interna de la Administración)
            nombre = input("Nombre del Edificio: ")
            admin = input("Nombre del Administrador: ")
            mi_edificio = Edificio(nombre, "Av. Siempre Viva 123", admin)
            print("✨ Edificio creado exitosamente.")

        elif opcion == "2":
            if mi_edificio:
                try:
                    num = int(input("Número Depto (ej. 101): "))
                    prop = input("Nombre Propietario: ")
                    deuda = int(input("Deuda Inicial $: "))
                    # Paso 2: Crear objeto Departamento
                    nuevo_depto = Departamento(num, prop, deuda)
                    # Paso 3: Agregación (Sumarlo al edificio)
                    mi_edificio.agregar_departamento(nuevo_depto)
                except ValueError:
                    print("Error: Ingrese números válidos para unidad y deuda.")
            else:
                print("⚠️ Primero debe crear el edificio (Opción 1).")

        elif opcion == "3":
            if mi_edificio:
                mi_edificio.listar_departamentos()
            else:
                print("⚠️ No hay edificio configurado.")

        elif opcion == "4":
            if mi_edificio:
                criterio = input("Ingrese Nº de Depto (ej. 101) o Nombre Propietario: ")

                # Intentamos convertir a int para ver si activamos la búsqueda por número
                if criterio.isdigit():
                    busqueda = int(criterio)  # Se convierte a INT -> Busca por numero
                else:
                    busqueda = criterio  # Se queda como STR -> Busca por nombre

                mi_edificio.buscar_departamento(busqueda)
            else:
                print("⚠️ No hay edificio configurado.")

        elif opcion == "5":
            if mi_edificio:
                try:
                    num = int(input("Ingrese Nº de Depto a pagar: "))
                    # Reutilizamos la búsqueda para obtener el objeto
                    depto_encontrado = mi_edificio.buscar_departamento(num)

                    if depto_encontrado:
                        monto = int(input("Monto a pagar $: "))
                        # Llamamos al método con lógica de encapsulamiento
                        depto_encontrado.pagar_gastos(monto)
                except ValueError:
                    print("Error: Datos inválidos.")
            else:
                print("⚠️ No hay edificio configurado.")

        elif opcion == "6":
            # Cambio de Atributo de Clase (Afecta a todos)
            try:
                nuevo_valor = float(input("Ingrese nuevo valor UF: "))
                Departamento.cambiar_valor_uf(nuevo_valor)
            except ValueError:
                print("Error: Ingrese un valor numérico.")

        elif opcion == "7":
            print("¡Hasta luego! Cerrando TuCondominio.cl...")
            break

        else:
            print("Opción no válida.")


# Punto de entrada estándar de Python
if __name__ == "__main__":
    main()