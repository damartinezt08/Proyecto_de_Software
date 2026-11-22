# inventario.py
# Administra los productos y su stock en el archivo inventario.json.

import json
import os

# Objeto Producto 
# artículo en la ferretería.

class Producto:
    def __init__(self, codigo, nombre, precio, costo, stock, tipo_medida="entero"):
        self.codigo = codigo.upper()
        self.nombre = nombre
        self.precio = float(precio)
        self.costo = float(costo)
        self.tipo_medida = tipo_medida  # "entero" (piezas) o "peso" (kilos/libras)

        # Si es peso permite decimales, si es entero solo número entero
        if tipo_medida == "peso":
            self.stock = float(stock)
        else:
            self.stock = int(stock)

    def a_diccionario(self):
        # Convierte los datos a un diccionario básico.
        diccionario = {}
        diccionario["codigo"] = self.codigo
        diccionario["nombre"] = self.nombre
        diccionario["tipo_medida"] = self.tipo_medida
        diccionario["precio"] = self.precio
        diccionario["costo"] = self.costo
        diccionario["stock"] = self.stock
        return diccionario



# 2. Controlador de Inventario 

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}            # { "CODIGO": objeto Producto }
        self.ventas = []               # Lista de ventas
        self.pedidos_pendientes = []   # Lista de compras en camino
        self.entregas_completadas = [] # Lista de compras recibidas
        self.cargar()

    # Diagrama D - Inicio: ¿Existe el archivo de inventario (inventario.json)?
    def cargar(self):
        # Rama Sí: Si el archivo existe, lo abrimos y lo leemos
        if os.path.exists(self.archivo):
            try:
                # 1. Abrir
                archivo_abierto = open(self.archivo, "r", encoding="utf-8")
                # 2. Leer
                datos = json.load(archivo_abierto)
                # 3. Cerrar
                archivo_abierto.close()

                # Cargar los productos usando un for 
                if "productos" in datos:
                    for cod in datos["productos"]:
                        info = datos["productos"][cod]
                        tipo = "entero"
                        if "tipo_medida" in info:
                            tipo = info["tipo_medida"]

                        nuevo = Producto(
                            info["codigo"],
                            info["nombre"],
                            info["precio"],
                            info["costo"],
                            info["stock"],
                            tipo
                        )
                        self.productos[cod] = nuevo

                # Cargar las listas
                if "ventas" in datos:
                    self.ventas = datos["ventas"]
                if "pedidos_pendientes" in datos:
                    self.pedidos_pendientes = datos["pedidos_pendientes"]
                if "entregas_completadas" in datos:
                    self.entregas_completadas = datos["entregas_completadas"]

            except Exception:
                # Rama No: Si el archivo está dañado, avisar e iniciar vacío
                print("AVISO El archivo estaba dañado. Se reinicia vacío.")
                self.guardar()
        else:
            # Rama No: Si no existe, crear el archivo vacío
            self.guardar()

    # Diagrama D: Guardar el inventario en el archivo
    def guardar(self):
        # Convertir productos a diccionario con un for normal
        productos_diccionario = {}
        for cod in self.productos:
            prod = self.productos[cod]
            productos_diccionario[cod] = prod.a_diccionario()

        datos = {}
        datos["productos"] = productos_diccionario
        datos["ventas"] = self.ventas
        datos["pedidos_pendientes"] = self.pedidos_pendientes
        datos["entregas_completadas"] = self.entregas_completadas

        # 1. Abrir
        archivo_abierto = open(self.archivo, "w", encoding="utf-8")
        # 2. Escribir
        json.dump(datos, archivo_abierto, indent=4)
        # 3. Cerrar
        archivo_abierto.close()

    # Diagrama D - Operación 1: Ingresar producto
    def registrar_producto(self, codigo, nombre, precio, costo, stock_inicial, tipo_medida="entero"):
        cod = str(codigo).strip().upper()
        nom = str(nombre).strip()

        if str(tipo_medida).lower() == "peso":
            tipo = "peso"
        else:
            tipo = "entero"

        # Diagrama D - Decisión: ¿Datos válidos?
        if cod == "" or nom == "":
            raise Exception("El código y el nombre no pueden estar vacíos.")

        precio_num = float(precio)
        costo_num = float(costo)
        stock_num = float(stock_inicial)

        if precio_num <= 0 or costo_num <= 0 or stock_num < 0:
            raise Exception("Precio y costo deben ser mayores a 0, y stock no puede ser negativo.")

        # Si es de categoría entero, no puede tener decimales 
        if tipo == "entero":
            if int(stock_num) != stock_num:
                raise Exception("Un producto de categoría 'entero' debe tener stock entero, sin decimales.")

        # Diagrama D - Decisión: ¿El código ya existe en el inventario?
        if cod in self.productos:
            # Rama Si: Error código duplicado
            raise Exception("El código ya existe en el inventario (duplicado).")

        # Rama No: Crear el producto y agregarlo al inventario
        nuevo = Producto(cod, nom, precio_num, costo_num, stock_num, tipo)
        self.productos[cod] = nuevo
        self.guardar()
        return nuevo

    # Diagrama D - Operación 4: Consultar stock y buscar producto
    def buscar_producto(self, codigo):
        cod = str(codigo).strip().upper()
        # Diagrama D - Decisión: ¿El producto existe?
        if cod in self.productos:
            return self.productos[cod]
        else:
            raise Exception("El producto no existe en el inventario.")

    def consultar_stock(self, codigo):
        producto = self.buscar_producto(codigo)
        return producto.stock

    # Diagrama D - Operación 2: Aumentar stock (Módulo A)
    def aumentar_stock(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        cant = float(cantidad)
        if producto.tipo_medida == "entero":
            producto.stock = int(producto.stock + cant)
        else:
            producto.stock = round(producto.stock + cant, 2)
        self.guardar()
        return producto.stock

    # Diagrama D - Operación 3: Disminuir stock (Módulo B)
    def disminuir_stock(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        cant = float(cantidad)
        nuevo_stock = producto.stock - cant
        # Regla del diagrama: sin bajar de 0
        if nuevo_stock < 0:
            nuevo_stock = 0

        if producto.tipo_medida == "entero":
            producto.stock = int(nuevo_stock)
        else:
            producto.stock = round(nuevo_stock, 2)
        self.guardar()
        return producto.stock