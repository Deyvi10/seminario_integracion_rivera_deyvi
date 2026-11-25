stock = 0
while stock < 50:
    stock += 10
    print("Se recibió un lote de 10 unidades. Stock:", stock)
print("Se alcanzó el stock objetivo")


stock_minimo = 15
while stock > stock_minimo:
    stock -= 8
    print("Venta de 8 unidades. Stock:", stock)
print("Alerta: el stock llegó al mínimo, generar pedido")

print("--------------------Continue y break----------------------")
dia = 0
while dia < 10:
    dia += 1
    if dia == 3:
        print("Día", dia, ": inventario físico, no hay despachos")
        continue
    print("Día", dia, ": despachos normales")
    if dia == 6:
        print("Fin de la semana laboral")
        break


print("-----------------------Ejercicio-------------------------")
stock = 20
opcion = ""
while opcion != "3":
    print("\nStock actual:", stock)
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        cantidad = int(input("Unidades que ingresan: "))
        stock += cantidad
    elif opcion == "2":
        cantidad = int(input("Unidades que salen: "))
        if cantidad > stock:
            print("No hay stock suficiente")
            continue
        stock -= cantidad
        if stock <= 5:
            print("Alerta: stock bajo")
    elif opcion != "3":
        print("Opción inválida")
print("Stock final:", stock)
