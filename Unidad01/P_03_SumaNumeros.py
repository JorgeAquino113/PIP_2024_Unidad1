import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_03_SumaNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.txt_sumar.clicked.connect(self.sumar)
        self.txt_resultado.setEnabled(False)

    def sumar(self):
        A = int(self.txt_A.text())
        B = int(self.txt_B.text())
        r = A + B
        self.txt_resultado.setText(str(r))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())