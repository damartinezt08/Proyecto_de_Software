"""Ejercicio 4: Del código al nombre

Consulte P03 y guarde su registro en una variable llamada persona. Muestre solo su nombre. El código identifica a la persona; nombre es un campo de su registro.
"""

personas = {
    "P01": {"nombre": "Ana", "cursos": ["Excel", "Python"]},
    "P02": {"nombre": "Luis", "cursos": []},
    "P03": {"nombre": "Carla", "cursos": ["Finanzas"]}
}

# Recuperar P03 y mostrar su nombre.
persona = personas["P03"]
print(persona["nombre"])