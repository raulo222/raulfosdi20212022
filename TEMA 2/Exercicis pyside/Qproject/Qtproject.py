import sys
import sqlite3

import qtmodern.styles
from qtmodern import styles,windows
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QLineEdit, QPushButton, QGridLayout, QWidget, QFormLayout, QListView, QTableWidget, QWidgetItem,
    QTableWidgetItem, QHeaderView, QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt

from riotwatcher import LolWatcher, ApiError
import pandas as pd

# golbal variables
api_key = 'RGAPI-49e69781-eb0b-451b-8a86-67c2450e0266'
watcher = LolWatcher(api_key)
my_region = 'EUW1'
con = sqlite3.connect('base.db')
cursor=con.cursor()


class MainWindow(QMainWindow):

    def __init__(self):
        self.api_key = 'RGAPI-49e69781-eb0b-451b-8a86-67c2450e0266'
        self.watcher = LolWatcher(api_key)
        self.my_region = 'EUW1'
        super(MainWindow, self).__init__()
        self.setFixedSize(1300, 600)
        self.setWindowTitle("  ")
        self.vlaY = QFormLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.vlaY)
        self.setCentralWidget(self.widget)
        self.widget.show()
        self.form = QTableWidget(1, 6)
        self.vlaY.addWidget(self.form)
        self.form.verticalHeader().hide()
        self.form.setHorizontalHeaderLabels(["Nickname", "rango", "divisio", "wins", "derrotes", "winrate"])
        self.form.showFullScreen()
        self.form.columnSpan(1, 1)
        self.form.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.i = 0
        self.form.setRowCount(0)
        self.noms = ""

        # Implementació del toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        self.cosa = QLineEdit()
        nom = QLabel("SoloqChallengue2")
        nom.setFixedSize(500, 30)
        toolbar.addWidget(nom)
        nom2 =  QPushButton("Buscador:")
        nom2.setFixedSize(70, 30)
        nom2.clicked.connect(self.opgg)
        toolbar.addWidget(nom2)
        self.cosa.setFixedSize(290, 30)
        toolbar.addWidget(self.cosa)
        self.botoafegir = QPushButton("Afegir")
        toolbar.addWidget(self.botoafegir)
        self.nom3 = QLabel("")
        self.nom3.setFixedSize(190, 30)
        toolbar.addWidget(self.nom3)
        self.botoafegir.clicked.connect(self.buttonp)
        self.botocarregar = QPushButton("Carregar")
        toolbar.addWidget(self.botocarregar)
        self.botocarregar.clicked.connect(self.carregar)
        self.guardar = QPushButton("Guardar")
        self.guardar.setFixedSize(60, 30)
        toolbar.addWidget(self.guardar)
        self.guardar.clicked.connect(self.guardare)

        # Implementació del toolbar



    def opgg(self):
        finestra3=opgg(self.traurenom())
        finestra3.show()






    def buttonp(self):

        if (self.cosa.text() == ""):
            print("esta vuit")
            self.nom3.setText("esta vuit")
        else:
            print("")
        try:
            me = watcher.summoner.by_name(my_region, self.cosa.text())
            nom = self.cosa.text()
            my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
        except Exception:
            self.nom3.setText("El invocador no existeix")
        try:
            self.form.setRowCount(self.i + 1)
            lstrig = my_ranked_stats[0]
            wins = int(lstrig['wins'])
            total = int(lstrig['wins']) + int(lstrig['losses'])
            if (self.noms==""):
                self.noms=(self.noms+nom)

            else:
                self.noms=(self.noms+",")
                self.noms=(self.noms+nom)
            item1 = QTableWidgetItem(nom)
            item2 = QTableWidgetItem(lstrig['tier'])
            item3 = QTableWidgetItem(lstrig['rank'])
            item4 = QTableWidgetItem(str(lstrig['wins']))
            item5 = QTableWidgetItem(str(lstrig['losses']))
            item6 = QTableWidgetItem(str(round((wins / total) * 100)))
            self.form.setItem(self.i, 0, item1)
            self.form.setItem(self.i, 1, item2)
            self.form.setItem(self.i, 2, item3)
            self.form.setItem(self.i, 3, item4)
            self.form.setItem(self.i, 4, item5)
            self.form.setItem(self.i, 5, item6)
            self.i = self.i + 1
            self.nom3.setText(" Afegit!!")
        except IndexError:
            print("El invocador seleccionat o no a juat ranked o no existeix")
            self.nom3.setText(" El compte no ha juat rankeds")
            self.form.setRowCount(self.i )

    def carregar(self):
        for row in con.execute('Select * from usuari WHERE nom="' + AnotherWindow.donar(window2) + '"'):
            j = 0
            noms = row[2]
            nomspartist = noms.split(",")
            print(nomspartist[0])
            print(nomspartist[1])
            print(len(nomspartist))
            while (j < len(nomspartist)):
                self.form.setRowCount(self.i+1)
                me = watcher.summoner.by_name(my_region, nomspartist[j])
                my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
                nom = me['name']
                lstrig = my_ranked_stats[0]
                if (self.noms == ""):
                    self.noms = (self.noms + nom)

                else:
                    self.noms = (self.noms + ",")
                    self.noms = (self.noms + nom)
                wins = int(lstrig['wins'])
                total = int(lstrig['wins']) + int(lstrig['losses'])
                item1 = QTableWidgetItem(me['name'])
                item2 = QTableWidgetItem(lstrig['tier'])
                item3 = QTableWidgetItem(lstrig['rank'])
                item4 = QTableWidgetItem(str(lstrig['wins']))
                item5 = QTableWidgetItem(str(lstrig['losses']))
                item6 = QTableWidgetItem(str((wins / total) * 100))
                self.form.setItem(self.i, 0, item1)
                self.form.setItem(self.i, 1, item2)
                self.form.setItem(self.i, 2, item3)
                self.form.setItem(self.i, 3, item4)
                self.form.setItem(self.i, 4, item5)
                self.form.setItem(self.i, 5, item6)
                j = j + 1
                self.nom3.setText(" Afegit!!")
                self.i = self.i + 1

        self.botocarregar.setDisabled(True)
    def guardare(self):
        cursor.execute('UPDATE usuari SET elsnoms="'+ self.noms +'" Where nom="'+str(AnotherWindow.donar(window2))+'"')
        self.nom3.setText("Actualitzat")
        con.commit()

    def traurenom(self):
        nom=self.cosa.text()
        return nom



