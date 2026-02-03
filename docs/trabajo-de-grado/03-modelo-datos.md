# Modelo de datos v0 – Sistema de Facturación

## 1. Entidades principales
- **Cliente**
- **Producto/Servicio**
- **Factura**
- **DetalleFactura (ítems de la factura)**

## 2. Campos sugeridos (v0)

### Cliente
- id (PK)
- nombre
- documento (NIT/CC) (opcional)
- teléfono (opcional)
- email (opcional)
- dirección (opcional)
- creado_en

### ProductoServicio
- id (PK)
- nombre
- descripción (opcional)
- precio_base (opcional)
- activo
- creado_en

### Factura
- id (PK)
- número_factura (único, legible)
- cliente_id (FK → Cliente.id)
- fecha
- subtotal
- total
- observaciones (opcional)
- creado_en

### DetalleFactura
- id (PK)
- factura_id (FK → Factura.id)
- producto_id (FK → ProductoServicio.id) (opcional si se permite ítem libre)
- descripción_item
- cantidad
- precio_unitario
- total_linea

## 3. Relaciones (v0)
- Cliente 1 ─── N Factura  
- Factura 1 ─── N DetalleFactura  
- ProductoServicio 1 ─── N DetalleFactura (si aplica)

## 4. Notas de alcance
- El modelo se mantiene simple para priorizar el flujo principal.
- Se puede extender a futuro con usuarios/roles, impuestos, estados de factura, etc.
