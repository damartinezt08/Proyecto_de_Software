
from src.inventario import Inventario


class ModuloPronostico:
    def __init__(self, inventario: Inventario):
        # Importar inventario compartido
        self.inventario = inventario

    def calcular_reabastecimiento(self, codigo, dias_cobertura_X=15, dias_entrega_L=3):
        cod = str(codigo).strip().upper()
        producto = self.inventario.buscar_producto(cod)

       
        # Demanda esperada diaria (Venta promedio)
        # Sumamos con un for las ventas del producto
        
        suma_ventas = 0
        total_ventas = 0
        for v in self.inventario.ventas:
            if v["codigo"] == cod:
                suma_ventas = suma_ventas + v["demanda_total"]
                total_ventas = total_ventas + 1

        if total_ventas > 0:
            venta_diaria = round(suma_ventas / total_ventas, 2)
        else:
            # Si no hay ventas, asumimos 1 unidad base
            venta_diaria = 1.0

       
        # [Diagrama C - PASO 2]: Calcular Stock Mínimo (Alerta de reorden)
        # Lo que se vende mientras llega el camión + 2 días de colchón

        demanda_espera = venta_diaria * dias_entrega_L
        colchon_seguridad = venta_diaria * 2
        stock_minimo = demanda_espera + colchon_seguridad


        # Calcular Stock Máximo (Meta para X días)

        stock_maximo = venta_diaria * dias_cobertura_X
        if stock_maximo < stock_minimo + 5:
            stock_maximo = stock_minimo + 5

        # Si el producto es entero redondear a entero; si es peso a decimales
        if producto.tipo_medida == "entero":
            stock_minimo = int(round(stock_minimo))
            stock_maximo = int(round(stock_maximo))
        else:
            stock_minimo = round(stock_minimo, 2)
            stock_maximo = round(stock_maximo, 2)

       
        #  Regla de decisión de reabastecimiento
        # Sumamos los pedidos en camino con un for
        
        en_camino = 0
        for p in self.inventario.pedidos_pendientes:
            if p["codigo"] == cod:
                en_camino = en_camino + p["cantidad_pedida"]

        stock_total_disponible = round(producto.stock + en_camino, 2)

        # [¿Stock disponible <= Stock Mínimo?
        if stock_total_disponible <= stock_minimo:
            # Rama si: Generar alerta y calcular cantidad sugerida Q
            alerta_reorden = True
            diferencia = stock_maximo - stock_total_disponible
            if producto.tipo_medida == "entero":
                cantidad_a_pedir = int(round(diferencia))
            else:
                cantidad_a_pedir = round(diferencia, 2)
        else:
            # Rama no: Sin acción, stock suficiente
            alerta_reorden = False
            cantidad_a_pedir = 0

        # Costo económico estimado de la compra
        costo_estimado = round(cantidad_a_pedir * producto.costo, 2)

        # Alerta y orden sugerida para el comprador
        resultado = {}
        resultado["codigo"] = producto.codigo
        resultado["nombre"] = producto.nombre
        resultado["tipo_medida"] = producto.tipo_medida
        resultado["stock_bodega"] = producto.stock
        resultado["pedidos_en_camino"] = en_camino
        resultado["stock_disponible"] = stock_total_disponible
        resultado["venta_diaria"] = venta_diaria
        resultado["stock_minimo"] = stock_minimo
        resultado["stock_maximo"] = stock_maximo
        resultado["alerta_reorden"] = alerta_reorden
        resultado["cantidad_a_pedir"] = cantidad_a_pedir
        resultado["costo_estimado"] = costo_estimado
        return resultado