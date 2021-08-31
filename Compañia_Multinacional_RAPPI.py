#EJERCICIO PRACTICO PYTHON DESDE CERO

print("DIAS DE VACACIONES PAR EMPLEADOS DE RAPPI")

nombre = input("INGRESA TU NOMBRE Y APELLIDO: ")
clave = int(input("INGRESA TU CLAVE DE DEPARTAMENTO DONDE 1 (ATENCION AL CLIENTE) 2 (LOGISTICA) 3 (GERENCIA): "))
antiguedad = float(input("INGRESA TU ANTIGUEDAD EN AÑOS DENTRO DE LA EMPRESA: "))

#CLAVE 1 PARA EMPLEADOS QUE TRABAJAN EN EL DEPARTAMENTO DE ATENCION AL CLIENTE

if clave == 1:
    print(nombre + " pertenece al departamento de ATENCION AL CLIENTE.")
    if antiguedad == 1:
        print(nombre," tiene derecho a 6 dias de vacaciones.")
    elif antiguedad > 2 and antiguedad <= 6:
        print(nombre," tiene derecho a 14 dias de vacaciones.")
    elif antiguedad > 7:
        print(nombre, " tiene derecho a 20 dias de vacaciones.")
    else:
        print("SIN DERECHO A VACACIONES.")

#else:
    #print("CLAVE DEPARTAMENTO INVALIDA.")

#CLAVE 2 PARA EMPLEADOS QUE TRABAJAN EN EL DEPARTAMENTO DE LOGISTICA

elif clave == 2:
    print(nombre + " pertenece al departamento de LOGISTICA.")
    if antiguedad == 1:
        print(nombre," tiene derecho a 7 dias de vacaciones.")
    elif antiguedad > 2 and antiguedad <= 6:
        print(nombre," tiene derecho a 15 dias de vacaciones.")
    elif antiguedad >= 7:
        print(nombre, " tiene derecho a 22 dias de vacaciones.")
    else:
        print("SIN DERECHO A VACACIONES.")



#CLAVE 3 PARA EMPLEADOS QUE TRABAJAN EN EL DEPARTAMENTO DE LOGISTICA

elif clave == 3:
    print(nombre + " pertenece al departamento de GERENCIA.")
    if antiguedad == 1:
        print(nombre," tiene derecho a 10 dias de vacaciones.")
    elif antiguedad > 2 and antiguedad <= 6:
        print(nombre," tiene derecho a 20 dias de vacaciones.")
    elif antiguedad >= 7:
        print(nombre, " tiene derecho a 30 dias de vacaciones.")
    else:
        print("SIN DERECHO A VACACIONES.")

else:
    print("CLAVE DEPARTAMENTO INVALIDA.")