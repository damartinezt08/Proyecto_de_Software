# crear una lsita vacia llamada "calificaciones"
# registrar un maximo de 5 calificaciones
# pedor al isusuario una calificacion entera entre 0 y 100
# si el usuario ingresa -1 el programa termina
# si la calificacion es menor que 0 o mayor qye 100 mostrar calificacion no valida

calificaciones = []
while len(calificaciones) < 5:
    nota = int(input("Registre sus calificaciones: "))
    if nota == -1:
        break
    if nota < 0 or nota > 100:
        print("Nota invalida xd")
        continue
    calificaciones.append(nota)
    
print("sus notas son:", calificaciones)
print(" sus notas son ",len(calificaciones))

