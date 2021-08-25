print("EJEMPLO DE ASIGNACION:")

mensaje = "MENSAJE UNO "
mensaje += ""
mensaje += "MENSAJE DOS "
print(mensaje)

print("EJEMPLO DE CONCATENACION:")

saludo = "hola como estas "
espacio = ""
nombre = "Freyder"
print(saludo+espacio+nombre)

print("EJEMPLO CONCATENACION CON NUMEROS")

numero1 = 5
numero2 = 10
resultado = numero1 + numero2
resultado = str(resultado)
print("EL RESULTADO DE LA SUMA ES: " + resultado)

print("EJEMPLO DE BUSQUEDA")

mensaje = "HOLA FREYDER"
buscar_subcadena = mensaje.find("FREYDER")
print(buscar_subcadena)

print ('EJEMPLO DE EXTRACCION')

mensaje = 'Freyder Urbano'
extraer_subcadena = mensaje[1:8]
print(extraer_subcadena)

print('EJEMPLO DE COMPARACION VERDADERA')

mensaje1 = 'mia coluche es mi mascota'
mensaje2 = 'topa es mi mascota'
print(mensaje1 == mensaje2)

print('EJEMPLO DE COMPARACION FALSA')

mensaje1 = 'topa es mi mascota'
mensaje2 = 'topa es mi mascota'
print(mensaje1 == mensaje2)

