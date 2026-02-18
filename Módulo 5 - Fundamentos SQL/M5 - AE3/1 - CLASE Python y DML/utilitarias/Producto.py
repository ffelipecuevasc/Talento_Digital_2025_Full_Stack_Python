# Este módulo contendrá la clase Producto
class Producto:

    # Constructor
    def __init__(self, id = None, nombre = None, categoria = None,
                 marca = None, precio = 0.0, stock = 0, descuento = 0.0,
                 peso = 0.0, fecha_ingreso = None):
        # Aplicamos encapsulación nivel PROTEGIDO (PROTECTED)
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        self._marca = marca
        self._precio = precio
        self._stock = stock
        self._descuento = descuento
        self._peso = peso
        self._fecha_ingreso = fecha_ingreso

    # Getter y Setter
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_categoria(self):
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def get_stock(self):
        return self._stock

    def set_stock(self, stock):
        self._stock = stock

    def get_descuento(self):
        return self._descuento

    def set_descuento(self, descuento):
        self._descuento = descuento

    def get_peso(self):
        return self._peso

    def set_peso(self, peso):
        self._peso = peso

    def get_fecha_ingreso(self):
        return self._fecha_ingreso

    def set_fecha_ingreso(self, fecha_ingreso):
        self._fecha_ingreso = fecha_ingreso

    # Metodo STR
    def __str__(self):
        return (f"--- PRODUCTO ID: {self._id} ---\n"
                f"- Nombre: {self._nombre}\n"
                f"- Categoría: {self._categoria}\n"
                f"- Marca: {self._marca}\n"
                f"- Precio: ${self._precio}\n"
                f"- Stock: {self._stock}\n"
                f"- Descuento: {self._descuento}\n"
                f"- Peso: {self._peso}\n"
                f"- Fecha de Ingreso: {self._fecha_ingreso}\n"
                f"--------------------------------------")
