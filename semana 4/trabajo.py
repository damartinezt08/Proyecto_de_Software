# Sistema de atención del laboratorio

cola = ["Sofía", "Mateo", "Valeria"]

while True:

    print("Sistema de atención del laboratorio")
    print("1. Registrar estudiante regular (al final)")
    print("2. Registrar estudiante prioritario (al inicio)")
    print("3. Cancelar una solicitud")
    print("4. Atender al siguiente estudiante")
    print("5. Consultar la cola")
    print("6. Cerrar el sistema")

    opcion = input("Seleccione una opción (1-6): ")

    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("Mensaje de opción inválida.")
        continue

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre == "" or nombre in cola:
            print("Mensaje de error.")
        else:
            cola.append(nombre)
            print("Estudiante agregado al final de la cola.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre == "" or nombre in cola:
            print("Mensaje de error.")
        else:
            cola.insert(0, nombre)
            print("Estudiante agregado al inicio de la cola.")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del estudiante: ")

        if nombre not in cola:
            print("Mensaje de error.")
        else:
            cola.remove(nombre)
            print("Estudiante retirado de la cola.")

    elif opcion == "4":

        if len(cola) == 0:
            print("No hay estudiantes.")
        else:
            estudiante = cola.pop(0)
            print("Atendiendo a:", estudiante)

    elif opcion == "5":
        print("Estudiantes en la cola:", len(cola))

        if len(cola) > 0:
            for i, estudiante in enumerate(cola, 1):
                print(f"{i}. {estudiante}")

    elif opcion == "6":

        if len(cola) == 0:
            print("Sistema cerrado.")
            break
        else:
            print(f"Aún hay {len(cola)} estudiantes en la cola.")
            confirmar = input("¿Desea realmente cerrar? (s/n): ").lower()

            if confirmar == "s":
                print("Sistema cerrado.")
                break
            else:
                print("El sistema continúa.")
                
                