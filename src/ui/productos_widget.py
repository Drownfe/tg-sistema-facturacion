from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QMessageBox,
    QTableWidget, QTableWidgetItem, QLabel, QDialog
)

from src.data.productos_repo import (
    Producto, listar_productos, crear_producto, actualizar_producto, eliminar_producto
)
from src.ui.productos_dialog import ProductoDialog


class ProductosWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.title = QLabel("Products")
        self.title.setStyleSheet("font-size: 18px; font-weight: 700;")

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search by name / notes...")

        self.btn_new = QPushButton("New Product")
        self.btn_edit = QPushButton("Edit")
        self.btn_delete = QPushButton("Delete")

        top = QHBoxLayout()
        top.addWidget(self.title)
        top.addStretch()
        top.addWidget(self.search, 3)
        top.addWidget(self.btn_new)
        top.addWidget(self.btn_edit)
        top.addWidget(self.btn_delete)

        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Price(Customer)", "Price(Entity)", "Profit", "Notes"
        ])
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)

        root = QVBoxLayout()
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(12)
        root.addLayout(top)
        root.addWidget(self.table, 1)
        self.setLayout(root)

        self.btn_new.clicked.connect(self.on_new)
        self.btn_edit.clicked.connect(self.on_edit)
        self.btn_delete.clicked.connect(self.on_delete)
        self.search.textChanged.connect(self.filtrar_tabla)

        self.refrescar_tabla()

    def refrescar_tabla(self) -> None:
        productos = listar_productos()
        self.table.setRowCount(0)

        for p in productos:
            row = self.table.rowCount()
            self.table.insertRow(row)

            values = [
                str(p.id or ""),
                p.nombre,
                f"{p.precio_cliente:.2f}",
                f"{p.precio_entidad:.2f}",
                f"{p.profit:.2f}",
                (p.notas or ""),
            ]

            for col, val in enumerate(values):
                item = QTableWidgetItem(val)
                if col in (0, 2, 3, 4):
                    item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)

        self.table.resizeColumnsToContents()
        self.filtrar_tabla(self.search.text())

    def _get_selected_producto(self) -> Producto | None:
        row = self.table.currentRow()
        if row < 0:
            return None
        try:
            producto_id = int(self.table.item(row, 0).text())
        except Exception:
            return None

        return Producto(
            id=producto_id,
            nombre=self.table.item(row, 1).text(),
            precio_cliente=float(self.table.item(row, 2).text()),
            precio_entidad=float(self.table.item(row, 3).text()),
            notas=self.table.item(row, 5).text() or None,
        )

    def on_new(self) -> None:
        dlg = ProductoDialog(self, None)
        if dlg.exec() == QDialog.Accepted:
            try:
                crear_producto(dlg.get_producto())
                self.refrescar_tabla()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def on_edit(self) -> None:
        p = self._get_selected_producto()
        if not p:
            QMessageBox.information(self, "Info", "Select a product to edit.")
            return

        dlg = ProductoDialog(self, p)
        if dlg.exec() == QDialog.Accepted:
            try:
                actualizar_producto(dlg.get_producto())
                self.refrescar_tabla()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def on_delete(self) -> None:
        p = self._get_selected_producto()
        if not p or p.id is None:
            QMessageBox.information(self, "Info", "Select a product to delete.")
            return

        resp = QMessageBox.question(self, "Confirm", "Delete selected product?")
        if resp != QMessageBox.Yes:
            return

        try:
            eliminar_producto(p.id)
            self.refrescar_tabla()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def filtrar_tabla(self, text: str) -> None:
        q = (text or "").strip().lower()

        for row in range(self.table.rowCount()):
            name = self.table.item(row, 1).text()
            notes = self.table.item(row, 5).text()
            hay = f"{name} {notes}".lower()
            self.table.setRowHidden(row, q not in hay)
