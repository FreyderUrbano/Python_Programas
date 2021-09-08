#EJEMPLO PARA SENTENCIA BRAKE
print("WHILE CON LA SENTENCIA BREAK \n")
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        break
    print("VALOR ACTUAL DE LA VARIABLE: ", contador)
print("Fin del programa la sentencia break se ha ejecutado.")

#EJEMPLE PARA SENTENCIA CONTINUE

print("\n WHILE CON LA SENTENCIA CONTINUE \n")

contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue
        
    print("VALOR ACTUAL DE LA VARIABLE: ", contador)
print("Fin del programa la sentencia continue se ha ejecutado.")