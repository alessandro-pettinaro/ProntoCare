import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import QWidget, QMessageBox

from Personale.Infermiere import Infermiere
from Personale.Medico import Medico


class VistaInserisciInfermieri(QWidget):
    def __init__(self,callback):
        super(VistaInserisciInfermieri,self).__init__()
        self.callback=callback
        pixmap = QPixmap("Viste/Vista_Amministratore/IconaInfermiere.png")
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Infermieri/Vista_Inserisci_Infermiere/VistaMenuRegistra.ui', self)
        self.ButtonRegistra.clicked.connect(self.aggiungi_Infermieri)
        self.ButtonAnnulla.clicked.connect(self.close)
        self.LogoInfermieri.setPixmap(pixmap)

    def aggiungi_Infermieri(self):

        nome = str(self.LineEdit_Nome.text())
        cognome = str(self.LineEdit_Cognome.text())
        cf = str(self.LineEdit_CodiceFiscale.text())
        username = str(self.LineEdit_Username.text())
        password = str(self.LineEdit_Password.text())
        sesso=str(self.comboBox.currentText())
        dataDiNascita=str(self.dateEdit.text())

        if len(nome) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Nome')
            return
        if len(cognome) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Cognome')
            return
        if len(cf) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci CoficeFiscle')
            return
        if len(username) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Username')
            return
        if len(password) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Password')
            return
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
                with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                    infermieri = dict(pickle.load(f))
                    if(infermieri.get(cf,None)):
                        QMessageBox.critical(self, 'Errore', 'Infermiere gia registrato ')
                        return

        infermiere = Infermiere()
        medico=Medico()
        if infermiere.ricerca_Infermiere_username(username)!=None or medico.ricerca_Medico_username(username) != None or username=="admin":
            QMessageBox.critical(self, 'Errore', 'Sciegliere un altro username perchè questo è gia in uso  ')
            return

        infermiere.aggiungi_Infermiere(nome, cognome, cf, "infermiere", username, password,dataDiNascita,sesso)
        self.callback()
        self.close()





