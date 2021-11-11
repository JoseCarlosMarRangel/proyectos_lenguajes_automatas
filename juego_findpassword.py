from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel


class Dialog4(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog4, self).__init__(*args, **kwargs)
        self.setWindowTitle("JUEGO DE BUSCAR CONTRAEÑA")
        self.setFixedSize(400, 400)
        self.ui()

    def ui(self):
        self.label = QLabel(self)
        self.label.setText("JUEGO DE BUSCAR CONTRAEÑA")
        self.label.move(50, 50)
        self.regresar = QtWidgets.QPushButton("Regresar", self)
        self.regresar.clicked.connect(self.cerrar)
        self.regresar.move(150, 300)

    def cerrar(self):
        self.close()