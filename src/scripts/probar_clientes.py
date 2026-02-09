from src.data.db import init_db
from src.data.clientes_repo import (
    Cliente,
    crear_cliente,
    listar_clientes,
    actualizar_cliente,
    eliminar_cliente,
)


def main() -> None:
    init_db()

    nuevo_id = crear_cliente(
        Cliente(
            id=None,
            nombre_cliente="Juan Felipe Hernandez",
            nombre_empresa="Juan Felipe Hernandez (DBA JH Logistics)",
            direccion_calle="7401 NW 36th St",
            direccion_linea2="Suite 120",
            ciudad="Miami",
            estado="FL",
            zipcode="33166",
            telefono="+1 305-555-1234",
            email="juan@example.com",
        )
    )
    print("Creado:", nuevo_id)

    clientes = listar_clientes()
    print("Listado:", clientes)

    if clientes:
        c = clientes[0]
        c.telefono = "+1 305-555-9999"
        actualizar_cliente(c)
        print("Actualizado:", c.id)

        eliminar_cliente(c.id)
        print("Eliminado:", c.id)


if __name__ == "__main__":
    main()
