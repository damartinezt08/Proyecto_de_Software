# Sistema de calculo e impuestos

try:
    ingreso = int(input("Digite el valor del ingreso: "))
except:
    print("El valor ingresado no es un numero ")
else:
    impuesto = ingreso * 0.1
    print(f"El imouesto calculado es {impuesto}.")
finally:
    print("Gracias mje")