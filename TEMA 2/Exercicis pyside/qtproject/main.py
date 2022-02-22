import sys
import sqlite3
import matplotlib.pyplot as plt

from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QLineEdit, QPushButton, QWidget, QFormLayout, QTableWidget,
    QTableWidgetItem, QHeaderView, QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView

from riotwatcher import LolWatcher

# golbal variables
api_key = 'RGAPI-49e69781-eb0b-451b-8a86-67c2450e0266'
watcher = LolWatcher(api_key)
my_region = 'EUW1'
con = sqlite3.connect('base.db')
cursor = con.cursor()


# Finestra principal , se compon principalment de una tabla ficat en un form layout asi definim les variales noms i
# winrates que mes tard plenarem en funcions
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
        self.winrates = ""

        # Implementació del toolbar , principalement son qPushButtons i labels , tambe estan les connexions a les
        # funcions que estan mes endavent
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        self.cosa = QLineEdit()
        nom = QLabel("SoloqChallengue2")
        nom.setFixedSize(300, 30)
        toolbar.addWidget(nom)
        self.grafica = QPushButton("Grafica")
        self.grafica.setFixedSize(200, 30)
        self.grafica.clicked.connect(self.graficar)
        nom.setFixedSize(200, 30)
        toolbar.addWidget(self.grafica)
        nom2 = QPushButton("Buscador:")
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
        self.botoafegir.clicked.connect(self.afegit)
        self.botocarregar = QPushButton("Carregar")
        self.botocarregar.setFixedSize(70, 30)
        toolbar.addWidget(self.botocarregar)
        self.botocarregar.clicked.connect(self.carregar)
        self.guardar = QPushButton("Guardar")
        self.guardar.setFixedSize(60, 30)
        toolbar.addWidget(self.guardar)
        self.guardar.clicked.connect(self.guardare)

    # llançar browser
    def opgg(self):
        finestra3 = opgg(self.traurenom())
        finestra3.show()

    # llançar grafiques
    def graficar(self):
        window5 = grafica()

    # get noms
    def getnoms(self):
        return self.noms

    # vore la informacio del carregar , basicament es lo mateix pero sense traureu de la base de dates sino de el widget
    def afegit(self):

        if self.cosa.text() == "":
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
            if (self.noms == ""):
                self.noms = (self.noms + nom)

            else:
                self.noms = (self.noms + ",")
                self.noms = (self.noms + nom)
            item1 = QTableWidgetItem(nom)
            item2 = QTableWidgetItem(lstrig['tier'])
            item3 = QTableWidgetItem(lstrig['rank'])
            item4 = QTableWidgetItem(str(lstrig['wins']))
            item5 = QTableWidgetItem(str(lstrig['losses']))
            item6 = QTableWidgetItem(str(round((wins / total) * 100)))
            if self.winrates == "":
                self.winrates = (self.winrates + str(round((wins / total) * 100)))
            else:
                self.winrates = (self.winrates + ",")
                self.winrates = (self.winrates + str(round((wins / total) * 100)))
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
            self.form.setRowCount(self.i)

    # funcio que carregua la base de datos el camp els noms
    def carregar(self):
        for row in con.execute('Select * from usuari WHERE nom="' + AnotherWindow.donar(window2) + '"'):
            j = 0
            noms = row[2]
            nomspartist = noms.split(",")
            print(nomspartist[0])
            print(nomspartist[1])
            print(len(nomspartist))
            while (j < len(nomspartist)):
                self.form.setRowCount(self.i + 1)
                # configuració llibreria riotwatcher
                me = watcher.summoner.by_name(my_region, nomspartist[j])
                my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
                nom = me['name']
                lstrig = my_ranked_stats[0]
                # Faig aço per a traure per a un futur a una variable tots els noms
                if (self.noms == ""):
                    self.noms = (self.noms + nom)

                else:
                    self.noms = (self.noms + ",")
                    self.noms = (self.noms + nom)
                # Agarrar de json que proporciona i ficaro en variables
                wins = int(lstrig['wins'])
                total = int(lstrig['wins']) + int(lstrig['losses'])
                item1 = QTableWidgetItem(me['name'])
                item2 = QTableWidgetItem(lstrig['tier'])
                item3 = QTableWidgetItem(lstrig['rank'])
                item4 = QTableWidgetItem(str(lstrig['wins']))
                item5 = QTableWidgetItem(str(lstrig['losses']))
                item6 = QTableWidgetItem(str((wins / total) * 100))
                # Faig aço per traure a una variable els winrates per a un futur
                if self.winrates == "":
                    self.winrates = self.winrates + str(round((wins / total) * 100))
                else:
                    self.winrates = (self.winrates + ",")
                    self.winrates = (self.winrates + str(round((wins / total) * 100)))
                # ficar en la tabla els elements
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

    # funcio guardar que actualitza el field elsnoms qu es una string on ficare tots els noms que perteneixen al usuari actual
    def guardare(self):
        cursor.execute(
            'UPDATE usuari SET elsnoms="' + self.noms + '" Where nom="' + str(AnotherWindow.donar(window2)) + '"')
        self.nom3.setText("Actualitzat")
        con.commit()

    # funció que se utilitza per passar la string de noms a alrtres finestres
    def traurenom(self):
        nom = self.cosa.text()
        return nom


