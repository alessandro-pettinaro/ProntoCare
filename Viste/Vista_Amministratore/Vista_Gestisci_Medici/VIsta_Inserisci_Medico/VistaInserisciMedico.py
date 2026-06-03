import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox

from Personale.Medico import Medico
from Personale.Infermiere import Infermiere
class VistaInserisciMedico(QWidget):
    def __init__(self,callback):
        super(VistaInserisciMedico,self).__init__()
        self.callback=callback
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Medici/VIsta_Inserisci_Medico/VistaRegistrazioneMedico.ui', self)
        self.ButtonRegistra.clicked.connect(self.aggiungi_medico)
        self.ButtonAnnulla.clicked.connect(self.close)
        pixmap = QPixmap("Viste/Vista_Amministratore/IconaMedico.png")
        self.LogoMedici.setPixmap(pixmap)

    def aggiungi_medico(self):

        nome = str(self.LineEdit_Nome.text())
        cognome = str(self.LineEdit_Cognome.text())
        cf = str(self.LineEdit_CodiceFiscale.text())
        username = str(self.LineEdit_Username.text())
        password = str(self.LineEdit_Password.text())
        sesso = str(self.comboBox.currentText())
        dataDiNascita = str(self.dateEdit.text())
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
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
                with open('Dati_Sistema/Medici.pickle', 'rb') as f:
                    medici = dict(pickle.load(f))
                    if(medici.get(cf,None)):
                        QMessageBox.critical(self, 'Errore', 'Medico gia registrato ')
                        return

        medico = Medico()
        infermiere=Infermiere()
        if medico.ricerca_Medico_username(username)!=None or infermiere.ricerca_Infermiere_username(username)!=None or username=="admin":
            QMessageBox.critical(self, 'Errore', 'Sciegliere un altro username perchè questo è gia in uso  ')
            return
        medico.aggiungi_Medico(nome, cognome, cf, "medico", username, password,sesso,dataDiNascita)
        self.callback()
        self.close()