"""
Manejo de Cadena de Caracteres
"""
nombre1="Qui-Gon Jin"
print(f"Jedi 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")
nombre2="Obiwan Kenobi"
print(f"Jedi 2: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")

######## Funciones comunes de las variables String
print("Funciones comunes de texto")
droide_1 ="R2-D2"
droide_2 ="C3PO"
longitud_droide_1=len(droide_1)
longitud_droide_2=len(droide_2)
print("nombre droide 1", droide_1)
print("longitud droide 1", longitud_droide_1)
print("nombre droide 2", droide_2)
print("longitud droide 2", longitud_droide_2)

print("Convertir Mayusculas y minúsculas")
mensaje = "La federación invade el Planeta Naboo"
mensaje_mayuscula = mensaje.upper()
mensaje_minuscula = mensaje.lower()
print("Mensaje Original", mensaje)
print("Mensaje en Mayuscula", mensaje_mayuscula)
print("Mensaje en Minuscula", mensaje_minuscula)

print("Reemplazo de substring")
mensaje = "La nave viajará a Tatooine"
nuevo_mensaje = mensaje.replace("Tatooine", "Coruscant")
print("Mensaje Original", mensaje)
print("Mensaje Reemplazado", nuevo_mensaje)