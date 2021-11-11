from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel


class Dialog3(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog3, self).__init__(*args, **kwargs)
        self.setWindowTitle("JUEGO DE DARDOS")
        self.setFixedSize(400, 400)
        self.ui()

    def ui(self):
        self.label = QLabel(self)
        self.label.setText("JUEGO DE DARDOS")
        self.label.move(50, 50)
        self.regresar = QtWidgets.QPushButton("Regresar", self)
        self.regresar.clicked.connect(self.cerrar)
        self.regresar.move(150, 300)

    def cerrar(self):
        self.close()