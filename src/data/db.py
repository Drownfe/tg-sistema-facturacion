from __future__ import annotations

import os
import sqlite3
from pathlib import Path

DB_FILENAME = "tg_facturacion.db"


def get_app_data_dir() -> Path:
    """
    Carpeta de datos local del proyecto.
    Por ahora se usa /data en el repo para desarrollo.
    (En producción se puede mover a Documents u AppData.)
    """
    base_dir = Path(__file__).resolve().parents[2]  # repo root
    data_dir = base_dir / "data"
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
                nombre TEXT NOT NULL,
                documento TEXT,
                telefono TEXT,
                email TEXT,
                direccion TEXT,
                creado_en TEXT NOT NULL DEFAULT (datetime('now'))
            );
            """
        )
        conn.commit()
