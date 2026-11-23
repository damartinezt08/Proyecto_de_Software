
# ventas.py
# Registra las ventas y la demanda no atendida (demanda real).


from inventario import Inventario


class ModuloVentas:
    def __init__(self, inventario: Inventario):
        # Diagrama B - Inicio: Importar inventario para acceder a productos y stock
        self.inventario = inventario

    # Diagrama B: Ingresar venta (código de producto, cantidad)
    def registrar_venta(self, codigo, cantidad):
        cod = str(codigo).strip().upper()

        # Diagrama B - Decisión 1: ¿Código existe en inventario?
        producto = self.inventario.buscar_producto(cod)

        # Diagrama B - Decisión 1: ¿Cantidad es válida y mayor a 0?
        cant_solicitada = float(cantidad)
        if cant_solicitada <= 0:
            raise Exception("La cantidad solicitada debe ser mayor a 0.")

        # Validación según categoría: si es 'entero', no se permiten decimales
        if producto.tipo_medida == "entero":
            # Si al quitar decimales cambia el número 
            if int(cant_solicitada) != cant_solicitada:
                raise Exception(
                    "El producto '" + producto.nombre + "' es de categoría ENTERO. "
                    "No se permiten decimales como 1.5; debe ingresar cantidades enteras (ej. 1, 2, 12)."
                )
            cant_solicitada = int(cant_solicitada)
        else:
            cant_solicitada = round(cant_solicitada, 2)

        stock_actual = producto.stock

        # Diagrama B - Decisión 2: ¿Stock >= cantidad solicitada?
        if stock_actual >= cant_solicitada:
            #  Rama Si: Descontar stock y registrar venta completa
            unidades_vendidas = cant_solicitada
            demanda_no_atendida = 0
            self.inventario.disminuir_stock(cod, cant_solicitada)
        else:
            # Rama No: Vender unidades disponibles, descontar stock y registrar faltante
            unidades_vendidas = stock_actual
            demanda_no_atendida = round(cant_solicitada - stock_actual, 2)
            if unidades_vendidas > 0:
                self.inventario.disminuir_stock(cod, unidades_vendidas)

        # Diagrama B - Proceso: Actualizar demanda del período: d = vendidas + no atendidas
        demanda_total = round(unidades_vendidas + demanda_no_atendida, 2)

        # Diagrama B - Salida: Guardar el registro en la lista de ventas del inventario compartido
        nuevo_id = len(self.inventario.ventas) + 1
        registro = {}
        registro["id"] = nuevo_id
        registro["codigo"] = cod
        registro["tipo_medida"] = producto.tipo_medida
        registro["solicitadas"] = cant_solicitada
        registro["vendidas"] = unidades_vendidas
        registro["no_atendidas"] = demanda_no_atendida
        registro["demanda_total"] = demanda_total

        self.inventario.ventas.append(registro)
        self.inventario.guardar()

        return registro