# Window de el login composat de labels i linedit dins de un vertical layout
class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()
        self.setFixedSize(500, 300)
        self.LOGIN = QLabel("                                                                   LOGIN")
        self.cuentalog = QLabel("Cuenta")
        self.passar = QLabel("")
        self.cuenta = QLineEdit()
        self.cuenta.setFixedSize(100, 100)
        self.passwd = QLineEdit()
        self.botologin = QPushButton()
        self.cuenta.setFixedWidth(100)
        self.cuenta.setFixedHeight(30)
        self.passwd.setFixedWidth(100)
        self.passwd.setFixedHeight(30)
        self.passwd.setEchoMode(QLineEdit.Password)
        self.botologin.setText("LOGIN")
        self.contrasenya = QLabel("Contrasenya")
        self.registra = QPushButton("Registrar")
        layout.addWidget(self.LOGIN)
        layout.addWidget(self.cuentalog)
        layout.addWidget(self.cuenta)
        layout.addWidget(self.contrasenya)
        layout.addWidget(self.passwd)
        layout.addWidget(self.botologin)
        layout.addWidget(self.registra)
        self.setLayout(layout)
        self.registra.clicked.connect(self.registrar)
        self.botologin.clicked.connect(
            lambda checked: self.clickar()
        )

    # funcio de comprobació d login on executa una query recorreguent la tabla usuari
    def clickar(self):
        for row in con.execute('Select * from usuari'):
            if self.cuenta.text() == row[0] and self.passwd.text() == row[1]:
                window.show()
                window2.close()
            else:

                self.botologin.setText("Error en contraseña o cuenta")

    # utilitze aquesta funcio per passar en quin usuari estem a el altra finestra
    def donar(self):
        for row in con.execute('Select * from usuari'):
            if self.cuenta.text() == row[0] and self.passwd.text() == row[1]:
                return self.cuenta.text()
            else:

                self.label.setText("ERROR")

    @staticmethod
    def registrar():
        window4.show()


# Classe que se encarrega de la busqueda a la pagina opgg al apretar el boto busqueda
class opgg(QWidget):
    def __init__(self, nom):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setFixedSize(1300, 1000)
        self.browser = QWebEngineView()
        self.browser.load("https://euw.op.gg/summoners/euw/" + str(nom))
        self.layout.addWidget(self.browser)
        self.browser.show()
        self.setCentralWidget(self.browser)


# Classe que se encarrega de la grafica
class grafica(QWidget):
    def __init__(self):
        super().__init__()
        # recibim noms i winrates en format string , utilitzarem split de , perque ho guarde en una string dividida per comes
        nomsplit = MainWindow.getnoms(window).split(",")
        wr = window.winrates
        winrates = wr.split(",")
        noms = nomsplit
        fig, ax = plt.subplots()
        ax.plot()
        llistadef = []
        i = 0
        # com guarde tots els datos en strings hi han voltes que tinc que reformatejar el string per a que
        # com en este cas desenvoque en un int que servira per a fer la grafica'''
        while (i < len(winrates)):
            llistadef.append(int(winrates[i]))
            i = i + 1
        print(llistadef)
        # Colocamos una etiqueta en la funcio
        ax.set_title('Winrate')
        # Creem la grafica amb els noms que hem rebut junt a els winrates(ints) que hem formateigat.
        plt.bar(noms, llistadef)
        # Fique un nom per el que podrem descarregar el archiu.
        plt.savefig('barras_simple.png')
        # Finalment mostrem la grafica amb el metode show()
        plt.show()


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
        self.cuenta2.setEchoMode(QLineEdit.Password)
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
        cuenta = self.cuenta.text()
        passw = self.cuenta2.text()
        demoment = " "
        cursor.executescript(
            "INSERT INTO usuari(nom,contraseña,elsnoms) VALUES('" + str(cuenta) + "','" + str(passw) + "','" + str(
                demoment) + "')")
        con.commit()
        window4.close()


app = QApplication(sys.argv)
window2 = AnotherWindow()
window = MainWindow()
window4 = regitrar()

window2.show()
app.exec()
