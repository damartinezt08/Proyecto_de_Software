# se pueden registrar hasta 5 paquetes
# se solicita el peso de cada paquetes en kg
# si se ingresa 0, el registro termina
# si se ingresa un peso negativo, se muestra un mensaje de error y se vuleve a solicitar otro peso
# el 0 y los pesos negativos no se guardan

pesos = []

while len(pesos) < 5:
    peso = int(input("Ingresa el peso del paquete: "))
    
    if peso == 0:
        break
    
    if peso < 0:
        print("Peso invalido")
        continue
    
    pesos.append(peso)
    
print("pesos registrados", pesos)