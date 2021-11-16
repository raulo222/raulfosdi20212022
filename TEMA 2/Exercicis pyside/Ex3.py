from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(300, 300))
        self.setWindowTitle("Example signals-slots 1")

        pybutton1 = QPushButton('Click', self)
        
        #Connectem la senyal clicked a la ranura button_pressed
        pybutton1.clicked.connect(self.button_pressed)

        pybutton1.resize(100, 100)

        pybutton1.move(100, 100)

    def button_pressed(self):

        print('Click rebut!')

if __name__ == "__main__":
    app = QApplication([])

    mainWin = MainWindow()

    mainWin.show()

    app.exec()
