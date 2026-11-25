print("Manejo de Cadenas de Caracteres en el Inventario")
producto1 = "Taladro Percutor"
print(f"Producto 1: {producto1}")
print(f"Tipo de datos: {type(producto1)}")
producto2 = "Sierra Circular"
print(f"Producto 2: {producto2}")
print(f"Tipo de datos: {type(producto2)}")

print("Funciones comunes de texto")
codigo_1 = "HER-001"
codigo_2 = "PIN-0025"
print("Código 1", codigo_1, "longitud", len(codigo_1))
print("Código 2", codigo_2, "longitud", len(codigo_2))

print("Convertir Mayusculas y minúsculas")
descripcion = "caja de clavos de 2 pulgadas"
print("Original:", descripcion)
print("Mayúsculas:", descripcion.upper())
print("Minúsculas:", descripcion.lower())
print("Tipo título:", descripcion.title())

print("Reemplazo de substring")
mensaje = "El pedido llegará a la Bodega Norte"
nuevo_mensaje = mensaje.replace("Bodega Norte", "Bodega Sur")
print("Mensaje Original", mensaje)
print("Mensaje Reemplazado", nuevo_mensaje)

print("Separar texto")
categorias = "Herramientas,Pinturas,Electricidad,Plomería"
lista_categorias = categorias.split(",")
print(lista_categorias)
print("Primera categoría:", lista_categorias[0])
print("Última categoría:", lista_categorias[-1])

print("Extraer subcadenas")
codigo = "HER-2026-0045"
prefijo = codigo[0:3]
anio = codigo[4:8]
secuencial = codigo[9:]
print("Prefijo:", prefijo)
print("Año:", anio)
print("Secuencial:", secuencial)

print("Limpiar texto ingresado")
entrada = "   tornillo hexagonal   "
print(f"[{entrada}]")
print(f"[{entrada.strip()}]")

print("Comprobaciones útiles")
print("HER001".isalnum())
print("0045".isdigit())
print("Herramientas".isalpha())
print(codigo.startswith("HER"))
print("TALADRO".isupper())
