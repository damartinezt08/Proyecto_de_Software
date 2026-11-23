"""Ejercicio 3: Una ficha actualizada

La tienda recibe un nuevo conteo: ahora hay 12 unidades. Actualice existencias y agregue categoria con valor Papelería. Luego muestre nombre, existencias y categoria, en ese orden.
"""

producto = {"nombre": "Cuaderno", "precio": 2.5, "existencias": 8}

# Actualizar una clave existente y agregar una nueva.

producto["existencias"] = 12
producto["categoria"] = "papeleria"

print(producto["nombre"], producto["existencias"], producto["categoria"])