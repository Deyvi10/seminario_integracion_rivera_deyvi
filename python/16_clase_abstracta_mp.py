from abc import ABC, abstractmethod


class Alerta(ABC):
    @abstractmethod
    def enviar(self, producto: str, stock: int) -> str:
        pass


class AlertaPantalla(Alerta):
    def enviar(self, producto: str, stock: int) -> str:
        return f"[PANTALLA] {producto} tiene solo {stock} unidades"


class AlertaCorreo(Alerta):
    def __init__(self, correo: str):
        self.correo = correo

    def enviar(self, producto: str, stock: int) -> str:
        return f"[CORREO a {self.correo}] Reponer {producto}, stock actual: {stock}"


class AlertaProveedor(Alerta):
    def __init__(self, proveedor: str):
        self.proveedor = proveedor

    def enviar(self, producto: str, stock: int) -> str:
        return f"[PEDIDO a {self.proveedor}] Solicitar reposición de {producto}"


inventario = {
    "Martillo de acero": (25, 5),
    "Caja de clavos": (3, 10),
    "Pintura blanca galón": (2, 4)
}

alertas = [
    AlertaPantalla(),
    AlertaCorreo("bodega@laeconomica.ec"),
    AlertaProveedor("Distribuidora Andina")
]

for producto, (stock, stock_minimo) in inventario.items():
    if stock <= stock_minimo:
        for alerta in alertas:
            print(alerta.enviar(producto, stock))

try:
    alerta = Alerta()
except TypeError:
    print("No se puede crear un objeto de una clase abstracta")
