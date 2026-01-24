class Libro:
    """
    Clase que representa un libro en una biblioteca.
    Define el molde para crear múltiples libros.
    """

    def __init__(self, titulo, autor, anio):
        """
        Método constructor: Inicializa los atributos de instancia.
        self.titulo -> Guarda el título específico de ESTE libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        """
        Método para mostrar los detalles del libro en pantalla de forma ordenada.
        """
        print(f"--- Información del Libro ---")
        print(f"Título: {self.titulo}")
        print(f"Autor:  {self.autor}")
        print(f"Año:    {self.anio}")
        print("-----------------------------")


# --- Ejecución de la Demo ---

# 1. Creamos el primer objeto (Instancia 1)
libro_favorito = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

# 2. Creamos el segundo objeto (Instancia 2)
libro_python = Libro("Python Crash Course", "Eric Matthes", 2019)

# 3. Llamamos al método mostrar_info() para cada objeto
# Fíjate cómo el mismo método muestra datos distintos según el objeto.
libro_favorito.mostrar_info()
libro_python.mostrar_info()