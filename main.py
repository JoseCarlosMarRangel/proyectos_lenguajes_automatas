"""
Creado con Python3 y PyQt5
Finite Machine Simulator(FSM) de la figura 4.2
Libro Algorithms, Languages, Automata, and Compilers
"""

import sys # Para usar la interfaz
from PyQt5.QtWidgets import QApplication # Para usar la interfaz
from interfaz import gui #gui de la interfaz

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = gui()
    gui.show()
    sys.exit(app.exec_())