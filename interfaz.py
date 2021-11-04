from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

from time import sleep

#Segunda ventana
from about_the_autor import Dialog

class gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Interfaz')
        
        self.btn1 = QPushButton('Menu Principal', self)
        self.btn1.move(50, 50)
        self.btn1.clicked.connect(self.menu_principal)
        
        self.show()


    def menu_principal(self):
        print('Estas en menu_principal')
        self.btn1.hide()

        self.newgameoption = QPushButton('Juego Nuevo',self)
        self.newgameoption.move(50,50)

        self.aboutautors = QPushButton('Acerca de los autores', self)
        self.aboutautors.move(50,100)
        self.aboutautors.clicked.connect(self.about_autors)

        self.gameload = QPushButton('Cargar Juego', self)
        self.gameload.move(50,150)

        self.tableofhonor = QPushButton('Tabla de Honor', self)
        self.tableofhonor.move(50,200)

        self.exit = QPushButton('Salir', self)
        self.exit.clicked.connect(self.salir)
        self.exit.move(50,250)

        self.newgameoption.show()
        self.aboutautors.show()
        self.gameload.show()
        self.tableofhonor.show()
        self.exit.show()
    
    def about_autors(self):
        print('Estas en about_autors')
        
        dialog = Dialog(self)
        dialog.show()

    def salir(self):
        print('Estas en salir')
        self.close()
        

