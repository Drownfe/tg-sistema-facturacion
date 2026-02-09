from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("TG Sistema de Facturación")

        label = QLabel("TG Sistema de Facturación\n(Inicio)", self)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
