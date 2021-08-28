#CONDICIONALES COMPUESTAS
print("SISTEMA PARA APROBAR O DESAPROBAR ALUMNOS")
nom = input("Ingresa tu nombre: ")
mate = float(input(nom+"Cual fue tu nota en matematicas: "))
fisica = float(input(nom+"Cual fue tu nota en fisica: "))
telematica = float(input(nom+"Cual fue tu nota en Telematica: "))

prom = (mate + fisica + telematica) / 3
prom = float(prom)

if prom >= 3 :
    print("Felicidades " + nom + " Aprobaste con un promedio de: ", prom)
    print("Felicidades " + nom + " Aprobaste con un promedio de: ", round(prom,2))
else :
    print(" Lo sentimos "+ nom+ " pero no aprobaste porque tu promedio fue de: ", round(prom,2))

print("Fin.")
