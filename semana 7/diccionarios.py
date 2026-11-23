"""prestamo = ["Ana", "Cargador", 2, True]
print(prestamo[1])"""

"""diccionario = {llave : valor}""" # esto es un ITEM, cada ITEM es un par 

"""diccionario = {"estudoante" : "ana",
               "equipo" : "cargador",
               "cantidad" : 2,
               "estado_activo" : True }"""

# Mi ejercicio de diccionarios

"""alumno = ["0001", "Ana", 19, True, ["coloreo", "plastilina"]]"""

"""print(len(alumno))
print(type(alumno))"""
"""print(alumno [4][1])"""

"""for v in range(3):
    materia = input("Digite la materia nueva: ")
    alumno[4].append(materia)
    
print(alumno[4])"""

# Mi primer diccionario
empleado = {"nombre" : "Alfonso"}

print(empleado["nombre"])

empleado["nombre"] = "Jorge"
print(empleado["nombre"])

empleado["carnet"] = "J001"
print(empleado["carnet"])
print(empleado)
print(empleado.get("tiempo", "Nuay"))

cantidad_hijos = int(input("Digite la cantidad de hijos: "))
if cantidad_hijos > 0:
    empleado["hijos"] = []
    for i in range (cantidad_hijos): 
        hijo = input(f"Nombre del hijo {i+1}: ")
        empleado["hijos"].append(hijo)
print(empleado)
        
            