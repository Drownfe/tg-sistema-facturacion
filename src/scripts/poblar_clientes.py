from __future__ import annotations

from src.data.db import init_db
from src.data.clientes_repo import Cliente, crear_cliente


def main() -> None:
    init_db()

    clientes = [
        # nombre_cliente, nombre_empresa, street, line2, city, state, zipcode, phone, email
        ("Juan Hernandez", "Pastelito LLC", "7401 NW 36th St", "Suite 120", "Miami", "FL", "33166", "3055551123", "juan@pastelito.com"),
        ("Maria Gomez", "MG Logistics DBA", "1020 Brickell Ave", None, "Miami", "FL", "33131", "3055552211", "maria@mglogistics.com"),

        ("Carlos Rivera", "Rivera Transport", "1 World Trade Center", "Floor 67", "New York", "NY", "10007", "2125553344", "carlos@riveratransport.com"),
        ("Ana Lopez", "AL Freight", "233 S Wacker Dr", "Suite 5400", "Chicago", "IL", "60606", "3125550101", "ana@alfreight.com"),
        ("Diego Martinez", "DM Trucking", "600 Congress Ave", None, "Austin", "TX", "78701", "5125557788", "diego@dmtrucking.com"),
        ("Sofia Perez", "SP Dispatch", "1600 Amphitheatre Pkwy", None, "Mountain View", "CA", "94043", "6505550202", "sofia@spdispatch.com"),
        ("Luis Torres", "Torres Hauling", "401 N Broad St", "Unit 12B", "Philadelphia", "PA", "19108", "2155559988", "luis@torreshauling.com"),
        ("Valentina Ruiz", "VR Cargo", "100 Peachtree St NW", "Apt 2105", "Atlanta", "GA", "30303", "4045554400", "valentina@vrcargo.com"),
        ("Mateo Castillo", "Castillo Express", "700 14th St", "Suite 300", "Denver", "CO", "80202", "3035555533", "mateo@castilloexpress.com"),
        ("Isabella Diaz", "IDB Services DBA", "500 Boylston St", None, "Boston", "MA", "02116", "6175551212", "isabella@idbservices.com"),

        ("Andres Molina", "Molina Logistics", "201 S Tryon St", "Floor 10", "Charlotte", "NC", "28202", "7045558899", "andres@molinallc.com"),
        ("Camila Soto", "Soto Freight", "50 S 16th St", None, "Phoenix", "AZ", "85004", "6025556677", "camila@sotofreight.com"),
        ("Sebastian Vega", "Vega Transport", "200 Public Square", "Suite 2300", "Cleveland", "OH", "44114", "2165553030", "sebastian@vegatransport.com"),
        ("Daniela Romero", "Romero Dispatch", "701 Fifth Ave", "Suite 4200", "Seattle", "WA", "98104", "2065559090", "daniela@romerodispatch.com"),
        ("Nicolas Rios", "Rios Trucking DBA", "600 E Las Olas Blvd", None, "Fort Lauderdale", "FL", "33301", "9545554141", "nicolas@riostrucking.com"),
        ("Laura Herrera", "Herrera Cargo", "1 E Broward Blvd", "Ste 1500", "Fort Lauderdale", "FL", "33301", "9545555151", "laura@herreracargo.com"),

        ("Santiago Alvarez", "Alvarez Hauling", "1500 Market St", "Suite 3500", "Philadelphia", "PA", "19102", "2675552323", "santiago@alvarezhauling.com"),
        ("Paula Navarro", "Navarro Logistics", "1201 3rd Ave", None, "San Diego", "CA", "92101", "6195554545", "paula@navarrologistics.com"),
        ("Esteban Cruz", "Cruz Express", "111 S Main St", "Apt 4C", "Salt Lake City", "UT", "84111", "8015557878", "esteban@cruzexpress.com"),
        ("Juliana Rojas", "Rojas Transport LLC", "650 Poydras St", "Suite 2600", "New Orleans", "LA", "70130", "5045556767", "juliana@rojasttransport.com"),
    ]

    creados = 0
    for c in clientes:
        try:
            crear_cliente(
                Cliente(
                    id=None,
                    nombre_cliente=c[0],
                    nombre_empresa=c[1],
                    direccion_calle=c[2],
                    direccion_linea2=c[3],
                    ciudad=c[4],
                    estado=c[5],
                    zipcode=c[6],
                    telefono=c[7],
                    email=c[8],
                )
            )
            creados += 1
        except Exception as e:
            print(f"[SKIP] {c[0]} / {c[1]} -> {e}")

    print(f"Listo. Clientes creados: {creados}")


if __name__ == "__main__":
    main()
