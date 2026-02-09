from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QLabel
)
from PySide6.QtWidgets import QDialog
from src.data.clientes_repo import (
    Cliente, listar_clientes, crear_cliente, actualizar_cliente, eliminar_cliente
)
from src.ui.clientes_dialog import ClienteDialog


class ClientesWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Header
        self.title = QLabel("Clients")
        self.title.setStyleSheet("font-size: 18px; font-weight: 700;")

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search by name / company / phone / email...")

        self.btn_new = QPushButton("New Client")
        self.btn_edit = QPushButton("Edit")
        self.btn_delete = QPushButton("Delete")

        top = QHBoxLayout()
        top.addWidget(self.title)
        top.addStretch()
        top.addWidget(self.search, 3)
        top.addWidget(self.btn_new)
        top.addWidget(self.btn_edit)
        top.addWidget(self.btn_delete)

        # Table
        self.table = QTableWidget(0, 10)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Company/DBA", "Street", "Line 2",
            "City", "State", "Zip", "Phone", "Email"
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

        # Events
        self.btn_new.clicked.connect(self.on_new)
        self.btn_edit.clicked.connect(self.on_edit)
        self.btn_delete.clicked.connect(self.on_delete)
        self.search.textChanged.connect(self.filtrar_tabla)

        self.refrescar_tabla()

    def refrescar_tabla(self) -> None:
        clientes = listar_clientes()
        self.table.setRowCount(0)

        for c in clientes:
            row = self.table.rowCount()
            self.table.insertRow(row)

            values = [
                str(c.id or ""),
                c.nombre_cliente,
                c.nombre_empresa,
                c.direccion_calle,
                c.direccion_linea2 or "",
                c.ciudad,
                c.estado,
                c.zipcode,
                c.telefono,
                c.email,
            ]
            for col, val in enumerate(values):
                item = QTableWidgetItem(val)
                if col == 0:
                    item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, col, item)

        self.table.resizeColumnsToContents()
        self.filtrar_tabla(self.search.text())

    def _get_selected_cliente(self) -> Cliente | None:
        row = self.table.currentRow()
        if row < 0:
            return None
        try:
            cliente_id = int(self.table.item(row, 0).text())
        except Exception:
            return None

        return Cliente(
            id=cliente_id,
            nombre_cliente=self.table.item(row, 1).text(),
            nombre_empresa=self.table.item(row, 2).text(),
            direccion_calle=self.table.item(row, 3).text(),
            direccion_linea2=self.table.item(row, 4).text() or None,
            ciudad=self.table.item(row, 5).text(),
            estado=self.table.item(row, 6).text(),
            zipcode=self.table.item(row, 7).text(),
            telefono=self.table.item(row, 8).text(),
            email=self.table.item(row, 9).text(),
        )

    def on_new(self) -> None:
        dlg = ClienteDialog(self, None)
        if dlg.exec() == QDialog.Accepted:
            try:
                crear_cliente(dlg.get_cliente())
                self.refrescar_tabla()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def on_edit(self) -> None:
        c = self._get_selected_cliente()
        if not c:
            QMessageBox.information(self, "Info", "Select a client to edit.")
            return

        dlg = ClienteDialog(self, c)
        if dlg.exec() == QDialog.Accepted:
            try:
                actualizar_cliente(dlg.get_cliente())
                self.refrescar_tabla()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

    def on_delete(self) -> None:
        c = self._get_selected_cliente()
        if not c or c.id is None:
            QMessageBox.information(self, "Info", "Select a client to delete.")
            return

        resp = QMessageBox.question(self, "Confirm", "Delete selected client?")
        if resp != QMessageBox.Yes:
            return

        try:
            eliminar_cliente(c.id)
            self.refrescar_tabla()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def filtrar_tabla(self, text: str) -> None:
        q = (text or "").strip().lower()

        for row in range(self.table.rowCount()):
            # Name, Company, Phone, Email
            values = [
                self.table.item(row, 1).text(),
                self.table.item(row, 2).text(),
                self.table.item(row, 8).text(),
                self.table.item(row, 9).text(),
            ]
            hay = " ".join(values).lower()
            self.table.setRowHidden(row, q not in hay)
