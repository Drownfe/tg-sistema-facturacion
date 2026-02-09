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
