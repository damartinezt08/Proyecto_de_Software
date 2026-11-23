#calcular cobro de paquetes
# puedo ingresar hasta 4 paquetes
# la persona encargada puede cerrar antes ingresando 0 como peso
# cada peso tiene que ser entero positivo en kg
# pesos negativos se rechazan
# el 0 solo indica cierre y tampoco se registra
# al alcanzar 4 paquetes validos el registro termina automaticamente

pesos = []

while len(pesos) < 4:
    peso = int(input("¿Cuál es el peso del paquete? "))
    
    if peso == 0:
        break
    if peso < 0:
        print("El peso no es válido")
        continue
    
    pesos.append(peso)
    
print("Pesos registrados:", pesos)
  



    
    
    




