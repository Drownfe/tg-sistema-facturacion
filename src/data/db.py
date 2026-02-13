from __future__ import annotations

import sqlite3
from pathlib import Path

DB_FILENAME = "tg_facturacion.db"


def get_repo_root() -> Path:
    # src/data/db.py -> parents[2] apunta a la raíz del repo
    return Path(__file__).resolve().parents[2]


def get_app_data_dir() -> Path:
    """
    Carpeta donde guardamos la DB en desarrollo (raíz/data).
    Luego, si quieres, la movemos a Documents/AppData para producción.
    """
    data_dir = get_repo_root() / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_connection() -> sqlite3.Connection:
    db_path = get_app_data_dir() / DB_FILENAME
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """
    Crea tablas mínimas si no existen.
    """
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                nombre_cliente  TEXT NOT NULL,
                nombre_empresa  TEXT NOT NULL,

                direccion_calle TEXT NOT NULL,
                direccion_linea2 TEXT,

                ciudad          TEXT NOT NULL,
                estado          TEXT NOT NULL,
                zipcode         TEXT NOT NULL,

                telefono        TEXT NOT NULL,
                email           TEXT NOT NULL,

                creado_en TEXT NOT NULL DEFAULT (datetime('now'))
            );
            """
        )
        conn.commit()

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                notas TEXT,
                precio_cliente REAL NOT NULL,
                precio_entidad REAL NOT NULL DEFAULT 0,
                creado_en TEXT NOT NULL DEFAULT (datetime('now'))
            );
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS facturas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                fecha TEXT NOT NULL DEFAULT (date('now')),
                notas TEXT,

                subtotal REAL NOT NULL DEFAULT 0,
                discount REAL NOT NULL DEFAULT 0,
                agent_fee REAL NOT NULL DEFAULT 0,
                support_fee REAL NOT NULL DEFAULT 0,
                total REAL NOT NULL DEFAULT 0,

                creado_en TEXT NOT NULL DEFAULT (datetime('now')),
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            );
            """
        )


        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS factura_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                factura_id INTEGER NOT NULL,
                producto_id INTEGER NOT NULL,
                descripcion TEXT,
                cantidad REAL NOT NULL DEFAULT 1,
                precio_unitario REAL NOT NULL,
                total_linea REAL NOT NULL,
                FOREIGN KEY (factura_id) REFERENCES facturas(id),
                FOREIGN KEY (producto_id) REFERENCES productos(id)
            );
            """
        )


