"""
Creado con Python3 y PyQt5
Finite Machine Simulator(FSM) de la figura 4.2
Libro Algorithms, Languages, Automata, and Compilers
"""

import sys # Para usar la interfaz
from PyQt5.QtWidgets import QApplication # Para usar la interfaz
from interfaz import gui #gui de la interfaz
from interfaz2 import ventana_dos #ventana 2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = gui()
    gui.show()
    gui2 = ventana_dos()
    gui2.show()
    sys.exit(app.exec_())