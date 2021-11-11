from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem


class Dialog2(QDialog):
    def __init__(self, *args, **kwargs):
        super(Dialog2, self).__init__(*args, **kwargs)
        self.setWindowTitle("Tabla de honor")
        self.setFixedSize(400, 400)
        self.ui()

    def ui(self):
        """self.label = QLabel(self)
        self.label.setText(self.textoautor)
        self.label.move(50, 50)"""
        self.regresar = QtWidgets.QPushButton("Regresar", self)
        self.regresar.clicked.connect(self.cerrar)
        self.createTable()
        # Añadir diseño de caja(Box Layout), agregue la tabla al diseño de la caja y agregue el diseño de la caja al widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.layout.addWidget(self.regresar)
        self.setLayout(self.layout) 
        self.show()

    def createTable(self):
       # Crea Tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Jose Carlos Mar Rangel"))
        self.tableWidget.move(0,0)

    def cerrar(self):
        self.close()