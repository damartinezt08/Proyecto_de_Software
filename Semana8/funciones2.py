# Registros de empleados
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
        "nombre" : "Javier", "departamento" : "cobros", "hijos" : [] },
    }

# Declarar la funcion buscar_empleado 
def buscar_empleado(registros, codigo):
    empleado = registros.get(codigo, "Empleado no encontrado")
    return empleado

print(buscar_empleado(empleados, "E003")["hijos"])



