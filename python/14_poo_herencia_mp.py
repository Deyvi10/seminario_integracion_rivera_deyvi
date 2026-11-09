class Producto:
    nombre: str
    precio: float
    stock: int

    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print("Producto:", self.nombre)
        print("Precio: $", self.precio)
        print("Stock:", self.stock)


class ProductoPerecible(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, fecha_caducidad: str):
        super().__init__(nombre, precio, stock)
        self.fecha_caducidad = fecha_caducidad

    def mostrar_caducidad(self):
        print(self.nombre, "caduca el", self.fecha_caducidad)


class ProductoElectrico(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, voltaje: int, garantia_meses: int):
        super().__init__(nombre, precio, stock)
        self.voltaje = voltaje
        self.garantia_meses = garantia_meses

    def mostrar_garantia(self):
        print(self.nombre, "funciona a", self.voltaje, "V y tiene", self.garantia_meses, "meses de garantía")


silicona = ProductoPerecible("Silicona selladora", 4.25, 30, "2027-03-15")
taladro = ProductoElectrico("Taladro percutor", 65.00, 8, 110, 12)

silicona.mostrar_info()
silicona.mostrar_caducidad()
taladro.mostrar_info()
taladro.mostrar_garantia()
