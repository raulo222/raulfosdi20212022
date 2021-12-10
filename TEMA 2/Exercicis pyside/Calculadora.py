import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton,QVBoxLayout,QTextEdit


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.generalLayout = QVBoxLayout()
        self.textpantalla = QTextEdit
        self.generalLayout.addWidget(self.textpantalla())
        self.buttons = {}
        self.buttonsLayout = QGridLayout()
        buttons = {'√': (0, 0),
                   'π': (0, 1),
                   '^': (0, 2),
                   '!': (0, 3),
                   'AC': (1, 0),
                   '()': (1, 1),
                   '%': (1, 2),
                   '/': (1, 3),
                   '7': (2, 0),
                   '8': (2, 1),
                   '9': (2, 2),
                   'x': (2, 3),
                   '4': (3, 0),
                   '5': (3, 1),
                   '6': (3, 2),
                   '+': (3, 3),
                   '1': (4, 0),
                   '2': (4, 1),
                   '3': (4, 2),
                   '-': (4, 3),
                   '0': (5, 0),
                   '.': (5, 1),
                   '<-': (5, 2),
                   '=': (5, 3),
                   }
        for btnText, pos in buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setFixedSize(40, 40)
            self.buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
        self.generalLayout.addLayout(self.buttonsLayout)

        widget = QWidget()
        widget.setLayout(self.generalLayout)
        self.setCentralWidget(widget)



    def resultat(self):
            boto=self.sender().textpantalla
            self.textpantalla.text=eval(self.textpantalla.text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
