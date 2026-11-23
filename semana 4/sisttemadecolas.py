# Sistema de control de colas
print("Bienvenido al sistema de control de colas.")

cola = ["Ana", "Pedro", "Carlos"]
retirados = []

# Mostrar cola 
print(cola)


print("Elija una opción (1-6):")
print("1. Agregar estudiante regular")
print("2. Agregar estudiante prioritario")
print("3. Cancelar solicitud")
print("4. Atender usuario")
print("5. Consultar cola")
print("6. Salir del sistema")


# Pedir opciones 
opcion = input("Digite la opcion elegida: ")

if opcion == "1":
    while True:
        estudiante = input("Digite el nombre del estudiante (Ej. Luis): ")
        if estudiante in cola or estudiante =="":
            print("Nombre no es valido")
        else:
            cola.append(estudiante)
            print(cola)
            break
elif opcion =="6":
    confirmacion = input("Esta usted seguro? (Y/N)")
    if confirmacion == "Y":
        print("Gracias por usar nuestro sistema")
        
    else:
        print("Ok sigamos.")
        
        
       
        
    
        
    
    