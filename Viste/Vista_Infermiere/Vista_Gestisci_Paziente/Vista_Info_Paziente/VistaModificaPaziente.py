import os
import pickle
import datetime

from PyQt6 import uic
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox, QWidget
from Paziente.Paziente import Paziente


class VistaModificaPaziente(QWidget):

    def __init__(self,paziente,elimina_callback):
        super(VistaModificaPaziente, self).__init__()
        self.elimina_callback = elimina_callback
        uic.loadUi('Viste/Vista_Infermiere/Vista_Gestisci_Paziente/Vista_Info_Paziente/VistaModificaPazienti.ui', self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Viste/Vista_Infermiere/IconaPazientiom.png")
        self.Back.setPixmap(pixmap)
        self.LogoPazienti.setPixmap(pixmap1)
        info = paziente.get_Info_Paziente()
        self.LineEdit_Nome.setText(str(info['nome']))
        self.LineEdit_Cognome.setText(str(info['cognome']))
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
        self.LineEdit_CittaDiNascita.setText(str(info['luogoDiNascita']))
        self.LineEdit_CodiceFiscale.setText(str(info['cf']))
        self.LineEdit_Residenza.setText(str(info['residenza']))
        self.LineEdit_Cellulare.setText(str(info['telefono']))
        self.ButtonSalva.clicked.connect(lambda:self.go_save_data(paziente))
        self.ButtonAnnulla.clicked.connect(self.close)

    def go_save_data(self,paziente):
        a=paziente.get_Info_Paziente
        nome = str(self.LineEdit_Nome.text())
        cognome = str(self.LineEdit_Cognome.text())
        sesso = str(self.comboBox.currentText())
        dataDiNascita = str(self.dateEdit.text())
        luogoDiNascita = str(self.LineEdit_CittaDiNascita.text())
        cf = str(self.LineEdit_CodiceFiscale.text())
        residenza = str(self.LineEdit_Residenza.text())
        telefono = str(self.LineEdit_Cellulare.text())

        if len(nome) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Nome')
            return
        if len(cognome) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Cognome')
            return
        if len(cf) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci CoficeFiscle')
            return
        if len(luogoDiNascita) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Luogo Di Nascita')
            return
        if len(sesso) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Sesso')
            return
        if len(telefono) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Numero Di Telefono')
            return
        if len(residenza) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Residenza')
            return
        try:
            datetime.datetime.strptime(dataDiNascita, '%d/%m/%Y')
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene la data')
            return

        paziente.rimuovi_Paziente()
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                pazienti = dict(pickle.load(f))
                if (pazienti.get(cf, None)):
                    QMessageBox.critical(self, 'Errore', 'Paziente già registrato ')
        pazientp=Paziente()
        pazientp.aggiungi_Paziente(nome, cognome, cf,dataDiNascita,luogoDiNascita,sesso,telefono,residenza)
        self.elimina_callback()
        self.close()

    def go_back(self):
        self.close()
