# Requisitos v0 – Sistema de Facturación (App de escritorio)

## 1. Requisitos funcionales (RF)

**RF-01. Gestión de clientes**
El sistema debe permitir crear, consultar, editar y eliminar clientes.

**RF-02. Gestión de productos/servicios**
El sistema debe permitir crear, consultar, editar y eliminar productos/servicios.

**RF-03. Creación de factura con ítems**
El sistema debe permitir crear una factura asociando un cliente y agregando ítems (producto/servicio), cantidad y precio unitario.

**RF-04. Cálculo de totales**
El sistema debe calcular subtotal y total de la factura (según reglas definidas).

**RF-05. Exportación de factura a PDF**
El sistema debe permitir exportar la factura a PDF con un formato consistente.
> Nota de alcance: En esta versión del Trabajo de Grado se prioriza el núcleo del sistema (clientes, productos/servicios y factura con exportación a PDF). Funcionalidades como historial detallado, reportes avanzados, inventario completo o renovaciones se consideran fuera de alcance.


## 2. Requisitos no funcionales (RNF)

**RNF-01. Usabilidad**
La interfaz debe ser simple y permitir ejecutar el flujo principal (crear y exportar factura) en pocos pasos.

**RNF-02. Persistencia**
La información debe almacenarse localmente en una base de datos y permanecer disponible entre sesiones.

**RNF-03. Confiabilidad**
El sistema debe validar datos mínimos (campos obligatorios, cantidades y precios válidos) para reducir errores.

**RNF-04. Rendimiento**
Las operaciones básicas (crear factura, buscar, listar) deben responder en tiempo razonable para el uso diario.

**RNF-05. Portabilidad**
La solución debe poder ejecutarse en Windows y contar con una forma de instalación/ejecución clara.

**RNF-06. Mantenibilidad**
El código debe estar organizado por módulos y documentado de forma básica para facilitar cambios.

## 3. Supuestos y restricciones (v0)
- El alcance no incluye facturación electrónica ni integración con DIAN.
- El sistema está orientado a uso interno/operativo.
- La solución se valida con escenarios reales o de prueba, según disponibilidad de datos.
