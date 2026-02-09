from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from src.ui.clientes_widget import ClientesWidget


class ClientsPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(ClientesWidget())
        self.setLayout(layout)


class ProductsPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Products (pendiente)")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)


class InvoicesPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Invoices (pendiente)")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)
