from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List
import re

from src.data.db import get_connection


@dataclass
class Cliente:
    id: Optional[int]
    nombre_cliente: str
    nombre_empresa: str
    direccion_calle: str
    direccion_linea2: Optional[str]
    ciudad: str
    estado: str
    zipcode: str
    telefono: str
    email: str


def _limpiar(texto: str) -> str:
    return texto.strip()


def _validar_cliente(c: Cliente) -> None:
    # Obligatorios (todos menos linea2)
    obligatorios = {
        "nombre_cliente": c.nombre_cliente,
        "nombre_empresa": c.nombre_empresa,
        "direccion_calle": c.direccion_calle,
        "ciudad": c.ciudad,
        "estado": c.estado,
        "zipcode": c.zipcode,
        "telefono": c.telefono,
        "email": c.email,
    }

    for campo, valor in obligatorios.items():
        if valor is None or not str(valor).strip():
            raise ValueError(f"El campo '{campo}' es obligatorio.")

    # Normalizaciones
    c.nombre_cliente = _limpiar(c.nombre_cliente)
    c.nombre_empresa = _limpiar(c.nombre_empresa)
    c.direccion_calle = _limpiar(c.direccion_calle)
    c.ciudad = _limpiar(c.ciudad)
    c.estado = _limpiar(c.estado).upper()
    c.zipcode = _limpiar(c.zipcode)
    c.telefono = _limpiar(c.telefono)
    c.email = _limpiar(c.email)

    if c.direccion_linea2 is not None:
        c.direccion_linea2 = c.direccion_linea2.strip() or None

    # Validaciones básicas (prácticas, no perfectas)
    if len(c.estado) != 2 or not c.estado.isalpha():
        raise ValueError("El estado debe tener 2 letras (ej: FL, TX).")

    if not re.fullmatch(r"\d{5}", c.zipcode):
        raise ValueError("El zipcode debe tener 5 dígitos (ej: 33166).")

    if "@" not in c.email or "." not in c.email.split("@")[-1]:
        raise ValueError("El email no parece válido.")


def crear_cliente(cliente: Cliente) -> int:
    _validar_cliente(cliente)

    with get_connection() as conn:
        cur = conn.execute(
            """
            INSERT INTO clientes
            (nombre_cliente, nombre_empresa, direccion_calle, direccion_linea2, ciudad, estado, zipcode, telefono, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                cliente.nombre_cliente,
                cliente.nombre_empresa,
                cliente.direccion_calle,
                cliente.direccion_linea2,
                cliente.ciudad,
                cliente.estado,
                cliente.zipcode,
                cliente.telefono,
                cliente.email,
            ),
        )
        conn.commit()
        return int(cur.lastrowid)


def listar_clientes() -> List[Cliente]:
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT
                id, nombre_cliente, nombre_empresa,
                direccion_calle, direccion_linea2,
                ciudad, estado, zipcode,
                telefono, email
            FROM clientes
            ORDER BY id DESC
            """
        ).fetchall()

    return [
        Cliente(
            id=row["id"],
            nombre_cliente=row["nombre_cliente"],
            nombre_empresa=row["nombre_empresa"],
            direccion_calle=row["direccion_calle"],
            direccion_linea2=row["direccion_linea2"],
            ciudad=row["ciudad"],
            estado=row["estado"],
            zipcode=row["zipcode"],
            telefono=row["telefono"],
            email=row["email"],
        )
        for row in rows
    ]


def actualizar_cliente(cliente: Cliente) -> None:
    if cliente.id is None:
        raise ValueError("Para actualizar, el cliente debe tener id.")

    _validar_cliente(cliente)

    with get_connection() as conn:
        conn.execute(
            """
            UPDATE clientes SET
                nombre_cliente = ?,
                nombre_empresa = ?,
                direccion_calle = ?,
                direccion_linea2 = ?,
                ciudad = ?,
                estado = ?,
                zipcode = ?,
                telefono = ?,
                email = ?
            WHERE id = ?
            """,
            (
                cliente.nombre_cliente,
                cliente.nombre_empresa,
                cliente.direccion_calle,
                cliente.direccion_linea2,
                cliente.ciudad,
                cliente.estado,
                cliente.zipcode,
                cliente.telefono,
                cliente.email,
                cliente.id,
            ),
        )
        conn.commit()


def eliminar_cliente(cliente_id: int) -> None:
    with get_connection() as conn:
        conn.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        conn.commit()
