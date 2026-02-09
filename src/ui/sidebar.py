from __future__ import annotations

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QSizePolicy
from src.app.settings import COMPANY_DISPLAY_NAME


class Sidebar(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(240)

        self.title = QLabel("Billing System")
        self.title.setStyleSheet("font-size: 16px; font-weight: 700; padding: 12px;")

        self.company = QLabel(COMPANY_DISPLAY_NAME)
        self.company.setWordWrap(True)
        self.company.setStyleSheet("padding: 0 12px 12px 12px; color: #bdbdbd;")

        self.btn_clients = QPushButton("Clients")
        self.btn_products = QPushButton("Products")
        self.btn_invoices = QPushButton("Invoices")

        for b in (self.btn_clients, self.btn_products, self.btn_invoices):
            b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            b.setFixedHeight(44)

        layout = QVBoxLayout()
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(10)

        layout.addWidget(self.title)
        layout.addWidget(self.company)
        layout.addSpacing(10)
        layout.addWidget(self.btn_clients)
        layout.addWidget(self.btn_products)
        layout.addWidget(self.btn_invoices)
        layout.addStretch()

        self.setLayout(layout)
