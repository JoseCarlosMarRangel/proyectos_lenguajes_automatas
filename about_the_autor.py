from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel


class Dialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Acerca de los autores")
        self.setFixedSize(400, 400)
        self.textoautor = "Autor: Jose Carlos Mar Rangel" + "\n" + "Carnet: 2018020" + "\n" + "Correo:" + "1930082@upv.edu.mx"
        self.ui()

    def ui(self):
        self.label = QLabel(self)
        self.label.setText(self.textoautor)
        self.label.move(50, 50)
        self.regresar = QtWidgets.QPushButton("Regresar", self)
        self.regresar.clicked.connect(self.cerrar)
        self.regresar.move(150, 300)

    def cerrar(self):
        self.close()
        
        