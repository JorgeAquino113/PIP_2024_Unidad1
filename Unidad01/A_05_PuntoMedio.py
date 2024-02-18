import math
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "A_05_PuntoMedio.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_Calcular.clicked.connect(self.calcular)

    def calcular(self):
        punto1 = []
        punto2 = []
        punto1 = float(self.txtx.text())
        punto1 = float(self.txtx2.text())
        punto2 = float(self.txty.text())
        punto2 = float(self.txty2.text())
        xMedia = (punto1[0] + punto2[0]) / 2
        yMedia = (punto1[1] + punto2[1]) / 2
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText("({0}, {1}".format(xMedia, yMedia))
        messageBox.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())