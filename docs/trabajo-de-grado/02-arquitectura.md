# Arquitectura v0 – Sistema de Facturación (App de escritorio)

## 1. Enfoque general
La solución se plantea como una aplicación de escritorio con persistencia local, organizada por módulos para facilitar mantenimiento y pruebas.

## 2. Componentes principales (v0)
- **UI (Presentación)**: pantallas para Clientes, Productos/Servicios y Facturación.
- **Lógica de negocio**: validaciones y cálculo de totales.
- **Persistencia**: base de datos local (CRUD y consultas mínimas).
- **Exportación PDF**: generación de la factura en PDF con formato estándar.

## 3. Flujo principal (v0)
1. Crear/seleccionar cliente
2. Crear/seleccionar productos/servicios
3. Crear factura (ítems + totales)
4. Exportar PDF
5. Guardar factura (solo si lo manejas como “persistir factura” — sin hablar de historial/reportes)
6. Riesgos

## 4. Decisiones iniciales
- Persistencia local para operación simple y sin dependencia de internet.
- Separación por módulos para soportar evolución por sprints.
- Documentación y pruebas como parte del proceso de entrega.

## 5. Riesgos y mitigación (v0)
- **Alcance crezca demasiado:** definir límites (sin facturación electrónica/DIAN).
- **Datos sensibles:** usar datos de prueba o anonimización si aplica.
- **Tiempo limitado:** priorizar flujo principal (factura + PDF + historial).
