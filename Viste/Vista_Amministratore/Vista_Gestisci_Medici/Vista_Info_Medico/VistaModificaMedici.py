
import os
import pickle

from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox, QDateEdit,QComboBox
from Personale.Medico import Medico

class VistaModificaMedico(QWidget):
    def __init__(self,medico,elimina_callback):
        super(VistaModificaMedico, self).__init__()
        self.elimina_callback = elimina_callback
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Medici/Vista_Info_Medico/VistaModificaMedico.ui', self)
        pixmap = QPixmap("Viste/Vista_Amministratore/IconaMedico.png")
        self.LogoMedici.setPixmap(pixmap)
        info = medico.get_Info_Medico()
        self.LineEdit_Nome.setText(str(info['nome']))
        self.LineEdit_Cognome.setText(str(info['cognome']))
        self.LineEdit_CodiceFiscale.setText(str(info['cf']))
        self.LineEdit_Username.setText(str(info['username']))
        self.LineEdit_Password.setText(str(info['password']))
        self.anno = info['dataDiNascita'].split("/")[2]
        self.mese = info['dataDiNascita'].split("/")[1]
        self.giorno = info['dataDiNascita'].split("/")[0]
        d = QDate(int(self.anno), int(self.mese), int(self.giorno))
        self.dateEdit.setDate(d)
        if str(info['sesso']) == "Donna":
            self.comboBox.clear()
            self.comboBox.addItems(['Donna', 'Uomo', 'Altro...'])
        if str(info['sesso']) == "Altro...":
            self.comboBox.clear()
            self.comboBox.addItems(['Altro...', 'Uomo', 'Donna'])

        self.ButtonSalva.clicked.connect(lambda:self.go_save_data(medico))
        self.ButtonAnnulla.clicked.connect(self.close)

    def go_save_data(self,medico):

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
        medico.rimuovi_Medico()
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle', 'rb') as f:
                infermieri = dict(pickle.load(f))
                if (infermieri.get(cf, None)):
                    QMessageBox.critical(self, 'Errore', 'Infermiere gia registrato ')

        medicop= Medico()
        medicop.aggiungi_Medico(nome, cognome, cf, 'medico', username, password,sesso,dataDiNascita)
        self.elimina_callback()
        self.close()

    def go_back(self):
        self.close()
