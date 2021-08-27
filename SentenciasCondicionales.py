print("SISTEMA PARA CALCULAR EL PROMEDIO DE UN ALUMNO")

nombre = str(input("INGRESA TU NOMBRE: "))
mate = int(input("CUAL FUE TU CALIFICACION EN MATEMATICAS: "))
fisica = int(input("CUAL FUE TU CALIFICACION EN FISICA: "))
quimica = int(input("CUAL FUE TU CALIFICACION EN QUIMICA: "))

notas = mate + fisica + quimica
promedio = notas / 3
promedio = int(promedio)

if promedio > 3 :
    print(nombre + " APROBASTE EL AÑO")

print(nombre + " REPROBASTE EL AÑO ")
    



