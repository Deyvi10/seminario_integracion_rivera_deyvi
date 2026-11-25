print("CRUD DE PRODUCTOS - CONTROL DE INVENTARIO")
productos = [
    {"id": 1, "nombre": "Martillo de acero", "stock": 25, "stock_minimo": 5, "proveedor": "Distribuidora Andina"},
    {"id": 2, "nombre": "Caja de clavos 2 pulgadas", "stock": 3, "stock_minimo": 10, "proveedor": "Ferretería Mayorista"},
    {"id": 3, "nombre": "Pintura blanca galón", "stock": 12, "stock_minimo": 4, "proveedor": "Importadora del Pacífico"}
]


def create():
    print("\n--- Registrar Producto ---")
    nuevo_id = productos[-1]["id"] + 1 if productos else 1
    nombre = input("Nombre del producto: ")
    stock = int(input("Stock inicial: "))
    stock_minimo = int(input("Stock mínimo: "))
    proveedor = input("Proveedor: ")
    nuevo_producto = {
        "id": nuevo_id,
        "nombre": nombre,
        "stock": stock,
        "stock_minimo": stock_minimo,
        "proveedor": proveedor
    }
    productos.append(nuevo_producto)
    print("Producto registrado.")


def read():
    print("\n--- Lista de Productos ---")
    for producto in productos:
        alerta = " <- STOCK BAJO" if producto["stock"] <= producto["stock_minimo"] else ""
        print(f"{producto['id']} - {producto['nombre']} | Stock: {producto['stock']} | Proveedor: {producto['proveedor']}{alerta}")


def update():
    print("\n--- Actualizar Producto ---")
    id_update = int(input("ID a modificar: "))
    for producto in productos:
        if producto["id"] == id_update:
            producto["nombre"] = input("Nuevo nombre: ")
            producto["stock"] = int(input("Nuevo stock: "))
            producto["stock_minimo"] = int(input("Nuevo stock mínimo: "))
            producto["proveedor"] = input("Nuevo proveedor: ")
            print("Producto actualizado.")
            return
    print("Producto no encontrado.")


def delete():
    print("\n--- Eliminar Producto ---")
    id_delete = int(input("ID a eliminar: "))
    for producto in productos:
        if producto["id"] == id_delete:
            productos.remove(producto)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")


def menu():
    while True:
        print("\n=== CONTROL DE INVENTARIO ===")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción (1 al 5): ")
        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            print("Saliendo del sistema de inventario...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menu()
