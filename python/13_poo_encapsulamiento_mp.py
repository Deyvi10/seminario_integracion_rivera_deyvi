class Producto:
    nombre: str
    __stock: int
    __stock_minimo: int

    def __init__(self, nombre: str, stock: int, stock_minimo: int):
        self.nombre = nombre
        self.__stock = stock
        self.__stock_minimo = stock_minimo

    def get_stock(self) -> int:
        return self.__stock

    def registrar_entrada(self, cantidad: int):
        if cantidad <= 0:
            print("La cantidad de entrada debe ser mayor a 0")
            return
        self.__stock += cantidad
        print(f"Entrada de {cantidad} unidades de {self.nombre}")

    def registrar_salida(self, cantidad: int):
        if cantidad > self.__stock:
            print(f"No hay stock suficiente de {self.nombre}")
            return
        self.__stock -= cantidad
        print(f"Salida de {cantidad} unidades de {self.nombre}")
        if self.__stock <= self.__stock_minimo:
            print(f"Alerta: {self.nombre} llegó al stock mínimo")

    def mostrar_info(self):
        print("Producto:", self.nombre)
        print("Stock:", self.__stock)



martillo = Producto("Martillo de acero", 25, 5)
clavos = Producto("Caja de clavos", 12, 10)

martillo.registrar_salida(5)
martillo.registrar_entrada(10)
martillo.mostrar_info()

clavos.registrar_salida(3)
clavos.registrar_salida(20)
clavos.mostrar_info()

print("Intentando cambiar el stock desde fuera de la clase")
clavos.__stock = 1000
print("Stock real de clavos:", clavos.get_stock())
