from __future__ import annotations

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, QTextEdit,
    QHBoxLayout, QPushButton, QMessageBox, QLabel
)

from src.data.productos_repo import Producto


class ProductoDialog(QDialog):
    def __init__(self, parent=None, producto: Producto | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Producto/Servicio")
        self.setModal(True)
        self.resize(540, 360)

        self._producto_id = producto.id if producto else None

        self.in_nombre = QLineEdit()
        self.in_precio_cliente = QLineEdit()
        self.in_precio_entidad = QLineEdit()
        self.in_notas = QTextEdit()
        self.in_notas.setFixedHeight(110)

        self.lbl_profit = QLabel("0.00")

        form = QFormLayout()
        form.addRow("Nombre *", self.in_nombre)
        form.addRow("Precio cliente *", self.in_precio_cliente)
        form.addRow("Precio entidad (default 0)", self.in_precio_entidad)
        form.addRow("Profit (auto)", self.lbl_profit)
        form.addRow("Notas / requisitos", self.in_notas)

        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_guardar = QPushButton("Guardar")

        btns = QHBoxLayout()
        btns.addStretch()
        btns.addWidget(self.btn_cancelar)
        btns.addWidget(self.btn_guardar)

        root = QVBoxLayout()
        root.addLayout(form)
        root.addLayout(btns)
        self.setLayout(root)

        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_guardar.clicked.connect(self._on_guardar)

        self.in_precio_cliente.textChanged.connect(self._actualizar_profit)
        self.in_precio_entidad.textChanged.connect(self._actualizar_profit)

        if producto:
            self._set_producto(producto)
        else:
            self.in_precio_entidad.setText("0")
            self._actualizar_profit()

    def _set_producto(self, p: Producto) -> None:
        self.in_nombre.setText(p.nombre)
        self.in_precio_cliente.setText(str(p.precio_cliente))
        self.in_precio_entidad.setText(str(p.precio_entidad))
        self.in_notas.setPlainText(p.notas or "")
        self.lbl_profit.setText(f"{p.profit:.2f}")

    def _actualizar_profit(self) -> None:
        try:
            pc = float(self.in_precio_cliente.text() or 0)
        except ValueError:
            pc = 0.0
        try:
            pe = float(self.in_precio_entidad.text() or 0)
        except ValueError:
            pe = 0.0
        self.lbl_profit.setText(f"{(pc - pe):.2f}")

    def get_producto(self) -> Producto:
        nombre = self.in_nombre.text()
        notas = self.in_notas.toPlainText() or None
        precio_cliente = float(self.in_precio_cliente.text() or 0)
        # vacío -> 0
        txt_entidad = (self.in_precio_entidad.text() or "").strip()
        precio_entidad = float(txt_entidad) if txt_entidad else 0.0

        return Producto(
            id=self._producto_id,
            nombre=nombre,
            precio_cliente=precio_cliente,
            precio_entidad=precio_entidad,
            notas=notas,
        )

    def _on_guardar(self) -> None:
        if not self.in_nombre.text().strip():
            QMessageBox.warning(self, "Falta información", "El nombre es obligatorio.")
            return

        try:
            float(self.in_precio_cliente.text())
        except ValueError:
            QMessageBox.warning(self, "Falta información", "Precio cliente debe ser numérico.")
            return

        txt_entidad = (self.in_precio_entidad.text() or "").strip()
        if txt_entidad:
            try:
                float(txt_entidad)
            except ValueError:
                QMessageBox.warning(self, "Falta información", "Precio entidad debe ser numérico.")
                return

        self.accept()
