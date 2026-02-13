from src.data.db import get_connection, init_db

def _col_exists(cols, name: str) -> bool:
    return any(c["name"] == name for c in cols)

def main() -> None:
    init_db()  # asegura tablas base

    with get_connection() as conn:
        cols = conn.execute("PRAGMA table_info(facturas);").fetchall()

        if not _col_exists(cols, "discount"):
            conn.execute("ALTER TABLE facturas ADD COLUMN discount REAL NOT NULL DEFAULT 0;")
        if not _col_exists(cols, "agent_fee"):
            conn.execute("ALTER TABLE facturas ADD COLUMN agent_fee REAL NOT NULL DEFAULT 0;")
        if not _col_exists(cols, "support_fee"):
            conn.execute("ALTER TABLE facturas ADD COLUMN support_fee REAL NOT NULL DEFAULT 0;")

        conn.commit()

    print("Migración facturas v2 OK")

if __name__ == "__main__":
    main()
