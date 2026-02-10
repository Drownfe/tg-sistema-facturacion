# Bitácora de avances (Trabajo de Grado)

## Semana 1
- Se creó el repositorio del Trabajo de Grado y se configuró rama `main`.
- Se definió la estructura base del proyecto (docs/src/tests).
- Se redactó la propuesta v0.
- Se redactaron requisitos v0 (funcionales y no funcionales).

- Reunión con el asesor: aval del proyecto y definición de seguimiento semanal (viernes 2:00–2:30 pm).
- Ajuste de alcance aprobado: el proyecto se limita a módulos de Clientes, Productos/Servicios y Facturación (con exportación a PDF).
- Se actualizó la documentación (propuesta, requisitos, arquitectura y modelo de datos) para reflejar el alcance reducido.
- Se envió correo a API Trabajo de Grado solicitando envío de propuesta a jurados.

## Pendiente (próximos pasos)
- Ajustar título, alcance y cronograma según lineamientos del asesor.
- Definir arquitectura v0 (capas/módulos) y modelo de datos v0.

## Semana 2
Fecha: 2026-02-10 (martes)
- Se implementó módulo Productos/Servicios: tabla productos, repo CRUD con precio_cliente, precio_entidad (default 0), notas, cálculo automático de profit.
- Se agregó vista Products con buscador + modales New/Edit/Delete + profit en tabla.
- Se corrigió duplicado de commit (reset/force-with-lease).