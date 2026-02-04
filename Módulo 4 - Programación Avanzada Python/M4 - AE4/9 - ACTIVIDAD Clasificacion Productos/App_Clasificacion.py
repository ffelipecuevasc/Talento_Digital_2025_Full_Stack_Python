from datetime import datetime  # Importamos para manejar fechas reales


# 1. Definimos la Clase Base
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        # Método base genérico
        return f"📦 {self.nombre} (${self.precio}) - Categoría: {self.categoria}"


# 2. Subclase Electrónico
class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, garantia_anios):
        # Llamamos al constructor del padre
        super().__init__(nombre, precio, categoria)
        self.garantia_anios = garantia_anios

    # Sobrescritura: Agregamos el dato de garantía al mensaje
    def mostrar_info(self):
        return f"💻 {self.nombre} (${self.precio}) | Garantía: {self.garantia_anios} años"


# 3. Subclase Alimento
class Alimento(Producto):
    def __init__(self, nombre, precio, categoria, fecha_vencimiento):
        super().__init__(nombre, precio, categoria)
        self.fecha_vencimiento = fecha_vencimiento  # Formato esperado: "YYYY-MM-DD"

    # Sobrescritura: Agregamos la fecha de vencimiento al mensaje
    def mostrar_info(self):
        return f"🍏 {self.nombre} (${self.precio}) | Vence el: {self.fecha_vencimiento}"


# --- FUNCIÓN GESTORA DEL PEDIDO (La lógica compleja) ---
def procesar_pedido(lista_productos):
    print("--- 🛒 Procesando Carrito de Compras ---")

    fecha_hoy = datetime.now().date()  # Obtenemos la fecha actual del sistema

    for producto in lista_productos:
        # 1. POLIMORFISMO: Mostramos la info básica
        # Cada producto se presenta a su manera
        print(producto.mostrar_info())

        # 2. VALIDACIÓN DINÁMICA CON ISINSTANCE

        # Caso A: Si es Electrónico, chequeamos garantía
        if isinstance(producto, Electronico):
            if producto.garantia_anios > 0:
                print(f"   ✅ Garantía válida de {producto.garantia_anios} años registrada.")
            else:
                print("   ⚠️ ADVERTENCIA: Este producto se vende SIN garantía extendida.")

        # Caso B: Si es Alimento, chequeamos vencimiento (Lógica PRO)
        elif isinstance(producto, Alimento):
            # Convertimos el string de fecha a un objeto fecha real
            fecha_venc = datetime.strptime(producto.fecha_vencimiento, "%Y-%m-%d").date()

            if fecha_venc < fecha_hoy:
                print("   ⛔ ALERTA CRÍTICA: ¡Producto VENCIDO! Retirar de la venta inmediatamente.")
            elif fecha_venc == fecha_hoy:
                print("   ⚠️ ATENCIÓN: Vence HOY. Poner en oferta 50% OFF.")
            else:
                dias_restantes = (fecha_venc - fecha_hoy).days
                print(f"   ✅ Estado fresco. Vence en {dias_restantes} días.")

        print("-" * 40)


# --- ZONA DE PRUEBAS ---

# Creamos un inventario mixto
inventario = [
    Electronico("Smart TV 50'", 450000, "Hogar", 3),
    Alimento("Leche Descremada", 1200, "Lácteos", "2023-10-01"),  # Fecha antigua (Vencido)
    Electronico("Audífonos Genéricos", 5000, "Audio", 0),  # Sin garantía
    Alimento("Pan Integral", 2500, "Panadería", datetime.now().strftime("%Y-%m-%d")),  # Vence hoy
    Producto("Caja Misteriosa", 9990, "Varios")  # Producto base genérico
]

# Ejecutamos el procesamiento
procesar_pedido(inventario)