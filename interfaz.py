from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *

from time import sleep

#Segunda ventana
from about_the_autor import Dialog
from table_of_honor import Dialog2
from juego_dardos import Dialog3
from juego_findpassword import Dialog4
from guardar_juego import Dialog5

class gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0, 0, 500, 500)
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
        self.newgameoption.clicked.connect(self.new_game)

        self.aboutautors = QPushButton('Acerca de los autores', self)
        self.aboutautors.move(50,100)
        self.aboutautors.clicked.connect(self.about_autors)

        self.gameload = QPushButton('Cargar Juego', self)
        self.gameload.move(50,150)
        self.gameload.clicked.connect(self.load_game)

        self.tableofhonor = QPushButton('Tabla de Honor', self)
        self.tableofhonor.move(50,200)
        self.tableofhonor.clicked.connect(self.table_honor)

        self.exit = QPushButton('Salir', self)
        self.exit.clicked.connect(self.salir)
        self.exit.move(50,250)

        self.newgameoption.show()
        self.aboutautors.show()
        self.gameload.show()
        self.tableofhonor.show()
        self.exit.show()
        
        #cosas de juego nuevo
        self.label1 = QLabel('Game', self)
        self.label1.move(50,50)
        self.label1.hide()
        self.darts = QPushButton('Dardos', self)
        self.darts.move(50,100)
        self.darts.clicked.connect(self.Dardos)
        self.darts.hide()
        self.victoria = QPushButton('Victoria', self)
        self.victoria.move(50,150)
        self.victoria.clicked.connect(self.metodo_victoria)
        self.victoria.hide()
        self.derrota = QPushButton('Derrota', self)
        self.derrota.move(50,200)
        self.derrota.clicked.connect(self.metodo_derrota)
        self.derrota.hide()
        self.find_password = QPushButton('Encontrar la contraseña', self)
        self.find_password.move(50,250)
        self.find_password.clicked.connect(self.buscar_contrasena)
        self.find_password.hide()
        self.guardar = QPushButton('Guardar', self)
        self.guardar.move(50,350)
        self.guardar.clicked.connect(self.save_data)
        self.guardar.hide()
        
        #cargar juego
        self.regresar_cargar_juego = QPushButton('Regresar', self)
        self.regresar_cargar_juego.move(50,300)
        self.regresar_cargar_juego.clicked.connect(self.regresar_menu_princial)
        self.regresar_cargar_juego.hide()
        self.label = QLabel(self)
        self.label.setText('Cargar Juego')
        self.label.move(100, 50)
        self.label.hide()
        
        #Guardar juego
        self.label2 = QLabel('GUARDAR JUEGO', self)
        self.label2.move(50,50)
        self.label2.hide()
        self.men_guardar_juego = QPushButton('Guardar', self)
        self.men_guardar_juego.move(50,250)
        self.men_guardar_juego.clicked.connect(self.mensaje_savedata)
        self.men_guardar_juego.hide()
        self.back_to_juego = QPushButton('regresar al juego',self)
        self.back_to_juego.move(50,200)
        self.back_to_juego.clicked.connect(self.volver_juego)
        self.back_to_juego.hide()
        
    
    def about_autors(self):
        print('Estas en acerca de los autores')
        dialog = Dialog(self)
        dialog.show()
        
    def table_honor(self):
        print('Estas en tabla de honor')
        dialog2 = Dialog2(self)
        dialog2.show()
        
    def load_game(self):
        print('Estas en cargar juego')
        self.btn1.hide()
        self.newgameoption.hide()
        self.aboutautors.hide()
        self.gameload.hide()
        self.tableofhonor.hide()
        self.exit.hide()
        self.label1.show()
        self.darts.show()
        self.victoria.show()
        self.derrota.show()
        self.find_password.show()
        self.guardar.show()
        self.regresar_cargar_juego.show()
        self.label.show()
        self.label2.hide()
        
    def regresar_menu_princial(self):
        self.label1.hide()
        self.darts.hide()
        self.victoria.hide()
        self.derrota.hide()
        self.find_password.hide()
        self.regresar_cargar_juego.hide()
        self.label.hide()
        self.guardar.hide()
        self.label2.hide()
        self.menu_principal()
        
        
    def new_game(self):
        print('Estas en juego nuevo')
        self.btn1.hide()
        self.newgameoption.hide()
        self.aboutautors.hide()
        self.gameload.hide()
        self.tableofhonor.hide()
        self.exit.hide()
        self.men_guardar_juego.hide()
        self.back_to_juego.hide()
        self.label2.hide()
        
        self.label1.show()
        self.darts.show()
        self.victoria.show()
        self.derrota.show()
        self.find_password.show()
        self.guardar.show()
        self.regresar_cargar_juego.show()
        
    def Dardos(self):
        print('Estas en Dardos')
        dialog3 = Dialog3(self)
        dialog3.show()
        
    def buscar_contrasena(self):
        print('Estas en encontrar la contraseña')
        dialog4 = Dialog4(self)
        dialog4.show()
        
    def metodo_victoria(self):
        print('Estas en Victoria')
        self.regresar_menu_princial()
    
    def metodo_derrota(self):
        print('Estas en Derrota')
        self.regresar_menu_princial()
        
    def save_data(self):
        print('Estas en guardar')
        self.label1.hide()
        self.darts.hide()
        self.victoria.hide()
        self.derrota.hide()
        self.find_password.hide()
        self.guardar.hide()
        self.label2.show()
        self.label.hide()
        self.men_guardar_juego.show()
        self.back_to_juego.show()
        
    def mensaje_savedata(self):
        dialog5 = Dialog5(self)
        dialog5.show()
        
    def volver_juego(self):
        print('Volver al juego')
        self.new_game()
        
    
    def salir(self):
        print('Estas en salir')
        self.close()
        

