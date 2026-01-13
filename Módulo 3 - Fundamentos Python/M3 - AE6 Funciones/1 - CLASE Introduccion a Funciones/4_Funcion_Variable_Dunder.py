# --- DEFINICIÓN DE FUNCIONES ---

def dar_bienvenida():
    """
    Función SIN parámetros.

    Esta es una función sencilla, como dar los "Buenos días".
    No necesita información externa para funcionar.
    """
    # 'def' avisa que empieza la función. ':' abre el bloque.
    # Noten el espacio a la izquierda (indentación). ¡Estamos dentro de la función!

    print("¡Bienvenido al sistema!")  # Instrucción 1
    print("Cargando tu perfil...")  # Instrucción 2
    print("-----------------------")  # Instrucción 3


def saludar_personalizado(nombre):
    """
    Función CON parámetros.

    Esta función es más inteligente, necesita información para trabajar.

    Args:
        nombre (str): El nombre de la persona a saludar.
    """
    # 'nombre' es el parámetro (el hueco a llenar).
    # Usamos la variable 'nombre' dentro de la función.

    print(f"Hola, {nombre}. ¡Qué gusto verte!")
    print("Espero que tengas un día genial.")


# --- FUNCIÓN PRINCIPAL ---
def principal():
    """
    Función principal que ejecuta el programa en el orden correcto.

    Orden de ejecución:
    1. dar_bienvenida() - Muestra mensaje de bienvenida
    2. saludar_personalizado(nombre) - Saluda personalizadamente
    """
    print("--- Inicio del programa ---")

    # Primera función: dar bienvenida general
    dar_bienvenida()

    # Segunda función: saludos personalizados
    # Al llamar a la función, debemos enviarle el "argumento" (el dato real).
    saludar_personalizado("Ana")  # Aquí la función recibe "Ana"
    saludar_personalizado("Carlos")  # Aquí recibe "Carlos". Usa la misma lógica.

    print("--- Fin del programa ---")

    # NOTA: Si intentas llamar a saludar_personalizado() sin nada dentro
    # de los paréntesis, ¡Python te dará un error porque le falta un ingrediente!


# --- PUNTO DE ARRANQUE DEL PROGRAMA PYTHON ---

if __name__ == "__main__":

    # __name__ es una VARIABLE DUNDER (double underscore) especial que Python
    # crea automáticamente en cada archivo/módulo.
    # - Si ejecutas este archivo directamente: __name__ = "__main__"
    # - Si lo importas en otro archivo: __name__ = "nombre_del_archivo"

    # ¿POR QUÉ SE RECOMIENDA USAR ESTE PATRÓN?
    # -----------------------------------------
    # 1. SEPARACIÓN DE RESPONSABILIDADES:
    #   - Permite que tu código sea reutilizable como módulo
    #   - Otras personas pueden importar tus funciones sin ejecutar todo
    # 2. TESTING Y DEBUGGING:
    #   - Puedes importar funciones individuales para probarlas
    #   - No se ejecuta automáticamente código no deseado
    # 3. BUENAS PRÁCTICAS:
    #   - Es el estándar en la comunidad Python
    #   - Hace tu código más profesional y mantenible
    principal()  # Ejecuta la función principal solo si el archivo se ejecuta directamente