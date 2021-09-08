#PYTHON UN POCO MAS AVANZADO METODO DE ABRIR EN CONSOLA 
print("PYTHON MAS AVANZADO")

texto = "TEXTO DE PRUEBA"
nombre = "FREYDER"
altura = "2 metros"
year = 2021

#print(f"{texto}--{nombre}--{altura}--{str(year)}")
print(texto + " " +nombre + " "+ altura +" "+ str(year))

#entradas o peticiones por teclado

sitio = input("CUAL ES TU NOMBRE: ")
print(sitio)

#condicionales
"""
altura = int(input("Cual es tu altura?: " ))
if altura > 190:
    print("ALT@")
else:
    print("BAJO")

"""
"""
#FUNCIONES
var_altura = int(input("Cual es tu altura?: " ))
def mostrarAltura(estatura):
    resultado = ""

    if estatura > 190:
       resultado = ("ALT@")
    else:
       resultado = ("BAJO")
    return resultado
    

print(mostrarAltura(var_altura))
"""
#listas

personas = ["PACHO", "HUGO", "PEIPEI"]
print(personas[2])

for persona in personas:
    print(persona)



