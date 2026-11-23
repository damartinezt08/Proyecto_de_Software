# SISTEMA DE INSCRIPCION A TALLER
inscritos = []
continuar = True
cupos = 6

while continuar and cupos > len(inscritos):
    nombre = input("Nombre alumno:")
    nombre = nombre.strip().lower()
    if nombre == "" or nombre in inscritos:
        print("Nombre invalido")
    else:
        inscritos.append(nombre)


