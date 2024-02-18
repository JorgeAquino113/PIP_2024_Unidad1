import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "A_02_IndiceMasaCorporal.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_Calcular.clicked.connect(self.calcular)

    def calcular(self):
        peso = float(self.txt_Peso.text())
        altura = float(self.txt_Altura.text())
        imc = peso / altura**2
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(str(imc))
        messageBox.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())