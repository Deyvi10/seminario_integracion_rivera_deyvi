print("---------Funciones en el Control de Inventario---------")
print("Autor: Deyvi Rivera")


def mostrar_bienvenida():
    print("Sistema de Control de Inventario")
    print("Ferretería La Económica")

mostrar_bienvenida()


def registrar_entrada(producto, cantidad):
    print("Ingreso de", cantidad, "unidades de", producto)

registrar_entrada("Martillo", 10)
registrar_entrada("Pintura", 4)


def calcular_valor_inventario(stock, precio):
    valor = stock * precio
    return valor

resultado = calcular_valor_inventario(25, 8.50)
print("Valor del inventario de martillos:", resultado)

resultado = calcular_valor_inventario(12, 18.75)
print("Valor del inventario de pintura:", resultado)


def verificar_stock(producto, stock, stock_minimo):
    if stock <= stock_minimo:
        print(f"Alerta: {producto} tiene stock bajo ({stock} unidades)")
    else:
        print(f"{producto} tiene stock suficiente ({stock} unidades)")

verificar_stock("Caja de clavos", 3, 10)
verificar_stock("Martillo", 25, 5)


producto_actual: str = "Taladro Percutor"
stock_actual: int = 8
disponible: bool = True


def registrar_salida(stock: int, cantidad: int) -> int:
    if cantidad > stock:
        print("No hay stock suficiente para", cantidad, "unidades")
        return stock
    return stock - cantidad

stock_actual = registrar_salida(stock_actual, 3)
print("Stock de", producto_actual, "después de la venta:", stock_actual)
stock_actual = registrar_salida(stock_actual, 10)
print("Stock final:", stock_actual)


def calcular_precio_venta(costo: float, margen: float = 0.30) -> float:
    return round(costo * (1 + margen), 2)

print("Precio de venta con margen normal:", calcular_precio_venta(10))
print("Precio de venta con margen del 50%:", calcular_precio_venta(10, 0.50))
