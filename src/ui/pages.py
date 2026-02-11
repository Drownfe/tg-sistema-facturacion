from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

from src.ui.clientes_widget import ClientesWidget
from src.ui.productos_widget import ProductosWidget


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
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(ProductosWidget())
        self.setLayout(layout)


class InvoicesPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        title = QLabel("Invoices")
        title.setStyleSheet("font-size: 18px; font-weight: 700;")

        subtitle = QLabel("En construcción (pendiente lógica de facturación + PDF).")
        subtitle.setStyleSheet("opacity: 0.8;")

        layout = QVBoxLayout()
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(8)
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()
        
        self.setLayout(layout)
