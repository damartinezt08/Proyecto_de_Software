# FerreStock

Sistema de gestión y control de inventario para ferreterías.

# 1. Descripción del proyecto

FerreStock es un sistema de software diseñado para facilitar la administración de inventarios en ferreterías. Permitirá controlar las entradas y salidas de productos, registrar las ventas y 
analizar el comportamiento de compra de los clientes para identificar el mejor punto de abastecimiento a la hora de comprar.

El objetivo es ayudar a las ferreterías a tomar mejores decisiones de abastecimiento, evitando compras innecesarias, acumulación de productos y desabastecimiento.

## 2. Integrantes

Gerardo Guandique 20265282
Herberth Prieto 20265541
Jorge Valencia 20245115
Diego Martínez 20265411

## 3. Dominio del negocio

Retail (comercio minorista de materiales de construcción, herramientas y artículos de ferretería).

## 4. Problema a resolver

Las ferreterías pueden presentar dificultades para controlar sus inventarios y analizar el comportamiento de compra de sus clientes, lo que provoca errores en el registro de entradas y salidas
de productos y una mala planificación de las compras. La falta de información sobre cuáles productos tienen mayor o menor demanda puede ocasionar compras innecesarias, acumulación de mercancía
con poca rotación, desabastecimiento de productos populares y pérdidas económicas para el negocio.

## 5. Estructura de módulos prevista

- **Módulo de inventario (`inventario.py` / `inventario.json`):** administración de productos (categorías entero y peso), persistencia de datos y control de cantidades disponibles.
- **Módulo de entradas y salidas:** registro de movimientos de mercancía y actualización de stock.
- **Módulo de ventas (`ventas.py`):** registro y seguimiento de las compras realizadas por los clientes, incluyendo demanda atendida y no atendida.
- **Módulo de compras y proveedores (`compras.py`):** control de adquisiciones en tránsito, proveedores, tiempos de entrega (Lead Time) y cumplimiento (Fill Rate).
- **Módulo de análisis de demanda (`pronostico.py`):** identificación de demanda diaria promedio, niveles mínimo y máximo de stock y sugerencias de reabastecimiento.
- **Módulo de usuarios:** administración de empleados y responsables de los movimientos.
- **Menú principal (`main.py`):** orquestación e interacción por consola de los módulos del sistema.

## 6. Declaración de uso de inteligencia artificial

Se ha usado IA en el inventario.json, en el archivo de pronósticos y en el diagrama de flujo


