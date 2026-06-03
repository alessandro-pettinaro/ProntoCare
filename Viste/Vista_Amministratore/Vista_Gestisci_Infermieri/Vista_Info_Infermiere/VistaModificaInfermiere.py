import os
import pickle

from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from Personale.Infermiere import Infermiere
class VistaModificaInfermiere(QWidget):
    def __init__(self,infermiere,elimina_callback):
        super(VistaModificaInfermiere, self).__init__()
        self.elimina_callback = elimina_callback
        pixmap = QPixmap("Viste/Vista_Amministratore/IconaInfermiere.png")
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Infermieri/Vista_Info_Infermiere/vista_infermiere_modifica.ui', self)
        info = infermiere.get_Info_Infermiere()
        self.LogoInfermieri.setPixmap(pixmap)
        self.LineEdit_Nome.setText(str(info['nome']))
        self.LineEdit_Cognome.setText(str(info['cognome']))
        self.LineEdit_CodiceFiscale.setText(str(info['cf']))
        self.LineEdit_Username.setText(str(info['username']))
        self.LineEdit_Password.setText(str(info['password']))
        self.anno=info['dataDiNascita'].split("/")[2]
        self.mese = info['dataDiNascita'].split("/")[1]
        self.giorno=info['dataDiNascita'].split("/")[0]
        d = QDate(int(self.anno),int(self.mese),int(self.giorno))
        self.dateEdit.setDate(d)
        if str(info['sesso'])=="Donna":
            self.comboBox.clear()
            self.comboBox.addItems(['Donna', 'Uomo','Altro...'])
        if str(info['sesso'])=="Altro...":
            self.comboBox.clear()
            self.comboBox.addItems(['Altro...', 'Uomo','Donna' ])

        self.ButtonSalva.clicked.connect(lambda:self.go_save_data(infermiere))
        self.ButtonAnnulla.clicked.connect(self.close)

    def go_save_data(self,infermiere):
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
        infermiere.rimuovi_Infermiere()
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermieri = dict(pickle.load(f))
                if (infermieri.get(cf, None)):
                    QMessageBox.critical(self, 'Errore', 'Infermiere gia registrato -_-')

        infermierep = Infermiere()
        infermierep.aggiungi_Infermiere(nome, cognome, cf, "infermiere", username, password,dataDiNascita,sesso)
        self.elimina_callback()
        self.close()

    def go_back(self):
        self.close()
