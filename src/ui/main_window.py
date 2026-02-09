from __future__ import annotations

from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget
from src.app.settings import APP_TITLE
from src.ui.sidebar import Sidebar
from src.ui.pages import ClientsPage, ProductsPage, InvoicesPage


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(APP_TITLE)

        self.sidebar = Sidebar()
        self.stack = QStackedWidget()

        self.page_clients = ClientsPage()
        self.page_products = ProductsPage()
        self.page_invoices = InvoicesPage()

        self.stack.addWidget(self.page_clients)   # index 0
        self.stack.addWidget(self.page_products)  # index 1
        self.stack.addWidget(self.page_invoices)  # index 2

        root = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack, 1)

        root.setLayout(layout)
        self.setCentralWidget(root)

        # Navegación
        self.sidebar.btn_clients.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.sidebar.btn_products.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.sidebar.btn_invoices.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        # Página inicial
        self.stack.setCurrentIndex(0)
