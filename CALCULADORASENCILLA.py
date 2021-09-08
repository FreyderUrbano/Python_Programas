#CALCULADORA SENCILLA CON PYTHON 
print("===========")
print("CALCULADORA")
print("===========")

suma = 1
resta = 2
multiplicacion = 3
division = 4
division_entera = 5
exponencial = 6
resto = 7
print("===============================")
print("MENU PARA ELECCION DE OPERACION")
print("===============================")

print(" 1. Para suma ")
print(" 2. Para resta ")
print(" 3. Para multiplicacion ")
print(" 4. Para division ")
print(" 5. Para division entera ")
print(" 6. exponencial ")
print(" 7. resto \n")

calculo = int(input("Elige el numero para la operacion que quieras realizar: "))

if calculo == 1:
    print("==============")
    print("OPERACION SUMA")
    print("==============\n")

    numero = int(input("Ingresa el primer numero: "))
    numero1 = int(input("Ingresa el segundo numero: "))
    resultado = numero + numero1
    print("La suma entre ",numero," y ",numero1,"es: " + str(resultado))
elif calculo == 2:
    print("===============")
    print("OPERACION RESTA")
    print("===============n")
    numero = int(input("Ingresa el primer numero: "))
    numero1 = int(input("Ingresa el segundo numero: "))
    resultado = numero - numero1
    print("La RESTA entre ",numero," y ",numero1,"es: " + str(resultado))
elif calculo == 3:
    print("\n======================")
    print("OPERACION MULTIPLICACION")
    print("========================\n")
    numero = int(input("Ingresa el primer numero: "))
    numero1 = int(input("Ingresa el segundo numero: "))
    resultado = numero * numero1
    print("La MULTIPLICACION entre ",numero," y ",numero1,"es: " + str(resultado))
elif calculo == 4:
    print("\n=================")
    print("OPERACION DIVISION")
    print("===================\n")
    numero = int(input("Ingresa el primer numero: "))
    numero1 = int(input("Ingresa el segundo numero: "))
    resultado = numero / numero1
    print("La DIVISION entre ",numero," y ",numero1,"es: " + str(resultado))
elif calculo == 5:
    print("\n=======================")
    print("OPERACION DIVISION ENTERA")
    print("========================\n")
    numero = int(input("Ingresa el primer numero: "))
    numero1 = int(input("Ingresa el segundo numero: "))
    resultado = numero // numero1
    print("La DIVISION ENTERA entre ",numero," y ",numero1,"es: " + str(resultado))
elif calculo == 6:
    print("\n===================")
    print("OPERACION EXPONENCIAL")
    print("=====================\n")
    numero = int(input("Ingresa el primer numero: "))
    numero1 = int(input("Ingresa el segundo numero: "))
    resultado = numero ** numero1
    print("La OPERACION EXPONENCIAL entre ",numero," y ",numero1,"es: " + str(resultado))
elif calculo == 7:
    print("\n=============")
    print("OPERACION RESTO")
    print("===============\n")
    numero = int(input("Ingresa el primer numero: "))
    numero1 = int(input("Ingresa el segundo numero: "))
    resultado = numero % numero1
    print("El RESTO entre ",numero," y ",numero1,"es: " + str(resultado))

else:
    print("ERROR EN LA ELEXION.")
print("FIN.")