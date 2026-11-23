
# main.py

# Nivel: Principiante Puro (Sin formato avanzado, solo print, input, if/else)
#  Menú principal que orquesta los módulos del sistema FerreStock.

import json
from inventario import Inventario
from ventas import ModuloVentas
from compras import ModuloCompras
from pronostico import ModuloPronostico


def menu():
    # Cargar inventario compartido
    inventario = Inventario("inventario.json")
    ventas = ModuloVentas(inventario)
    compras = ModuloCompras(inventario)
    pronostico = ModuloPronostico(inventario)

    while True:
        print(" FERRESTOCK - MENÚ PRINCIPAL")
    
        print("1. MÓDULO D Registrar nuevo producto")
        print("2. MÓDULO D Ver catálogo y stock")
        print("3. MÓDULO B Registrar venta (Demanda real)")
        print("4. MÓDULO A Crear orden de compra ('en tránsito')")
        print("5. MÓDULO A Recibir pedido (actualizar stock y L)")
        print("6. MÓDULO C Pronóstico y Reabastecimiento (Min-Max)")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ").strip()

        try:
            
            # Opcion 1: Registrar producto (Módulo D)
            
            if opcion == "1":
                cod = input("Código (ej. P-01): ").strip()

                # Validar si el código ya existe ANTES de pedir más datos
                cod_upper = cod.upper()
                if cod_upper in inventario.productos:
                    print("[ERROR] El código " + cod_upper + " ya existe en el inventario (duplicado).")
                    continue

                nom = input("Nombre o descripción: ").strip()
                print("Categoría:")
                print("  1. Entero (piezas, martillos, palas)")
                print("  2. Peso   (kilos, libras, cemento, cal)")
                cat = input("Seleccione (1 o 2): ").strip()

                # Validar que solo se acepte 1 o 2
                if cat == "1":
                    tipo = "entero"
                elif cat == "2":
                    tipo = "peso"
                else:
                    print("[ERROR] Categoría no válida. Solo puede elegir 1 o 2.")
                    continue

                pre = input("Precio de venta $: ")
                cos = input("Costo de compra $: ")
                stk = input("Stock inicial: ")

                p = inventario.registrar_producto(cod, nom, pre, cos, stk, tipo)
                print("[OK] Producto guardado: " + p.codigo + " - " + p.nombre + " (" + p.tipo_medida + ") | Stock: " + str(p.stock))

            
            # Opcion 2: Consultar catálogo de productos (Módulo D)
           
            elif opcion == "2":
                print(" CATÁLOGO DE PRODUCTOS EN BODEGA")
                if len(inventario.productos) == 0:
                    print("[AVISO] El inventario está vacío actualmente.")
                    print("        Utilice la Opción 1 para registrar un producto primero.")
                else:
                    for cod in inventario.productos:
                        p = inventario.productos[cod]
                        print("  * Código   : " + p.codigo)
                        print("    Nombre   : " + p.nombre)
                        print("    Categoría: " + p.tipo_medida.upper())
                        print("    Stock    : " + str(p.stock))
                        print("    Precio   : $" + str(p.precio))
                        print("    Costo    : $" + str(p.costo))
                        print("    ---------------------------------------------------")
                input("\nPresione Enter para volver al menú principal...")

            
            # Opcion 3: Registrar venta (Módulo B)
            
            elif opcion == "3":
                cod = input("Código de producto a vender: ").strip()
                p = inventario.buscar_producto(cod)
                if p.tipo_medida == "peso":
                    unidad = "kilos o libras (ej. 1.5)"
                else:
                    unidad = "unidades enteras (ej. 12)"

                cant = input("Cantidad solicitada por el cliente en " + unidad + ": ")
                v = ventas.registrar_venta(cod, cant)

                print("[OK] Venta procesada:")
                print("  Unidades vendidas  : " + str(v["vendidas"]))
                print("  Demanda no atendida: " + str(v["no_atendidas"]))
                print("  Demanda real total : " + str(v["demanda_total"]))
                print("  Stock restante     : " + str(inventario.consultar_stock(cod)))

            
            # Opcion 4: Crear orden de compra (Módulo A)
            
            elif opcion == "4":
                cod = input("Código de producto: ").strip()
                p = inventario.buscar_producto(cod)
                prov = input("Nombre del proveedor: ").strip()
                cant = input("Cantidad a pedir: ")
                cos = input("Costo pactado ($): ")

                o = compras.ingresar_orden_compra(cod, prov, cant, cos)
                print("[OK] Orden #" + str(o["id_pedido"]) + " creada en estado 'en tránsito'.")

            
            # Opcion 5: Recibir pedido del proveedor (Módulo A)
            
            elif opcion == "5":
                if len(inventario.pedidos_pendientes) == 0:
                    print("[AVISO] No hay pedidos pendientes en tránsito.")
                    continue

                print("\nPedidos pendientes en tránsito:")
                for p in inventario.pedidos_pendientes:
                    print("  Pedido " + str(p["id_pedido"]) + " -> " + p["codigo"] + " (" + str(p["cantidad_pedida"]) + " con proveedor " + p["proveedor"] + ")")

                id_p = input("Ingrese el número de pedido a recibir: ")
                cant_r = input("Cantidad realmente recibida: ")
                dias_l = input("Días que tardó en llegar, Lead Time L: ")

                entrega, prom_l = compras.ingresar_recepcion(id_p, cant_r, dias_l)
                print("[OK] Recepción completada:")
                print("  Cumplimiento (Fill Rate) : " + str(round(entrega["fill_rate"] * 100, 1)) + "%")
                print("  Días de espera (L)       : " + str(entrega["dias_entrega_L"]) + " días")
                print("  Nuevo stock en bodega    : " + str(inventario.consultar_stock(entrega["codigo"])))
                print("  Demora promedio proveedor: " + str(prom_l) + " días")

            
            # Opcion 6: Pronóstico y Reabastecimiento Min-Max (Módulo C)
            
            elif opcion == "6":
                if len(inventario.productos) == 0:
                    print("AVISO No hay productos en el inventario.")
                    continue

                cod = input("Código del producto a analizar: ").strip()
                dias_x = input("¿Para cuántos días de venta desea comprar? Enter para 15: ").strip()
                if dias_x == "":
                    dias_cobertura = 15
                else:
                    dias_cobertura = int(dias_x)

                dias_l_input = input("¿Días que tarda el proveedor en traer el pedido? Enter para 3: ").strip()
                if dias_l_input == "":
                    dias_l = 3
                else:
                    dias_l = int(dias_l_input)

                res = pronostico.calcular_reabastecimiento(cod, dias_cobertura, dias_l)
                if res["tipo_medida"] == "peso":
                    medida = "kg/lb"
                else:
                    medida = "unidades"

                
                print("REPORTE DE REABASTECIMIENTO: " + res["codigo"] + " - " + res["nombre"])
    
                print("  Venta promedio diaria  : " + str(res["venta_diaria"]) + " " + medida + "/día")
                print("  Stock actual en bodega : " + str(res["stock_bodega"]) + " " + medida)
                print("  Pedidos en camino      : " + str(res["pedidos_en_camino"]) + " " + medida)
                print("  Stock total disponible : " + str(res["stock_disponible"]) + " " + medida)
                
                print("  Stock MÍNIMO (Alerta)  : " + str(res["stock_minimo"]) + " " + medida)
                print("  Stock MÁXIMO (Meta)    : " + str(res["stock_maximo"]) + " " + medida)
                

                if res["alerta_reorden"] == True:
                    print(" ESTADO: ¡ALERTA! El stock está por debajo del MÍNIMO.")
                    print(" SUGERENCIA: Pedir " + str(res["cantidad_a_pedir"]) + " " + medida)
                    print("Inversión estimada $: " + str(res["costo_estimado"]))
                else:
                    print(" ESTADO: Stock suficiente. No hace falta pedir hoy.")
                

            
            # Opcion 7: Salir del programa
            
            elif opcion == "7":
                print("Cerrando el sistema FerreStock")
                break

        except Exception as error:
            print("ERROR: " + str(error))


if __name__ == "__main__":
    menu()
