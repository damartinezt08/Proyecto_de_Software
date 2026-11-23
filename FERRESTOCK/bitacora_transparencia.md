# Bitácora de Transparencia Técnica

**Proyecto:** FerreStock  
**Documento:** Registro de uso y auditoría de Inteligencia Artificial

---

## 1. Declaración de Uso de IA
En este proyecto utilizamos Inteligencia Artificial como herramienta de apoyo técnico para agilizar la escritura de código y estructurar pruebas. A continuación se presentan los **3 casos principales** donde se utilizó la IA y la forma en que el equipo auditó y corrigió cada uno:

---

## 2. Los 3 Casos de Asistencia y Auditoría

### Caso 1: Script de Pruebas Unitarias (`tests/test_ferrestock.py`)
* **Qué asistió la IA:**  
  Generó el esqueleto de las pruebas unitarias automatizadas para verificar que las reglas del sistema funcionaran ante casos de borde (quiebres de stock, entregas parciales de compras y validaciones numéricas).
* **Cómo lo auditó y corrigió el equipo:**  
  El equipo auditó el código generado y eliminó clases complejas (`unittest.TestCase`, `self.assertEqual`, `setUp` y `tearDown`). Se reescribieron como 6 funciones simples para principiantes usando la palabra clave `assert` y se ejecutaron en consola (`python tests/test_ferrestock.py`) verificando que pasaran al 100%.

---

### Caso 2: Unificación y Estructura del JSON (`inventario.json`)
* **Qué asistió la IA:**  
  La IA propuso inicialmente crear 3 archivos JSON separados (`inventario.json`, `ventas.json` y `compras.json`).
* **Cómo lo auditó y corrigió el equipo:**  
  El equipo rechazó la idea de múltiples archivos para evitar desorden y ordenó unificar todo en **un único archivo JSON compartido**. Además, se le indicó agregar el campo `"tipo_medida"` para distinguir productos por unidades (`"entero"`, como martillos) de productos a granel (`"peso"`, como cemento o cal), y se precargaron más de 20 productos de prueba.

---

### Caso 3: Diagrama de Flujo y Modelo de Pronóstico (`FerreStock Flujos.md`)
* **Qué asistió la IA:**  
  La IA propuso inicialmente algoritmos de alta complejidad matemática (simulación de Monte Carlo, percentiles estadísticos y nivel de servicio Newsvendor).
* **Cómo lo auditó y corrigió el equipo:**  
  El equipo evaluó la propuesta y concluyó que era innecesariamente difícil de entender y defender en una exposición. Por ello, se corrigió el flujo para adoptar el modelo clásico **Mínimo - Máximo (Min-Max)**. Esto permitió que el diagrama y el archivo `pronostico.py` utilizaran operaciones elementales (venta promedio diaria, stock mínimo de seguridad y meta de stock máximo para $X$ días), asegurando que todo el equipo domine la lógica al 100%.

---

## 3. Conclusión
La IA sirvió como asistente de código base, pero las decisiones de simplificación, la arquitectura de datos compartida y la elección de modelos comprensibles fueron auditadas y dirigidas por los integrantes del equipo.
