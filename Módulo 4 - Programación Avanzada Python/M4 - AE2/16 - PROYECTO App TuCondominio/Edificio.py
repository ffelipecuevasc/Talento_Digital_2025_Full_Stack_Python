# Importamos las clases necesarias para que Python las reconozca
from Administracion import Administracion
from Departamento import Departamento


class Edificio:
    """
    Clase Principal.
    Usa COMPOSICIÓN con Administración y AGREGACIÓN con Departamentos.
    """

    def __init__(self, nombre, direccion, nombre_admin_edificio):
        self.nombre = nombre
        self.direccion = direccion

        # --- AGREGACIÓN ---
        # Lista vacía para contener objetos Departamento.
        self.lista_departamentos = []

        # --- COMPOSICIÓN ---
        # Instanciamos la Administración DENTRO del Edificio.
        # Si este objeto Edificio muere, esta instancia de Administración también.
        self.administracion = Administracion(nombre_admin_edificio, "555-1234", "admin@tucondominio.cl")

    def agregar_departamento(self, departamento_obj):
        """Recibe un OBJETO Departamento y lo guarda en la lista"""
        self.lista_departamentos.append(departamento_obj)
        print(f"🏠 Departamento {departamento_obj.numero_unidad} agregado al sistema.")

    def listar_departamentos(self):
        """Muestra todos los departamentos usando su método __str__"""
        print(f"\n--- Nómina de {self.nombre} ---")
        print(f"Gestión a cargo de: {self.administracion}")  # Usa __str__ de Administracion
        print("-" * 40)
        for depto in self.lista_departamentos:
            print(depto)  # Usa __str__ de Departamento
        print("-" * 40)

    # --- SOBRECARGA SIMULADA ---
    def buscar_departamento(self, dato_busqueda):
        """
        Busca un departamento. Se comporta distinto según el tipo de dato:
        - Si es INT: Busca por número de unidad.
        - Si es STR: Busca por nombre del propietario.
        """
        encontrado = None

        # Lógica para detectar el tipo de dato (Sobrecarga)
        if isinstance(dato_busqueda, int):
            print(f"🔎 Buscando por Número de Unidad: {dato_busqueda}...")
            for depto in self.lista_departamentos:
                if depto.numero_unidad == dato_busqueda:
                    encontrado = depto
                    break
        elif isinstance(dato_busqueda, str):
            print(f"🔎 Buscando por Propietario: {dato_busqueda}...")
            for depto in self.lista_departamentos:
                # .lower() para que no importen mayúsculas/minúsculas
                if dato_busqueda.lower() in depto.propietario.lower():
                    encontrado = depto
                    break

        if encontrado:
            print("✅ ¡Encontrado!")
            print(encontrado)
            return encontrado
        else:
            print("❌ No se encontraron coincidencias.")
            return None