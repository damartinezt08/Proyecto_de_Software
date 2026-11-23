"""Ejercicio 5: Dos personas y dos cantidades

Muestre cuántos cursos tiene P01 y cuántos tiene P02, en líneas separadas. Use len() sobre la lista correspondiente; no cuente las claves del registro.
"""

personas = {
    "P01": {"nombre": "Ana", "cursos": ["Excel", "Python"]},
    "P02": {"nombre": "Luis", "cursos": []},
    "P03": {"nombre": "Carla", "cursos": ["Finanzas"]}
}

# Mostrar cantidad de cursos de P01 y P02.

print(len(personas["P01"]["cursos"]))
print(len(personas["P02"]["cursos"]))