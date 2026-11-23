# Obtener un valor

estudiante = {
    "nombre": "Carlos",
    "edad": 19,
    "carrera": "Software"
}
print(estudiante["nombre"])
print(estudiante["carrera"])

celular = {
    "marca": "Samsung",
    "modelo": "Galaxy S24",
    "almacenamiento": 256,
    "precio": 750
}
print(f"El precio es de ${celular["precio"]}")

# Modificar dicionarios
producto = {
    "nombre": "Cuaderno",
    "precio": 2.5,
    "existencias": 8
}

producto["precio"] = 3.0            #Solo es para agregar otro producto


# Agregar elementos a un diccionario
producto = {
    "nombre": "Cuaderno",
    "precio": 2.5
}

producto["color"] = "Azul"




empleado = {
    "nombre": "Carlos",
    "puesto": "Contador",
    "salario": 850
}

empleado["departamento"] = "Finanzas"
empleado["edad"] = 25

print(empleado["nombre"], empleado["puesto"], empleado["salario"], empleado["departamento"], empleado["edad"])


# Comprobar lo aprendido
curso = {
    "nombre": "Python",
    "duracion": 12,
    "nivel": "Principiante"
}

"""Cambia el nivel a "Intermedio".

Agrega una clave "profesor" con el valor "Roberto".

Agrega una clave "alumnos" con el valor 25.

Muestra toda la información del diccionario."""

curso["nivel"] = "intermedio"
curso["profesor"] = "Roberto"
curso["alumnos"] = 25

print(curso["nombre"], curso["duracion"], curso["nivel"], curso["profesor"], curso["alumnos"])




# Eliminar elementos de un diccionario: del

producto = {
    "nombre": "Laptop",
    "precio": 800,
    "marca": "HP"
}

del producto["marca"]

print(producto)


estudiante = {
    "nombre": "Carlos",
    "edad": 20,
    "carrera": "Software",
    "universidad": "ESEN"
}

del estudiante["edad"]
del estudiante["universidad"]

print(estudiante)


# Comprobar si existe una clave
estudiante = {
    "nombre": "Carlos",
    "carrera": "Software"
}

print("nombre" in estudiante)          #True
print("carrera" in estudiante)         #True
print("edad" in estudiante)            #False

# Combinar lo aprendido
empleado = {
    "nombre": "Andrea",
    "puesto": "Analista",
    "salario": 850,
    "departamento": "Ventas"
}

print("salario" in empleado)
empleado["salario"] = 950
empleado["edad"] = 24
del empleado["departamento"]
print(empleado)


# Recorrer un diccionario con for
empleado = {
    "nombre": "Andrea",
    "puesto": "Analista",
    "salario": 850
}

for clave in empleado:
    print(clave)
    
for todos in empleado:
    print(todos)
    
    
    
# Obtener valores con .values()
for valor in empleado.values():
    print(valor)
    
for todo in empleado.values():
    print(todo)
    
# Recorrer claves y valores juntos con .items()
for clave, valor in empleado.items():
    print(clave, valor)
    
for codigo, resultado in empleado.items():
    print(codigo, resultado)
