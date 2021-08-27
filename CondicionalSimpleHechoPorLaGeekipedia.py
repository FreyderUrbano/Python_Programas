#CONDICIONALES SIMPLES GEEKIPEDIA 
print("SISTEMA PARA CALCULAR EL PROMEDIO DE UN ALUMNO")

nom = input('Cual es tu nombre?: ')

fisica = int(input(nom + ' Cual es tu nota en Fisica?: '))
quimica = int(input(nom + ' Cual estu nota en Quimica?: '))
biologia = int(input(nom + ' Cual estu nota en Biologia?: '))

prom = (fisica + quimica + biologia) / 3
prom = int(prom)

if prom >= 3:
    print('FELICIDADES ' + nom + '"APROBASTE " con un promedio de: ', prom)

print('QUE LASTIMA ' + nom + ' " NO APROBASTE " tu promedio fue de: ', prom)
