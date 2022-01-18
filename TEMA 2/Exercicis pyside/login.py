import sys
from random import randint

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit
)


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("LOGIN")
        self.label2 = QLabel("Cuenta")
        self.passar = QLabel("")
        self.cuenta = QLineEdit()
        self.cuenta2 = QLineEdit()
        self.boto = QPushButton()
        self.cuenta.setFixedWidth(100)
        self.cuenta.setFixedHeight(30)
        self.cuenta2.setFixedWidth(100)
        self.cuenta2.setFixedHeight(30)
        self.boto.setText("Registrar")
        self.label3 = QLabel("Contrasenya")
        self.cuenta2.isHidden()
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.cuenta)
        layout.addWidget(self.label3)
        layout.addWidget(self.cuenta2)
        layout.addWidget(self.boto)

        self.setLayout(layout)
        self.boto.clicked.connect(
            lambda checked: self.clickar()
        )

    def clickar(self):
        if self.cuenta.text() == "admin" and self.cuenta2.text() == "1234":
            window1.close()
            w.show()
            self.passar.setText("ADMIN")
            return 0
        if self.cuenta.text() == "user" and self.cuenta2.text() == "1234":
            window1.close()
            w.show()
            self.passar.setText("USER")
            return 1
        else:

            self.label.setText("ERROR")


class window2(QMainWindow):
    def __init__(self):
        super().__init__()
        layout2 = QVBoxLayout()
        self.label = QLabel()
        self.label.setText("hola")
        layout2.addWidget(self.label)
        self.setLayout(layout2)
        self.show()


app = QApplication(sys.argv)
w = window2()
window1 = AnotherWindow()
window1.show()
app.exec()
