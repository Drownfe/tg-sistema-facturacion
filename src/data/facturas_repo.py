from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

from src.data.db import get_connection


@dataclass
class Factura:
    id: Optional[int]
    cliente_id: int
    fecha: str
    subtotal: float
    total: float
    notas: Optional[str] = None


@dataclass
class FacturaItem:
    id: Optional[int]
    factura_id: int
    producto_id: int
    descripcion: Optional[str]
    cantidad: float
    precio_unitario: float
    total_linea: float


def crear_factura(cliente_id: int, notas: Optional[str] = None) -> int:
    if not cliente_id:
        raise ValueError("cliente_id es obligatorio.")

    with get_connection() as conn:
        cur = conn.execute(
            """
            INSERT INTO facturas (cliente_id, notas, subtotal, total)
            VALUES (?, ?, 0, 0)
            """,
            (cliente_id, notas),
        )
        conn.commit()
        return int(cur.lastrowid)


def agregar_item(factura_id: int, producto_id: int, cantidad: float, precio_unitario: float, descripcion: Optional[str] = None) -> int:
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser > 0.")
    if precio_unitario <= 0:
        raise ValueError("El precio unitario debe ser > 0.")

    total_linea = float(cantidad) * float(precio_unitario)

    with get_connection() as conn:
        cur = conn.execute(
            """
            INSERT INTO factura_items (factura_id, producto_id, descripcion, cantidad, precio_unitario, total_linea)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (factura_id, producto_id, descripcion, float(cantidad), float(precio_unitario), total_linea),
        )
        conn.commit()
        recalcular_totales(factura_id)
        return int(cur.lastrowid)


def listar_items(factura_id: int) -> List[FacturaItem]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, factura_id, producto_id, descripcion, cantidad, precio_unitario, total_linea
            FROM factura_items
            WHERE factura_id = ?
            ORDER BY id ASC
            """,
            (factura_id,),
        ).fetchall()

    return [
        FacturaItem(
            id=row["id"],
            factura_id=row["factura_id"],
            producto_id=row["producto_id"],
            descripcion=row["descripcion"],
            cantidad=float(row["cantidad"]),
            precio_unitario=float(row["precio_unitario"]),
            total_linea=float(row["total_linea"]),
        )
        for row in rows
    ]


def recalcular_totales(factura_id: int) -> None:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT COALESCE(SUM(total_linea), 0) AS subtotal FROM factura_items WHERE factura_id = ?",
            (factura_id,),
        ).fetchone()

        subtotal = float(row["subtotal"]) if row else 0.0
        total = subtotal  # por ahora sin impuestos/descuentos (TG básico)

        conn.execute(
            "UPDATE facturas SET subtotal = ?, total = ? WHERE id = ?",
            (subtotal, total, factura_id),
        )
        conn.commit()


def obtener_factura(factura_id: int) -> Factura:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT id, cliente_id, fecha, subtotal, total, notas FROM facturas WHERE id = ?",
            (factura_id,),
        ).fetchone()

    if not row:
        raise ValueError("Factura no encontrada.")

    return Factura(
        id=row["id"],
        cliente_id=row["cliente_id"],
        fecha=row["fecha"],
        subtotal=float(row["subtotal"]),
        total=float(row["total"]),
        notas=row["notas"],
    )
