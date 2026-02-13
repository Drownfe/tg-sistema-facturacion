from src.data.db import init_db
from src.data.productos_repo import Producto, crear_producto


def main() -> None:
    init_db()

    productos = [
        Producto(None, "USDOT Registration", 250.00, 60.00, "Requiere datos carrier, EIN y dirección."),
        Producto(None, "BOC-3 Filing", 40.00, 0.00, "Formulario BOC-3. Normalmente sin costo entidad."),
        Producto(None, "UCR (Unified Carrier Registration)", 120.00, 30.00, "Depende del tamaño de flota. Validar año."),
        Producto(None, "MC Authority (Filing base)", 450.00, 300.00, "Incluye filing inicial. Requiere info del carrier."),
        Producto(None, "SCAC Code", 95.00, 0.00, "Código SCAC para freight. Tiempo 1–3 días hábiles."),
        Producto(None, "IFTA Setup", 180.00, 0.00, "Registro IFTA (setup). Requiere base state y docs."),
        Producto(None, "IRP Registration (setup)", 220.00, 0.00, "Placas IRP. Requiere VIN, weights y jurisdicciones."),
        Producto(None, "2290 Heavy Vehicle Tax (Filing)", 85.00, 0.00, "Filing 2290. Requiere VIN y periodo."),
        Producto(None, "Biennial Update (MCS-150)", 55.00, 0.00, "Actualización bienal MCS-150."),
        Producto(None, "Drug & Alcohol Program Enrollment", 150.00, 50.00, "Inscripción programa D&A. Depende del proveedor."),
    ]

    creados = 0
    for p in productos:
        try:
            crear_producto(p)
            creados += 1
        except Exception as e:
            print("No se pudo crear:", p.nombre, "-", e)

    print(f"Productos insertados: {creados}/10")


if __name__ == "__main__":
    main()
