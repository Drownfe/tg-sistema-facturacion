from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

from src.data.db import get_connection


@dataclass
class Producto:
    id: Optional[int]
    nombre: str
    precio_cliente: float
    precio_entidad: float = 0.0
    notas: Optional[str] = None

    @property
    def profit(self) -> float:
        return float(self.precio_cliente) - float(self.precio_entidad)


def _validar_producto(p: Producto) -> None:
    if p.nombre is None or not str(p.nombre).strip():
        raise ValueError("El nombre del producto/servicio es obligatorio.")
    p.nombre = p.nombre.strip()

    try:
        p.precio_cliente = float(p.precio_cliente)
    except Exception:
        raise ValueError("El precio al cliente debe ser numérico.")
    if p.precio_cliente <= 0:
        raise ValueError("El precio al cliente debe ser mayor a 0.")

    # Si viene vacío/None -> 0
    if p.precio_entidad is None or str(p.precio_entidad).strip() == "":
        p.precio_entidad = 0.0
    try:
        p.precio_entidad = float(p.precio_entidad)
    except Exception:
        raise ValueError("El precio a entidad debe ser numérico.")
    if p.precio_entidad < 0:
        raise ValueError("El precio a entidad no puede ser negativo.")

    if p.notas is not None:
        p.notas = p.notas.strip() or None


def crear_producto(p: Producto) -> int:
    _validar_producto(p)
    with get_connection() as conn:
        cur = conn.execute(
            """
            INSERT INTO productos (nombre, notas, precio_cliente, precio_entidad)
            VALUES (?, ?, ?, ?)
            """,
            (p.nombre, p.notas, p.precio_cliente, p.precio_entidad),
        )
        conn.commit()
        return int(cur.lastrowid)


def listar_productos() -> List[Producto]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT id, nombre, notas, precio_cliente, precio_entidad
            FROM productos
            ORDER BY id DESC
            """
        ).fetchall()

    return [
        Producto(
            id=row["id"],
            nombre=row["nombre"],
            notas=row["notas"],
            precio_cliente=float(row["precio_cliente"]),
            precio_entidad=float(row["precio_entidad"]),
        )
        for row in rows
    ]


def actualizar_producto(p: Producto) -> None:
    if p.id is None:
        raise ValueError("Para actualizar, el producto debe tener id.")
    _validar_producto(p)

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE productos SET
                nombre = ?,
                notas = ?,
                precio_cliente = ?,
                precio_entidad = ?
            WHERE id = ?
            """,
            (p.nombre, p.notas, p.precio_cliente, p.precio_entidad, p.id),
        )
        conn.commit()


def eliminar_producto(producto_id: int) -> None:
    with get_connection() as conn:
        conn.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conn.commit()
