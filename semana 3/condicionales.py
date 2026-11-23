# Vamos a trabajar con condicionales
"""edad_alumno =int(input("Ingrese la edad del alumno:")) # Cast de string a int
mayoria_edad = 18
adulto = edad_alumno >= mayoria_edad
print(adulto)"""

#investigar por que lo de arriba me da error
# hacer ejercisios de mayor o igual

# Programa para prestamo de equipo 

equipo = input("Digite el quipo (Laptop o Tablet): ")
if equipo == "Laptop":

    horas = int(input(" Horas de prestamo: "))
    if horas < 0:
        print("Solo valores positivos!!!")
    elif horas < 2:
        print("Muy poquito ")
    elif horas <= 4:
        print("Correcto")
    else:
        print("Tampoco...")
else:
    print("Laptop, papá")
    
    



