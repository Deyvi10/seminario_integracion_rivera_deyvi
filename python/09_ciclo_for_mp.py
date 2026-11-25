print("Conteo de cajas recibidas")
for caja in range(1, 6):
    print("Revisando caja", caja)

print("Lista de precios por cantidad (precio unitario $2.50)")
for cantidad in range(1, 11):
    print(cantidad, "unidades =", 2.5 * cantidad)

print("Pedidos en múltiplos de 3")
for cantidad in range(3, 31, 3):
    print("Pedido de", cantidad, "unidades")


productos = [
    {"id": 1, "nombre": "Martillo de acero", "stock": 25},
    {"id": 2, "nombre": "Caja de clavos", "stock": 3},
    {"id": 3, "nombre": "Pintura blanca galón", "stock": 12}
]

print("---------------- Lista de productos ----------------")
for producto in productos:
    print(f"{producto['id']} - {producto['nombre']}: {producto['stock']} unidades")


proveedores = ["Distribuidora Andina", "Importadora del Pacífico", "Ferretería Mayorista"]
for proveedor in proveedores:
    print("Proveedor:", proveedor)


stock_por_producto = {
    "Martillo": 25,
    "Clavos": 3,
    "Pintura": 12,
    "Brocha": 0
}

for nombre, stock in stock_por_producto.items():
    if stock == 0:
        print(nombre, "está agotado")
    elif stock < 5:
        print(nombre, "tiene stock bajo")
    else:
        print(nombre, "tiene stock suficiente")


print("Ciclos for anidados")
bodegas = ["Bodega Norte", "Bodega Sur"]
for bodega in bodegas:
    print("Inventario de:", bodega)
    for estante in range(1, 4):
        print("  Revisando estante", estante)


print("--------------- Break y Continue ---------------")
for nombre, stock in stock_por_producto.items():
    if stock == 0:
        print(nombre, "agotado, se detiene la revisión para hacer el pedido")
        break
    if stock >= 10:
        continue
    print(nombre, "se agrega a la lista de reposición")


total_unidades = 0
for producto in productos:
    total_unidades += producto["stock"]
print("Total de unidades en inventario:", total_unidades)
