from src.data.db import init_db
from src.data.productos_repo import Producto, crear_producto, listar_productos


def main() -> None:
    init_db()

    crear_producto(Producto(id=None, nombre="USDOT Registration", precio_cliente=250, precio_entidad=60, notas="Requiere datos carrier"))
    crear_producto(Producto(id=None, nombre="BOC-3 Filing", precio_cliente=40, precio_entidad=0, notas="Si no hay entidad, queda 0"))
    crear_producto(Producto(id=None, nombre="UCR", precio_cliente=120, precio_entidad=None, notas="None -> 0"))

    for p in listar_productos():
        print(p.id, p.nombre, p.precio_cliente, p.precio_entidad, "profit=", p.profit)


if __name__ == "__main__":
    main()
