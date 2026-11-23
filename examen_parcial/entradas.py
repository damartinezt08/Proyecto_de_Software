# entrada de adulto $5.00
# entrada de menores $3.00
# indicar cantidad entera de adultos y cantidad entera de menores y el dinero disponible para pagar
# cada grupo debe incluir por lo menos 1 adulto  y como maximo 2 menores por adulto
# la cantidad de menores puede ser 0
# el dinero disoonible puede ser 0 pero no negativo
# si algun dato incumple las reglas no puede procesarse y no se calculan cobros

# una solicitud valida recive 10% de descuento sobre el valor de todas sus entradas si el grupo tiene 4 personas o más
# grupos menores de cuatro personas pagan el servicio comppleto



adultos = int(input("¿Cuantos adultos son: "))
menores = int(input("Cuantos menores son: "))
dinero = float(input("¿Cuanto dinero posee?: "))
if adultos < 1 or dinero < 0:
    print("Solicitud no valida.")
elif menores > adultos:
    print("Solicitud no valida.")
else:
    personas = adultos + menores
    precio_adultos = adultos * 5.00
    precio_menores = menores * 3.00
    subtotal = precio_adultos + precio_menores
    
    if personas >= 4:
        descuento = subtotal * 0.10
    else:
        descuento = 0
    total = subtotal - descuento

    print("Cantidad de adultos:", adultos)
    print("Cantidad de menores:", menores)
    print("Total de personas:", personas)
    print("Precio de adultos: $", (precio_adultos))
    print("Precio de menores: $", (precio_menores))
    print("Subtotal: $", subtotal)
    print("Descuento: $", descuento)
    print("Total a pagar: $", total)

    if dinero >= total:
        print("Cambio: $", dinero - total)
    else:
        print("Falta: $", total - dinero)



    
    






