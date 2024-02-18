import math
import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "A_8_Calificacion.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_Calcular.clicked.connect(self.calcular)

    def calcular(self):
        calificacion = (float(self.txtCalificacion.text()))
        if calificacion == 10:
            nota = 'A'
        elif calificacion >= 9:
            nota = 'B'
        elif calificacion >=8:
            nota = 'C'
        elif calificacion >= 7:
            nota = 'D'
        elif calificacion >=6:
            nota = 'E'
        else:
            nota = 'F'
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(str(math.factorial(nota)))
        messageBox.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())