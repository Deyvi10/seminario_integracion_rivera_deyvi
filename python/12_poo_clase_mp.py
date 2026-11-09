class Producto:
    nombre: str
    categoria: str
    stock: int
    precio: float

    def __init__(self, nombre: str, categoria: str, stock: int, precio: float):
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock
        self.precio = precio

    def mostrar_info(self):
        print("Producto:", self.nombre)
        print("Categoría:", self.categoria)
        print("Stock:", self.stock)
        print("Precio: $", self.precio)

    def valor_inventario(self) -> float:
        return self.stock * self.precio



martillo = Producto("Martillo de acero", "Herramientas", 25, 8.50)
pintura = Producto("Pintura blanca galón", "Pinturas", 12, 18.75)
cable = Producto("Cable eléctrico 100m", "Electricidad", 6, 45.00)

martillo.mostrar_info()
print("Valor en inventario: $", martillo.valor_inventario())
pintura.mostrar_info()
print("Valor en inventario: $", pintura.valor_inventario())
cable.mostrar_info()
print("Valor en inventario: $", cable.valor_inventario())
