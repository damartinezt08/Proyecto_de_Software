# FerreStock: Sistema Inteligente de Inventario y Reabastecimiento

Sistema modular en Python para la gestión de compras, ventas, inventario y reabastecimiento en ferreterías. Desarrollado con Programación Orientada a Objetos (POO), manejo de excepciones y persistencia en un archivo JSON único compartido.

---

## 1. Cómo Ejecutar la Aplicación

Para iniciar el sistema interactivo en consola:

```bash
python main.py
```

El sistema cargará de inmediato el catálogo precargado y mostrará el menú principal con las 7 operaciones:
1. Registrar nuevo producto (categorías: entero o peso).
2. Ver catálogo y existencias en bodega.
3. Registrar venta (con captura de demanda no atendida en caso de quiebre).
4. Crear orden de compra al proveedor (mercadería en tránsito).
5. Recibir pedido (actualización de stock, cálculo de Lead Time $L$ y Fill Rate).
6. Pronóstico y Reabastecimiento con el modelo Mínimo - Máximo (Min-Max).
7. Salir.

---

## 2. Cómo Ejecutar las Pruebas Unitarias

El archivo ejecutable de pruebas se encuentra en `tests/test_ferrestock.py`. Se puede ejecutar con cualquiera de los siguientes comandos:

### Opción A: Con el módulo estándar de Python (`unittest`)
```bash
python -m unittest tests/test_ferrestock.py
```

### Opción B: Ejecución directa del script
```bash
python tests/test_ferrestock.py
```

### Opción C: Con `pytest` (si está instalado en el entorno)
```bash
pytest tests/test_ferrestock.py
```

---

## 3. Casos de Borde Cubiertos por las Pruebas (Tests)

El script de pruebas unitarias contiene **6 pruebas automáticas** que pasan al **100%**, cubriendo los casos de borde del cálculo central:

1. **Venta con quiebre de stock (`test_venta_con_quiebre_de_stock`):**
   * *Caso de borde:* El cliente solicita más unidades de las disponibles en bodega.
   * *Verificación:* Vende únicamente las unidades en existencia, registra la diferencia como demanda no atendida y asegura que el stock nunca baje de cero.
2. **Rechazo de decimales en categoría entero (`test_categoria_entero_rechaza_decimales`):**
   * *Caso de borde:* Se intenta vender o registrar una fracción (ej. 1.5 martillos).
   * *Verificación:* Lanza una excepción inmediata impidiendo que se guarden números no enteros en productos por unidad.
3. **Aceptación de decimales en categoría peso (`test_categoria_peso_permite_decimales`):**
   * *Caso de borde:* Transacciones con números con decimales (ej. 2.75 kg de cemento).
   * *Verificación:* Procesa la venta con precisión flotante y descuenta exactamente la fracción del stock.
4. **Recepción parcial de compras y Fill Rate (`test_recepcion_parcial_calcula_fill_rate`):**
   * *Caso de borde:* El proveedor entrega menos unidades de las pedidas (ej. 15 de 20).
   * *Verificación:* Calcula el Fill Rate exacto ($75\%$), suma al inventario solo lo recibido y retira el pedido de la lista de tránsito.
5. **Activación de alerta en modelo Min-Max (`test_pronostico_min_max_activa_alerta`):**
   * *Caso de borde:* El inventario disponible cae por debajo o igual al Stock Mínimo.
   * *Verificación:* Enciende la bandera de alerta y calcula la cantidad sugerida de compra $Q$ para restaurar las existencias hasta el Stock Máximo.
6. **Validación de código duplicado (`test_registro_rechaza_codigo_duplicado`):**
   * *Caso de borde:* Intento de registrar un código que ya existe en el inventario.
   * *Verificación:* Bloquea la creación del producto garantizando la integridad de los datos.

---

## 4. Datos de Ejemplo Precargados

El archivo `inventario.json` cuenta con **21 registros precargados** de productos reales de ferretería para comprobar el funcionamiento inmediato de todas las opciones del sistema:

* **Categoría Peso (Materiales a granel, kilos y libras):** Cemento Gris 42.5kg, Cal Hidratada 20kg, Arena de Río, Grava Triturada, Clavo Corriente 2.5 pulg, Clavo para Concreto 2 pulg, Alambre de Amarre.
* **Categoría Entero (Herramientas, pinturas y fontanería):** Martillo de Uña, Combo de 4lb, Pala Redonda, Pala Cuadrada, Carretilla 5.5 pies³, Serrucho 20 pulg, Pintura Blanca Látex, Pintura Anticorrosiva, Brocha 3 pulg, Tubos PVC 1/2 y 2 pulg, Cinta Métrica, Alicate Universal y Juego de Desarmadores.
* **Historial inicial:** Incluye registros de ventas y compras completadas para que el Módulo C (Pronóstico Min-Max) pueda calcular promedios reales desde la primera ejecución.

---

## 5. Bitácora de Transparencia Técnica y Auditoría de IA

En cumplimiento con el sílabo del curso, el repositorio cuenta con un registro formal de transparencia técnica disponible en el archivo:
📄 **[Bitácora de Transparencia Técnica](docs/bitacora_transparencia.md)** (`docs/bitacora_transparencia.md`)

### Resumen del Registro de Transparencia:
* **Asistencia de IA:** Se utilizó Inteligencia Artificial como copiloto para la estructuración de la lógica base de los módulos (Inventario, Ventas, Compras, Pronóstico Min-Max) y la suite de pruebas unitarias (`tests/test_ferrestock.py`).
* **Auditoría de Sintaxis por el Equipo:** Se auditaron las respuestas iniciales de la IA y se descartó toda sintaxis avanzada (como `with`, operadores ternarios y compresiones de listas) para asegurar un código 100% de nivel principiante, legible y defendible.
* **Auditoría de Arquitectura:** Se rechazó la creación de múltiples archivos JSON y se obligó a unificar los datos en un solo archivo compartido (`inventario.json`).
* **Auditoría del Modelo Matemático:** Se sustituyeron modelos abstractos (Monte Carlo / Newsvendor) por el modelo Mínimo-Máximo, justificando la decisión por practicidad operativa y claridad expositiva.
* **Validación de Tests:** Se realizaron pruebas de falla forzada y comprobaciones automatizadas que garantizan una tasa de éxito del 100%.
