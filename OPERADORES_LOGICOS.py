#OPERADORES LOGICOS

#OPERADOR LOGICO CONJUNCION

print("CONJUNCION (AND)")

var1 = int(input("INGRESA UN NUMERO MAYOR A 2 Y MENOR A 5: :"))

if var1 > 2 and var1 < 5:
    print("las condiciones se cumplen para el numero ", var1)
else:
    print("la condicion no se cumple para el numero; ",var1)

#OPERADOR LOGICO DISYUNCION

print("DISYUNCION (OR)")

palabra = input("Para cumplir con la condicion escribe 'yes' o 'si':  ")

if palabra == "si" or palabra == "yes":
    print("la condicion se cumple.\n")
else:
    print("la condicion no se cumple.\n")

#OPERADOR NOT NEGACION

print("NEGACION (NOT)")

num = int(input("INGRESA UN NUMERO IGUAL A 5: "))

if not num == 5:
    print("el numero es diferente a 5 y se cumple la condicion")
else:
    print("no se cumple la condicion")

