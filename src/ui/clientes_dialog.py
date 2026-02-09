from __future__ import annotations

from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QHBoxLayout, QPushButton, QMessageBox

from src.data.clientes_repo import Cliente


class ClienteDialog(QDialog):
    def __init__(self, parent=None, cliente: Cliente | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Cliente")
        self.setModal(True)
        self.resize(520, 420)

        self._cliente_id = cliente.id if cliente else None

        self.in_nombre_cliente = QLineEdit()
        self.in_nombre_empresa = QLineEdit()
        self.in_direccion_calle = QLineEdit()
        self.in_direccion_linea2 = QLineEdit()
        self.in_ciudad = QLineEdit()
        self.in_estado = QLineEdit()
        self.in_zipcode = QLineEdit()
        self.in_telefono = QLineEdit()
        self.in_email = QLineEdit()

        form = QFormLayout()
        form.addRow("Nombre cliente *", self.in_nombre_cliente)
        form.addRow("Nombre empresa/DBA *", self.in_nombre_empresa)
        form.addRow("Dirección (calle) *", self.in_direccion_calle)
        form.addRow("Dirección (línea 2)", self.in_direccion_linea2)
        form.addRow("Ciudad *", self.in_ciudad)
        form.addRow("Estado (2 letras) *", self.in_estado)
        form.addRow("Zipcode (5) *", self.in_zipcode)
        form.addRow("Teléfono *", self.in_telefono)
        form.addRow("Email *", self.in_email)

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

        if cliente:
            self._set_cliente(cliente)

    def _set_cliente(self, c: Cliente) -> None:
        self.in_nombre_cliente.setText(c.nombre_cliente)
        self.in_nombre_empresa.setText(c.nombre_empresa)
        self.in_direccion_calle.setText(c.direccion_calle)
        self.in_direccion_linea2.setText(c.direccion_linea2 or "")
        self.in_ciudad.setText(c.ciudad)
        self.in_estado.setText(c.estado)
        self.in_zipcode.setText(c.zipcode)
        self.in_telefono.setText(c.telefono)
        self.in_email.setText(c.email)

    def get_cliente(self) -> Cliente:
        return Cliente(
            id=self._cliente_id,
            nombre_cliente=self.in_nombre_cliente.text(),
            nombre_empresa=self.in_nombre_empresa.text(),
            direccion_calle=self.in_direccion_calle.text(),
            direccion_linea2=self.in_direccion_linea2.text() or None,
            ciudad=self.in_ciudad.text(),
            estado=self.in_estado.text(),
            zipcode=self.in_zipcode.text(),
            telefono=self.in_telefono.text(),
            email=self.in_email.text(),
        )

    def _on_guardar(self) -> None:
        # Aquí no guardamos en DB, solo validamos mínimo de UI
        c = self.get_cliente()
        if not c.nombre_cliente.strip() or not c.nombre_empresa.strip():
            QMessageBox.warning(self, "Falta información", "Nombre cliente y Nombre empresa/DBA son obligatorios.")
            return
        self.accept()
