class Movimiento:
    producto: str
    cantidad: int

    def __init__(self, producto: str, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def aplicar(self, stock: int) -> int:
        return stock

    def mostrar_info(self):
        print("Movimiento de", self.cantidad, "unidades de", self.producto)


class Entrada(Movimiento):
    def aplicar(self, stock: int) -> int:
        return stock + self.cantidad

    def mostrar_info(self):
        print("Entrada:", self.cantidad, "unidades de", self.producto)


class Salida(Movimiento):
    def aplicar(self, stock: int) -> int:
        if self.cantidad > stock:
            print("Salida rechazada, no hay stock suficiente")
            return stock
        return stock - self.cantidad

    def mostrar_info(self):
        print("Salida:", self.cantidad, "unidades de", self.producto)


class Devolucion(Movimiento):
    def aplicar(self, stock: int) -> int:
        return stock + self.cantidad

    def mostrar_info(self):
        print("Devolución de cliente:", self.cantidad, "unidades de", self.producto)


stock_martillos = 25
movimientos = [
    Entrada("Martillo", 10),
    Salida("Martillo", 18),
    Devolucion("Martillo", 2),
    Salida("Martillo", 40)
]

print("Stock inicial:", stock_martillos)
for movimiento in movimientos:
    movimiento.mostrar_info()
    stock_martillos = movimiento.aplicar(stock_martillos)
    print("Stock actual:", stock_martillos)
