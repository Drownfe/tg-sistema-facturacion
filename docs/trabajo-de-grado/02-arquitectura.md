# Arquitectura v0 – Sistema de Facturación (App de escritorio)

## 1. Enfoque general
La solución se plantea como una aplicación de escritorio con persistencia local, organizada por módulos para facilitar mantenimiento y pruebas.

## 2. Componentes principales (v0)
- **UI (Presentación):** pantallas y formularios para clientes, productos/servicios, facturación, historial y reportes.
- **Servicios / Lógica de negocio:** validaciones, cálculo de totales, reglas de factura, generación de reportes.
- **Datos / Persistencia:** acceso a base de datos local (CRUD y consultas).
- **Exportación PDF:** generación de documentos (facturas) con formato estándar.

## 3. Flujo principal (v0)
1. Usuario registra/selecciona cliente.
2. Usuario registra/selecciona productos/servicios.
3. Usuario crea factura, agrega ítems, valida y calcula totales.
4. Usuario exporta la factura a PDF.
5. El sistema guarda la factura para consulta en historial.

## 4. Decisiones iniciales
- Persistencia local para operación simple y sin dependencia de internet.
- Separación por módulos para soportar evolución por sprints.
- Documentación y pruebas como parte del proceso de entrega.

## 5. Riesgos y mitigación (v0)
- **Alcance crezca demasiado:** definir límites (sin facturación electrónica/DIAN).
- **Datos sensibles:** usar datos de prueba o anonimización si aplica.
- **Tiempo limitado:** priorizar flujo principal (factura + PDF + historial).
