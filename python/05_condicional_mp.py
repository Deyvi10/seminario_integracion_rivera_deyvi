print("Condicional if")
print("Condicional Simple")
stock = 0
if stock == 0:
    print("El producto está agotado")

print("Programa finalizó")


print("Condicional If - else")
print("Condicional Dos Caminos")
stock_disponible = int(input("Stock disponible: "))
cantidad_pedida = int(input("Cantidad solicitada por el cliente: "))

if stock_disponible >= cantidad_pedida:
    print("Venta autorizada")
    print("Stock restante:", stock_disponible - cantidad_pedida)
else:
    print("Stock insuficiente")
    print("Solicitar reposición al proveedor")


print("Condicional If - elif - else")
print("Condicional Condiciones Anidadas")
porcentaje_stock = float(input("Porcentaje de stock en bodega: "))

if porcentaje_stock >= 75:
    print("Stock óptimo")
elif porcentaje_stock >= 50:
    print("Stock suficiente")
elif porcentaje_stock >= 20:
    print("Stock bajo")
else:
    print("Stock crítico")
    print("Generar orden de compra urgente")


print("Condicionales anidados")
proveedor_activo = input("¿El proveedor está activo? SI o NO: ")
unidades_pedido = int(input("Unidades a pedir: "))

if proveedor_activo == "SI":
    if unidades_pedido >= 12:
        print("Pedido aprobado con descuento por volumen")
    else:
        print("Pedido aprobado sin descuento")
else:
    print("No se puede generar el pedido")
    print("Buscar otro proveedor")
