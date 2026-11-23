productos = {
    "A101": {"tipo": "Teclado", "precio": 25, "unidades": 8},
    "A102": {"tipo": "Mouse", "precio": 15, "unidades": 0},
    "A103": {"tipo": "Monitor", "precio": 180, "unidades": 3},
    "A104": {"tipo": "Audifonos", "precio": 35, "unidades": 5}
}

def buscar_producto(productos, codigo):
    return productos.get(codigo)

def calcular_valor(producto):
    return producto["precio"] * producto["unidades"]

solicitud_usuario = input("Ingrese el código del producto que desea consultar: ")

p = buscar_producto(productos, solicitud_usuario)

if p is None:
    print("Producto no encontrado")
else:
    valor_total = calcular_valor(p)

    print(f"Nombre: {p["tipo"]}")
    print(f"Precio: ${p["precio"]}")
    print(f"Unidades disponibles: {p["unidades"]}")
    print(f"Valor total: ${valor_total}")
    if p["unidades"] == 0:
        print("Producto agotado")


    
    
