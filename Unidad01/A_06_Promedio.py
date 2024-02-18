import math
import sys

import numpy
from PyQt5 import uic, QtWidgets
qtCreatorFile = "A_06_Promedio.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_Calcular.clicked.connect(self.calcular)

    def calcular(self):
        calificaciones = []
        calificaciones.append(float(self.txtcalif1.text()))
        calificaciones.append(float(self.txtcalif2.text()))
        calificaciones.append(float(self.txtcalif3.text()))
        calificaciones.append(float(self.txtcalif4.text()))
        calificaciones.append(float(self.txtcalif5.text()))
        promedio = numpy.average(calificaciones)
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(str(promedio))
        messageBox.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())