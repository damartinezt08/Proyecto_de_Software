# Estado inicial del inventario
inventario = {
    "EXT": {"nombre": "Extensión electrica", "unidades": 6},
    "ADA": {"nombre": "Adaptador HDMI", "unidades": 3},
    "MIC": {"nombre": "Microgono", "unidades": 2}
}

# Prestamos pendientes
prestamos = {}

def entregar_prestamo():
    nombreGrupo = input("Ingrese el nombre del grupo: ")
    prestamo = {}
    while True:
        codigo = input("Ingrese el código del equipo (o 'fin' para terminar): ").strip().upper()
        if codigo == 'FIN':
            break
        cantidad = int(input(f"Ingrese la cantidad de {inventario[codigo]['nombre']}: "))
        if cantidad > inventario[codigo]['unidades']:
            print(f"No hay suficientes unidades de {inventario[codigo]['nombre']}.")
            continue
        prestamo[codigo] = cantidad
        inventario[codigo]['unidades'] -= cantidad

    prestamo_id = len(prestamos) + 1
    prestamos[prestamo_id] = {"grupo": nombreGrupo, "equipos": prestamo}
    print(f"Prestamo registrado con ID: {prestamo_id}")

def recibir_devolucion():
    prestamo_id = input("Ingrese el identificador del prestamo: ").strip()
    if prestamo_id not in prestamos:
        print("Identificador no encontrado o ya devuelto.")
        return

    prestamo = prestamos[prestamo_id]
    for codigo, cantidad in prestamo["equipos"].items():
        inventario[codigo]["unidades"] += cantidad
    print(f"Devolución recibida para prestamo ID: {prestamo_id}")
    del prestamos[prestamo_id]

def consultar_estado():
    print("Estado del inventario:")
    for codigo, equipo in inventario.items():
        print(f"Código: {codigo}, Nombre: {equipo['nombre']}, Unidades: {equipo['unidades']}")

    print("\nPrestamos pendientes:")
    for prestamo_id, prestamo in prestamos.items():
        print(f"ID: {prestamo_id}, Grupo: {prestamo['grupo']}")
        for codigo, cantidad in prestamo["equipos"].items():
            print(f"  - {inventario[codigo]['nombre']}: {cantidad}")

def main():
    while True:
        print("\nMesa de Atención de Equipos")
        print("1. Entregar Prestamo")
        print("2. Recibir Devolución")
        print("3. Consultar Estado")
        print("4. Salir")
        opcion = input("Ingrese una opción: ").strip()

        if opcion == '1':
            entregar_prestamo()
        elif opcion == '2':
            recibir_devolucion()
        elif opcion == '3':
            consultar_estado()
        elif opcion == '4':
            print("Sesión finalizada.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
    