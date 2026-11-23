
import os
import sys

# Conectar con los módulos del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from inventario import Inventario
from ventas import ModuloVentas
from compras import ModuloCompras
from pronostico import ModuloPronostico


def nuevo_inventario():
    """Crea un inventario de prueba con 2 productos para no alterar los datos reales."""
    if os.path.exists("test_temp.json"):
        os.remove("test_temp.json")
    inv = Inventario("test_temp.json")
    inv.registrar_producto("MAR-01", "Martillo", 10.0, 6.0, 10, "entero")
    inv.registrar_producto("CEM-01", "Cemento", 9.0, 6.5, 30.0, "peso")
    return inv


def limpiar():
    """Borra el archivo temporal al finalizar cada prueba."""
    if os.path.exists("test_temp.json"):
        os.remove("test_temp.json")


# PRUEBA 1: VENTA CON FALTA DE STOCK

def test_1_venta_con_quiebre():
    """Verifica que una venta sin suficiente stock no deje números negativos."""
    inv = nuevo_inventario()
    ventas = ModuloVentas(inv)

    # El cliente pide 15 martillos pero solo tenemos 10
    resultado = ventas.registrar_venta("MAR-01", 15)

    # Comprobamos que vendió 10, anotó 5 no atendidas y el stock quedó en 0
    assert resultado["vendidas"] == 10
    assert resultado["no_atendidas"] == 5
    assert inv.consultar_stock("MAR-01") == 0
    limpiar()

# PRUEBA 2: Rechazo de decimales en productos enteros 

def test_2_rechaza_decimales_en_entero():
    """Verifica que no se puedan vender fracciones de martillos como 1.5."""
    inv = nuevo_inventario()
    ventas = ModuloVentas(inv)

    hubo_error = False
    try:
        # Intentar vender 1.5 martillos debe generar un error
        ventas.registrar_venta("MAR-01", 1.5)
    except Exception:
        hubo_error = True

    # Comprobamos que efectivamente se haya bloqueado
    assert hubo_error == True
    limpiar()


# PRUEBA 3: Permite decimales en producto de pesos 

def test_3_permite_decimales_en_peso():
    """Verifica que en cemento sí se puedan vender fracciones como 2.75 kg."""
    inv = nuevo_inventario()
    ventas = ModuloVentas(inv)

    # Vender 2.75 kg de cemento
    resultado = ventas.registrar_venta("CEM-01", 2.75)

    # Comprobamos que vendió los 2.75 y descontó del stock (30 - 2.75 = 27.25)
    assert resultado["vendidas"] == 2.75
    assert inv.consultar_stock("CEM-01") == 27.25
    limpiar()

# PRUEBA 4: Recepcion parcial de compra (FILL RATE)

def test_4_recepcion_parcial_fill_rate():
    """Verifica que al recibir menos de lo pedido calcule el cumplimiento correcto."""
    inv = nuevo_inventario()
    compras = ModuloCompras(inv)

    # Pedimos 20 martillos pero el camión solo nos trajo 15
    orden = compras.ingresar_orden_compra("MAR-01", "Proveedor", 20, 6.0)
    entrega, prom = compras.ingresar_recepcion(orden["id_pedido"], 15, 3)

    # Comprobamos que el cumplimiento sea 75% (15 de 20) y el stock suba a 25
    assert entrega["fill_rate"] == 0.75
    assert inv.consultar_stock("MAR-01") == 25
    limpiar()

# PRUEBA 5: Alerta min-max por stock bajo 

def test_5_alerta_reorden_min_max():
    """Verifica que el modelo active la alerta de compra cuando el stock llega a cero."""
    inv = nuevo_inventario()
    ventas = ModuloVentas(inv)
    pronostico = ModuloPronostico(inv)

    # Vendemos los 10 martillos en 2 ventas de 5 para dejar el stock en 0
    ventas.registrar_venta("MAR-01", 5)
    ventas.registrar_venta("MAR-01", 5)

    # Calculamos para 10 días de cobertura y 3 días de espera
    resultado = pronostico.calcular_reabastecimiento("MAR-01", dias_cobertura_X=10, dias_entrega_L=3)

    # Comprobamos que se encienda la alerta de compra
    assert resultado["alerta_reorden"] == True
    assert resultado["cantidad_a_pedir"] == 50
    limpiar()

# PRUEBA 6: Rechazo de Codigo Duplicado 
def test_6_rechaza_codigo_duplicado():
    """Verifica que el inventario impida registrar un código repetido."""
    inv = nuevo_inventario()

    hubo_error = False
    try:
        # Intentar registrar de nuevo 'MAR-01' debe dar error
        inv.registrar_producto("MAR-01", "Martillo Repetido", 10.0, 6.0, 5)
    except Exception:
        hubo_error = True

    # Comprobamos que el duplicado fue bloqueado
    assert hubo_error == True
    limpiar()


# Compatibilidad con UNITTest

import unittest
class SuitePruebas(unittest.TestCase):
    def test_todas_las_pruebas(self):
        test_1_venta_con_quiebre()
        test_2_rechaza_decimales_en_entero()
        test_3_permite_decimales_en_peso()
        test_4_recepcion_parcial_fill_rate()
        test_5_alerta_reorden_min_max()
        test_6_rechaza_codigo_duplicado()

if __name__ == "__main__":
    print("\nEjecutando pruebas unitarias de FerreStock...")
    test_1_venta_con_quiebre()
    print(" OK Prueba 1: Venta con quiebre de stock")
    test_2_rechaza_decimales_en_entero()
    print(" OK Prueba 2: Rechazo de decimales en enteros")
    test_3_permite_decimales_en_peso()
    print(" OK Prueba 3: Aceptación de decimales en peso")
    test_4_recepcion_parcial_fill_rate()
    print(" OK Prueba 4: Recepción parcial y Fill Rate")
    test_5_alerta_reorden_min_max()
    print(" OK Prueba 5: Alerta de compra Min-Max")
    test_6_rechaza_codigo_duplicado()
    print(" OK Prueba 6: Rechazo de código duplicado")

    print(" TODAS LAS PRUEBAS PASARON AL 100% SIN ERRORES!")
