from src.data.db import init_db
from src.data.clientes_repo import listar_clientes
from src.data.productos_repo import listar_productos, Producto, crear_producto
from src.data.facturas_repo import crear_factura, agregar_item, obtener_factura, listar_items


def main() -> None:
    init_db()

    clientes = listar_clientes()
    if not clientes:
        print("No hay clientes. Corre poblar_clientes primero.")
        return

    productos = listar_productos()
    if not productos:
        crear_producto(Producto(id=None, nombre="Service Fee", precio_cliente=50, precio_entidad=0, notas="Demo"))
        productos = listar_productos()

    cliente = clientes[0]
    factura_id = crear_factura(cliente_id=cliente.id, notas="Factura demo")
    print("Factura creada:", factura_id)

    p1 = productos[0]
    agregar_item(factura_id, p1.id, cantidad=1, precio_unitario=p1.precio_cliente, descripcion=p1.nombre)

    factura = obtener_factura(factura_id)
    items = listar_items(factura_id)

    print("Factura:", factura)
    for it in items:
        print("Item:", it)


if __name__ == "__main__":
    main()
