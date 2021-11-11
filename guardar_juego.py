from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel


class Dialog5(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog5, self).__init__(*args, **kwargs)
        self.setWindowTitle("GUARDAR JUEGO")
        self.setFixedSize(400, 400)
        self.ui()

    def ui(self):
        self.label = QLabel(self)
        self.label.setText("JUEGO \n GUARDADO \n EXITOSAMENTE")
        self.label.move(50, 50)
        self.regresar = QtWidgets.QPushButton("Regresar", self)
        self.regresar.clicked.connect(self.cerrar)
        self.regresar.move(150, 300)

    def cerrar(self):
        self.close()