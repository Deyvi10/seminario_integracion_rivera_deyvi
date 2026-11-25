print("Colecciones de datos en el inventario")
print("Listas")
productos = ["Martillo", "Destornillador", "Llave inglesa"]
print("Productos ", productos)
print("Tipo: ", type(productos))
productos.append("Alicate")
print("Después de agregar:", productos)
print("Total de productos:", len(productos))

print("Tuplas")
dimensiones_caja = (40, 30, 25)
print("Dimensiones de la caja (cm):", dimensiones_caja)
print("Tipo: ", type(dimensiones_caja))

print("Diccionario")
producto = {
    "codigo": "HER-001",
    "nombre": "Martillo de acero",
    "stock": 25,
    "precio": 8.50,
    "activo": True
}
print("Producto: ", producto)
print("Nombre:", producto["nombre"])
print("Stock:", producto["stock"])
print("Tipo ", type(producto))

print("Conjunto")
proveedores = {
    "Distribuidora Andina",
    "Importadora del Pacífico",
    "Ferretería Mayorista",
    "Distribuidora Andina"
}
print("Proveedores: ", proveedores)
print("Tipo ", type(proveedores))
