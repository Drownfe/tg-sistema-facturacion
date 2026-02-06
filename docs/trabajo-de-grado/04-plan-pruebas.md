# Plan de Pruebas v0 – Sistema de Facturación

## 1. Objetivo
Verificar que los módulos del alcance (Clientes, Productos/Servicios y Facturación con exportación a PDF)
funcionan correctamente, validando reglas básicas, manejo de errores y consistencia de datos.

## 2. Alcance de pruebas
Incluye:
- Clientes (CRUD)
- Productos/Servicios (CRUD)
- Factura: crear, validar, calcular totales y exportar a PDF

Fuera de alcance:
- Reportes avanzados
- Facturación electrónica
- Inventario completo

## 3. Enfoque
- Pruebas funcionales manuales por casos de uso.
- Validaciones de datos (campos obligatorios, valores numéricos).
- Evidencias: capturas de pantalla + archivos PDF generados + registro de resultados.

## 4. Criterios de aceptación (v0)
- El sistema permite registrar y consultar clientes y productos/servicios sin errores.
- El sistema permite crear una factura válida y calcular correctamente los totales.
- El PDF se genera correctamente con datos consistentes respecto a la factura.
- Se impide guardar facturas con datos incompletos o inválidos.

## 5. Casos de prueba

### 5.1 Clientes
**CP-C01 – Crear cliente (válido)**
- Precondición: Ninguna
- Pasos: abrir módulo Clientes → crear cliente con nombre válido → guardar
- Resultado esperado: cliente guardado y visible en lista

**CP-C02 – Validación de cliente (campo obligatorio)**
- Pasos: intentar guardar cliente sin nombre
- Resultado esperado: el sistema muestra mensaje de validación y no guarda

**CP-C03 – Editar cliente**
- Pasos: seleccionar cliente existente → modificar teléfono/email → guardar
- Resultado esperado: cambios persistidos

**CP-C04 – Eliminar cliente**
- Pasos: seleccionar cliente → eliminar → confirmar
- Resultado esperado: cliente eliminado y no aparece en lista

### 5.2 Productos/Servicios
**CP-P01 – Crear producto/servicio (válido)**
- Pasos: crear producto con nombre y precio válido → guardar
- Resultado esperado: registro guardado

**CP-P02 – Validación de precio**
- Pasos: intentar guardar producto con precio negativo o no numérico
- Resultado esperado: validación y bloqueo de guardado

**CP-P03 – Editar producto/servicio**
- Pasos: editar nombre/precio → guardar
- Resultado esperado: cambios persistidos

**CP-P04 – Eliminar producto/servicio**
- Pasos: eliminar producto → confirmar
- Resultado esperado: registro eliminado

### 5.3 Facturación y PDF
**CP-F01 – Crear factura (mínima válida)**
- Precondición: existe al menos 1 cliente y 1 producto/servicio
- Pasos: seleccionar cliente → agregar 1 ítem con cantidad y precio → guardar/generar
- Resultado esperado: factura creada y totales correctos

**CP-F02 – Validación de factura sin cliente**
- Pasos: intentar generar factura sin cliente seleccionado
- Resultado esperado: validación y bloqueo

**CP-F03 – Validación de ítems**
- Pasos: agregar ítem con cantidad 0 o negativa
- Resultado esperado: validación y bloqueo

**CP-F04 – Cálculo de totales**
- Pasos: agregar 2+ ítems con cantidades y precios diferentes
- Resultado esperado: subtotal/total correcto (según regla definida)

**CP-F05 – Exportación a PDF**
- Pasos: generar/exportar PDF
- Resultado esperado: se crea un archivo PDF y el contenido coincide con la factura

## 6. Evidencias
- Capturas de pantalla de cada caso de prueba (antes/después).
- Carpeta con PDFs generados (nombres consistentes).
- Registro de resultados (aprobado/fallido + observaciones).

## 7. Trazabilidad (RF → Casos de prueba)
- RF Clientes (CRUD) → CP-C01, CP-C02, CP-C03, CP-C04
- RF Productos/Servicios (CRUD) → CP-P01, CP-P02, CP-P03, CP-P04
- RF Facturación (crear + totales + PDF) → CP-F01, CP-F02, CP-F03, CP-F04, CP-F05