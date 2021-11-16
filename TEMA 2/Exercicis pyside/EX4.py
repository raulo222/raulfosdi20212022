from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        ample=600
        alt=600
        self.setFixedSize(QSize(ample, alt))
        self.setWindowTitle("Normalitzat")

        self.pybutton = QPushButton('Normalizar', self)
        self.pybutton2 = QPushButton('Maximitzar', self)
        self.pybutton3 = QPushButton('Minimitzar', self)
        # Connectem la senyal clicked a la ranura button_pressed


        self.pybutton.resize(ample/6, ample/6)
        self.pybutton.move(250, 250)
        self.pybutton2.resize(ample / 6, ample / 6)
        self.pybutton2.move(50, 250)
        self.pybutton3.resize(ample/6, ample/6)
        self.pybutton3.move(450, 250)
        self.pybutton3.clicked.connect(self.Minimitzar)
        self.pybutton.clicked.connect(self.Normalitzar)
        self.pybutton2.clicked.connect(self.Ampliar)
    def Minimitzar(self):
        self.setFixedSize(QSize(600, 100))
        self.pybutton3.move(450,0)
        self.pybutton2.move(50, 0)
        self.pybutton.move(250, 0)
        self.pybutton3.setDisabled(True)
        self.pybutton.setDisabled(False)
        self.pybutton2.setDisabled(False)
        self.setWindowTitle("Minimitzat")
    def Normalitzar(self):
        self.setFixedSize(QSize(600, 600))
        self.pybutton.move(250, 250)
        self.pybutton2.move(50, 250)
        self.pybutton3.move(450, 250)
        self.pybutton3.setDisabled(False)
        self.pybutton.setDisabled(True)
        self.pybutton2.setDisabled(False)
        self.setWindowTitle("Normalitzat")
    def Ampliar(self):
        self.setFixedSize(QSize(900, 900))
        self.pybutton2.move(200, 350)
        self.pybutton.move(400, 350)
        self.pybutton3.move(600, 350)
        self.pybutton3.setDisabled(False)
        self.pybutton.setDisabled(False)
        self.pybutton2.setDisabled(True)
        self.setWindowTitle("Maximitzat")

if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()