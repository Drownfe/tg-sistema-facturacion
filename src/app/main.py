import sys
from PySide6.QtWidgets import QApplication

from src.ui.main_window import MainWindow
from src.data.db import init_db


def main() -> int:
    app = QApplication(sys.argv)
    init_db()
    window = MainWindow()
    window.resize(900, 600)
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
