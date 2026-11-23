# Registra órdenes de compra ("en tránsito") y recepciones con Lead Time L.

from inventario import Inventario


class ModuloCompras:
    def __init__(self, inventario: Inventario):
        # Diagrama A - Inicio: Importar inventario para acceder a productos y stock
        self.inventario = inventario

    
    # RAMA 1: INGRESAR ORDEN DE COMPRA
    
    def ingresar_orden_compra(self, codigo, proveedor, cantidad, costo):
        cod = str(codigo).strip().upper()

        # Diagrama A - Decisión: ¿Datos válidos?
        producto = self.inventario.buscar_producto(cod)
        cant = float(cantidad)
        cost = float(costo)
        prov = str(proveedor).strip()

        if cant <= 0 or cost <= 0 or prov == "":
            raise Exception("La cantidad y costo deben ser mayores a 0, y el proveedor no puede estar vacío.")

        # Validación según categoría
        if producto.tipo_medida == "entero":
            if int(cant) != cant:
                raise Exception("El producto es de categoría ENTERO; ingrese cantidad entera (sin decimales).")
            cant = int(cant)
        else:
            cant = round(cant, 2)

        # Diagrama A - Proceso: Asignar nº de pedido y agregar a la lista de pendientes ("en tránsito")
        total_pedidos = len(self.inventario.pedidos_pendientes) + len(self.inventario.entregas_completadas)
        nuevo_id = total_pedidos + 1

        orden = {}
        orden["id_pedido"] = nuevo_id
        orden["codigo"] = cod
        orden["tipo_medida"] = producto.tipo_medida
        orden["proveedor"] = prov
        orden["cantidad_pedida"] = cant
        orden["costo"] = cost

        self.inventario.pedidos_pendientes.append(orden)
        self.inventario.guardar()
        return orden

    
    # Rama 2: INGRESAR RECEPCIÓN DE PEDIDO
    
    def ingresar_recepcion(self, id_pedido, cantidad_recibida, dias_entrega_L):
        # Diagrama A - Decisión: ¿El pedido está en la lista de pendientes?
        pedido = None
        for p in self.inventario.pedidos_pendientes:
            if p["id_pedido"] == int(id_pedido):
                pedido = p
                break

        if pedido == None:
            raise Exception("El pedido #" + str(id_pedido) + " no existe en pendientes o ya fue recibido.")

        cant_rec = float(cantidad_recibida)
        if cant_rec < 0:
            raise Exception("La cantidad recibida no puede ser negativa.")

        producto = self.inventario.buscar_producto(pedido["codigo"])
        if producto.tipo_medida == "entero":
            if int(cant_rec) != cant_rec:
                raise Exception("El producto es Entero; ingrese número entero sin decimales.")
            cant_rec = int(cant_rec)
        else:
            cant_rec = round(cant_rec, 2)

        # Diagrama A - Proceso: Calcular tiempo de entrega L (en días)
        L = int(dias_entrega_L)

        # Diagrama A - Decisión: ¿Cantidad recibida == cantidad pedida? (Fill Rate)
        cant_pedida = pedido["cantidad_pedida"]
        if cant_pedida > 0:
            fill_rate = cant_rec / cant_pedida
            if fill_rate > 1.0:
                fill_rate = 1.0
        else:
            fill_rate = 1.0

        # Diagrama A - Proceso: Sumar lo recibido al stock del producto y quitar de pendientes
        if cant_rec > 0:
            self.inventario.aumentar_stock(pedido["codigo"], cant_rec)
        self.inventario.pedidos_pendientes.remove(pedido)

        # Diagrama A - Proceso: Guardar la entrega en la lista de entregas completadas
        entrega = {}
        entrega["id_pedido"] = pedido["id_pedido"]
        entrega["codigo"] = pedido["codigo"]
        entrega["tipo_medida"] = producto.tipo_medida
        entrega["proveedor"] = pedido["proveedor"]
        entrega["dias_entrega_L"] = L
        entrega["cantidad_pedida"] = cant_pedida
        entrega["cantidad_recibida"] = cant_rec
        entrega["fill_rate"] = round(fill_rate, 2)

        self.inventario.entregas_completadas.append(entrega)
        self.inventario.guardar()

        # Diagrama A - Decisión: Calcular promedio de demora del proveedor con un bucle for
        suma_dias = 0
        total_entregas = 0
        for e in self.inventario.entregas_completadas:
            if e["proveedor"].lower() == pedido["proveedor"].lower():
                suma_dias = suma_dias + e["dias_entrega_L"]
                total_entregas = total_entregas + 1

        if total_entregas > 0:
            promedio_L = round(suma_dias / total_entregas, 1)
        else:
            promedio_L = L

        return entrega, promedio_L