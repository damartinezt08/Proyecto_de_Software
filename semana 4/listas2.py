#Dos listas para trabajar 
equipos = ["Ada","Turing","Grace","Linus"]
puntajes = [82,95,76,88]
puntaje_minimo = int(input("Digite puntaje minimo"))
index = 0
puntajes_aprobados =[]
equipos_aprobados =[]

for p in puntajes:
    if p >= puntaje_minimo:
        puntajes_aprobados.append(p)
        equipos_aprobados.append(equipos[index])
        index += 1
        print(equipos_aprobados)
        