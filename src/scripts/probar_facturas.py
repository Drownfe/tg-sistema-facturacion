from src.data.db import init_db, get_connection
from src.data.clientes_repo import listar_clientes
from src.data.productos_repo import (
    listar_productos,
    Producto,
    crear_producto,
)
from src.data.facturas_repo import (
    crear_factura,
    agregar_item,
    obtener_factura,
    listar_items,
    recalcular_totales,
)


def main() -> None:
    init_db()

    # 1) Necesitamos al menos 1 cliente
    clientes = listar_clientes()
    if not clientes:
        print("No hay clientes. Corre poblar_clientes primero.")
        return
    cliente = clientes[0]

    # 2) Necesitamos al menos 2 productos
    productos = listar_productos()
    if len(productos) < 2:
        crear_producto(Producto(id=None, nombre="USDOT Registration", precio_cliente=250, precio_entidad=60, notas="Demo"))
        crear_producto(Producto(id=None, nombre="BOC-3 Filing", precio_cliente=40, precio_entidad=0, notas="Demo"))
        productos = listar_productos()

    p1, p2 = productos[0], productos[1]

    # 3) Crear factura
    factura_id = crear_factura(cliente_id=cliente.id, notas="Factura demo con fees")
    print("Factura creada:", factura_id)

    # 4) Agregar items (usa precio_cliente como unit price)
    agregar_item(factura_id, p1.id, cantidad=1, precio_unitario=p1.precio_cliente, descripcion=p1.nombre)
    agregar_item(factura_id, p2.id, cantidad=2, precio_unitario=p2.precio_cliente, descripcion=p2.nombre)

    # 5) Setear fees + discount
    discount = 10.00
    agent_fee = 15.00
    support_fee = 5.00

    with get_connection() as conn:
        conn.execute(
            "UPDATE facturas SET discount = ?, agent_fee = ?, support_fee = ? WHERE id = ?",
            (discount, agent_fee, support_fee, factura_id),
        )
        conn.commit()

    # 6) Recalcular totales para que aplique fees/discount
    recalcular_totales(factura_id)

    # 7) Imprimir resultado
    factura = obtener_factura(factura_id)
    items = listar_items(factura_id)

    print("\n--- FACTURA ---")
    print("ID:", factura.id)
    print("Cliente ID:", factura.cliente_id)
    print("Fecha:", factura.fecha)
    print("Subtotal:", factura.subtotal)
    print("Discount:", factura.discount)
    print("Agent fee:", factura.agent_fee)
    print("Support fee:", factura.support_fee)
    print("TOTAL:", factura.total)
    print("Notas:", factura.notas)

    print("\n--- ITEMS ---")
    for it in items:
        print(f"- producto_id={it.producto_id} qty={it.cantidad} unit={it.precio_unitario} total_linea={it.total_linea}")


if __name__ == "__main__":
    main()