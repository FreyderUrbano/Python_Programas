#OPERADORES RELACIONALES EN PYTHON

print("COMPARACION ENTRE DOS NUMEROS \n")

num1 = int(input("INTRODUCE EL PRIMER NUMERO: "))
num2 = int(input("INTRODUCE EL SEGUNDO NUMERO: "))

print("\n LOS NUMEROS A COMPARARA SON: ", num1," y ", num2,"\n")

if num1 < num2:
    print(num1, " es menor que ",num2 )
if num1 > num2:
    print(num1, " es mayor que ",num2 )
if num1 == num2:
    print(num1, " es igual que ",num2 )
if num1 != num2:
    print(num1, " es difente de  ",num2 )
if num1 <= num2:
    print(num1, " es menor o igual que ",num2 ) 
if num1 >= num2:
    print(num1, " es mayor o igual que ",num2 )

print("\n Fin.")
