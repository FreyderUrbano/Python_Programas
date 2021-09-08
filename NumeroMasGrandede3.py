#EJERCICIO NUMERO 3 DE PYTHON DESDE CERO

print("Calcular el numero mayor")

num1 = int(input("INGRESA EL PRIMER NUMERO: "))
num2 = int(input("INGRESA EL SEGUNDO NUMERO: "))
num3 = int(input("INGRESA EL TERCER NUMERO: "))

print("LOS NUMEROS A COMPARAR SON: ",num1,", ",num2," y ",num3)

if num1 > num2 and num2 > num3:
    print("El numero ",num1," es el mayor de los 3")
else:
    if num2 > num3:
       print("El numero ",num2," es el mayor de los 3")
    else: 
       print("El numero ",num3," es el mayor de los 3")
print("Fin.")