class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setFixedSize(500,300)
        self.label = QLabel("                                                                   LOGIN")
        self.label2 = QLabel("Cuenta")
        self.passar = QLabel("")
        self.cuenta = QLineEdit()
        self.cuenta.setFixedSize(100,100)
        self.cuenta2 = QLineEdit()
        self.boto = QPushButton()
        self.cuenta.setFixedWidth(100)
        self.cuenta.setFixedHeight(30)
        self.cuenta2.setFixedWidth(100)
        self.cuenta2.setFixedHeight(30)
        self.boto.setText("LOGIN")
        self.label3 = QLabel("Contrasenya")
        self.label4 = QPushButton("Registrar")
        self.cuenta2.isHidden()
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.cuenta)
        layout.addWidget(self.label3)
        layout.addWidget(self.cuenta2)
        layout.addWidget(self.boto)
        layout.addWidget(self.label4)
        self.cuenta.text()
        self.setLayout(layout)
        self.label4.clicked.connect(self.registrar)
        self.boto.clicked.connect(
            lambda checked: self.clickar()
        )

    def clickar(self):
        for row in con.execute('Select * from usuari'):
            if self.cuenta.text() == row[0] and self.cuenta2.text() == row[1]:
                window.show()
                window2.close()
            else:

                self.label.setText("ERROR")
    def donar(self):
        for row in con.execute('Select * from usuari'):
            if self.cuenta.text() == row[0] and self.cuenta2.text() == row[1]:
               return self.cuenta.text()
            else:

                self.label.setText("ERROR")
    def registrar(self):
        window4.show()

class opgg(QWidget):
    def __init__(self,nom):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setFixedSize(1300,1000)
        self.browser=QWebEngineView()
        self.browser.load("https://euw.op.gg/summoners/euw/"+str(nom))
        self.layout.addWidget(self.browser)
        self.browser.show()
        self.setCentralWidget(self.browser)
class regitrar(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setFixedSize(500, 300)
        self.label = QLabel("                                                                   REGISTRAR")
        self.label2 = QLabel("Cuenta")
        self.passar = QLabel("")
        self.cuenta = QLineEdit()
        self.cuenta.setFixedSize(300, 100)
        self.cuenta2 = QLineEdit()
        self.boto = QPushButton()
        self.cuenta.setFixedWidth(100)
        self.cuenta.setFixedHeight(30)
        self.cuenta2.setFixedWidth(100)
        self.cuenta2.setFixedHeight(30)
        self.boto.setText("REGISTRAR")
        self.label3 = QLabel("Contrasenya")
        self.cuenta2.isHidden()
        layout.addWidget(self.label)
        layout.addWidget(self.label2)
        layout.addWidget(self.cuenta)
        layout.addWidget(self.label3)
        layout.addWidget(self.cuenta2)
        layout.addWidget(self.boto)
        self.cuenta.text()
        self.setLayout(layout)
        self.boto.clicked.connect(
            lambda checked: self.registrar()
        )
    def registrar(self):
        cuenta=self.cuenta.text()
        passw = self.cuenta2.text()
        demoment=" "
        cursor.executescript("INSERT INTO usuari(nom,contraseña,elsnoms) VALUES('"+str(cuenta)+"','"+str(passw)+"','"+str(demoment)+"')")
        con.commit()
        window4.close()





app = QApplication(sys.argv)
window2 = AnotherWindow()
window = MainWindow()
window4 = regitrar()



qtmodern.styles.dark(app)
window2.show()
app.exec()
