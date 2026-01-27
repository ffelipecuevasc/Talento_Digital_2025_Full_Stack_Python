class Estudiante:
    """
    Clase que representa a un alumno.
    Sabe su nombre y sabe presentarse gracias a __str__.
    """

    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo

    # Implementamos __str__ para que al imprimir el objeto se vea bonito
    def __str__(self):
        return f"[Legajo {self.legajo}] {self.nombre}"


class Curso:
    """
    Clase que representa un curso.
    Contiene una COLECCIÓN (lista) de objetos Estudiante.
    Esto es una Agregación: El curso agrupa estudiantes.
    """

    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        # Inicializamos la lista vacía. Aquí guardaremos los objetos completos.
        self.lista_estudiantes = []

    def agregar_estudiante(self, estudiante):
        """
        Recibe un objeto de tipo Estudiante y lo guarda en la lista.
        """
        self.lista_estudiantes.append(estudiante)
        print(f"✅ Alumno {estudiante.nombre} agregado al curso {self.nombre_curso}.")

    def listar_estudiantes(self):
        """
        Recorre la lista e imprime a cada estudiante.
        Al hacer print(estudiante), Python invoca automáticamente al __str__ del estudiante.
        """
        print(f"\n--- Lista de Alumnos del Curso: {self.nombre_curso} ---")

        # Validación: Si la lista está vacía, avisamos.
        if not self.lista_estudiantes:
            print("(No hay alumnos inscritos aún)")
        else:
            for alumno in self.lista_estudiantes:
                # AQUÍ OCURRE LA MAGIA:
                # 'alumno' es un objeto. Al imprimirlo, usamos su __str__.
                print(alumno)
        print("--------------------------------------------------")


# --- EJECUCIÓN DEL SISTEMA (PRUEBAS) ---

print("--- 1. Creando los Objetos Individuales (Estudiantes) ---")
# Los estudiantes existen independientemente del curso
est1 = Estudiante("Harry Potter", 101)
est2 = Estudiante("Hermione Granger", 102)
est3 = Estudiante("Ron Weasley", 103)

print("--- 2. Creando el Contenedor (Curso) ---")
curso_magia = Curso("Defensa contra las Artes Oscuras")

# Mostramos lista vacía
curso_magia.listar_estudiantes()

print("\n--- 3. Realizando la Agregación (Inscribiendo alumnos) ---")
# Agregamos los objetos que creamos antes
curso_magia.agregar_estudiante(est1)
curso_magia.agregar_estudiante(est2)
# Ron todavía no se inscribe...

print("\n--- 4. Listando los inscritos ---")
# El curso recorre su lista y colabora con el __str__ de cada objeto
curso_magia.listar_estudiantes()

print("\n--- 5. Agregando uno más tarde ---")
curso_magia.agregar_estudiante(est3)
curso_magia.listar_estudiantes()