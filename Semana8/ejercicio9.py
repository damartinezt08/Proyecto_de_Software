"""Ejercicio 9: Un cálculo que puedo guardar

La tienda calcula importes. Complete calcular_importe(precio, cantidad) para devolver precio por cantidad.
Guarde el resultado de llamar con 2.5 y 4 en importe y muéstrelo fuera de la función.
"""

def calcular_importe(precio, cantidad):
    pass

# Guardar e imprimir el resultado de la llamada.
# src/main.py

def calcular_importe(precio, cantidad):
    return precio * cantidad

# Llamamos a la función con los valores 2.5 y 4
importe = calcular_importe(2.5, 4)

# Mostramos el resultado
print("El importe es:", importe)