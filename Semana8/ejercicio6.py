"""Ejercicio 6: El código que no existe

Busque el código fijo P99 con get(). Si no existe, muestre Persona no encontrada. Si existe, muestre su nombre. 
Luego cambie únicamente el código a P01 para comprobar la otra ruta.
"""

personas = {
    "P01": {"nombre": "Ana", "cursos": ["Excel", "Python"]},
    "P02": {"nombre": "Luis", "cursos": []},
    "P03": {"nombre": "Carla", "cursos": ["Finanzas"]}
}

codigo = "P99"
# Buscar y validar antes de acceder a nombre.

persona = personas.get(codigo)

if persona is None:
    print("Persona no encontrada")
else:
    print(persona["nombre"])
    
    
    

