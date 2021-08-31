print("CONVERSOR \n")

print("Menu de opciones \n")
print("Presiona 1 para convertir de numero a palabra.")
print("Presiona 2 para convertir de palabra a numero. \n ")

elexion = int(input("Cual es tu opcion deseada:"))

if elexion == 1:
    print(" \n Convertir de numero a palabra. \n")

    numero1 = int(input("Cual es el numero que deseas convertir a palabra?: "))

    if numero1 == 1:
        print("El numero es ''UNO")
    elif numero1 == 2:
        print("El numero es 'DOS' ")
    elif numero1 == 3:
        print("El numero es 'TRES' ")
    elif numero1 == 4:
        print("El numero es 'CUATRO' ")
    elif numero1 == 5:
        print("El numero es 'CINCO' ")   
    elif numero1 == 6:
        print("El numero es 'SEIS' ")
    else:
        print("EL NUMERO QUE ESCRIBISTE NO EXISTE")  

if elexion == 2:
    print(" \n Convertir de palabra a numero. \n") 

    palabra = input("Cual es la palabra que quieres traducir a numero?: ")
    palabra = palabra.lower()

    if palabra == "uno":
        print("El numero es '1'")
    elif palabra == "dos":
        print("El numero es '2' ") 
    elif palabra == "tres":
        print("El numero es '3' ")         
    elif palabra == "cuatro":
        print("El numero es '4' ")  
    elif palabra == "cinco":
        print("El numero es '5' ")  
    elif palabra == "seis":
        print("El numero es '6' ")  
    else:
        print("LA PALABRA QUE ESCRIBISTE NO EXISTE")      

print("Fin.")