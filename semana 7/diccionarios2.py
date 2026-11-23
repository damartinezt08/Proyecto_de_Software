"""alumno = {
    "carnet" : "c001",
    "nombre" : " Carlos",
    "edad" : 20,
    "direccion" : "San Salvador"
}
del alumno["direccion"]
print(len(alumno))
print(alumno)"""


# Sistema de control de datos de empleados
empleados = {
    "E003" : {
        "nombre" : "Carla", "departamento" : "ventas", "hijos" : ["Mia"]
        },
    "E001" : {
        "nombre" : "Ana", "departamento" : "ventas", "hijos" : ["Lucia", "Diego"]
        },
    "E002" : {
        "nombre" : "Luis", "departamento" : "soporte", "hijos" : []
        },
    "E004" : {
        "nombre" : "Javier", "departamento" : "cobros", "hijos" : []
        },
    }
#empleado_buscar = input("Digite el codigo de el empleado a buscar: ")
#print(empleados.get(empleado_buscar, "Ese codigo no corresponde a un empleado"))

for i, j in empleados.items():
    if j ["departamento"].lower() == "ventas":
        print(f"El empleado {i} con nombre {j["nombre"]} tiene {len(j["hijos"])}")
    