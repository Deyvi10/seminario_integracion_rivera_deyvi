print(" OPERADORES EN EL INVENTARIO ")
print("Operadores Aritmeticos")
stock = 50
ingreso = 20
print(" + Ingreso de mercadería: ", stock, "+", ingreso, "=", stock + ingreso)
print(" - Salida por venta: ", stock, "-", ingreso, "=", stock - ingreso)
print(" * Valor del stock a $3: ", stock, "*", 3, "=", stock * 3)
print(" / Unidades por caja: ", stock, "/", 6, "=", stock / 6)
print(" // Cajas completas: ", stock, "//", 6, "=", stock // 6)
print(" % Unidades sueltas: ", stock, "%", 6, "=", stock % 6)
print(" ** Potencia: ", 2, "**", 5, "=", 2 ** 5)


print("Lista de precios por cantidad (precio unitario $5)")
print(1, "unidad =", 5 * 1)
print(2, "unidades =", 5 * 2)
print(3, "unidades =", 5 * 3)
print(4, "unidades =", 5 * 4)
print(5, "unidades =", 5 * 5)
print(6, "unidades =", 5 * 6)
print(7, "unidades =", 5 * 7)
print(8, "unidades =", 5 * 8)
print(9, "unidades =", 5 * 9)
print(10, "unidades =", 5 * 10)


print("OPERADORES DE COMPARACION")
stock_actual = 8
stock_minimo = 10
print(" == igual a: ", stock_actual, "==", stock_minimo, "=", stock_actual == stock_minimo)
print(" != diferente de: ", stock_actual, "!=", stock_minimo, "=", stock_actual != stock_minimo)
print(" > mayor que: ", stock_actual, ">", stock_minimo, "=", stock_actual > stock_minimo)
print(" < menor que: ", stock_actual, "<", stock_minimo, "=", stock_actual < stock_minimo)
print(" >= mayor o igual que: ", stock_actual, ">=", stock_minimo, "=", stock_actual >= stock_minimo)
print(" <= menor o igual que: ", stock_actual, "<=", stock_minimo, "=", stock_actual <= stock_minimo)


print("OPERADORES LOGICOS")
hay_stock = stock_actual > 0
proveedor_activo = True
bajo_minimo = stock_actual < stock_minimo

puede_vender = hay_stock and proveedor_activo
print("¿Se puede vender?", puede_vender)

hacer_pedido = bajo_minimo or not hay_stock
print("¿Hay que hacer pedido?", hacer_pedido)

print("¿El producto está agotado?", not hay_stock)
