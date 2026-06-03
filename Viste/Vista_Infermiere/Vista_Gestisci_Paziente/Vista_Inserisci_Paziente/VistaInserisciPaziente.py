import os
import pickle
import datetime
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox

from Paziente.Paziente import Paziente


class VistaInserisciPaziente(QWidget):
    def __init__(self, callback):
        super(VistaInserisciPaziente, self).__init__()
        self.callback = callback
        uic.loadUi('Viste/Vista_Infermiere/Vista_Gestisci_Paziente/Vista_Inserisci_Paziente/VistaRegistraPazienti.ui',self)
        self.ButtonRegistra.clicked.connect(self.aggiungi_Paziente)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Viste/Vista_Infermiere/IconaPazientiom.png")
        self.Back.setPixmap(pixmap)
        self.LogoPazienti.setPixmap(pixmap1)
        self.ButtonAnnulla.clicked.connect(self.close)
    def aggiungi_Paziente(self):
        nome = str(self.LineEdit_Nome.text())
        cognome = str(self.LineEdit_Cognome.text())
        sesso=str(self.comboBox.currentText())
        dataNascita=str(self.dateEdit.text())
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
        if len(sesso) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Sesso')
            return
        if len(luogoDiNascita) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Luogo Di Nascita')
            return
        if len(cf) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci CoficeFiscle')
            return
        if len(residenza) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Residenza')
            return
        if len(telefono) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci  Numero di Telefono')
            return
        try:
            datetime.datetime.strptime(dataNascita, '%d/%m/%Y')
        except:
            QMessageBox.critical(self, 'Errore', 'Controlla bene la data')
            return
        paziente = Paziente()
        if not paziente.verifica_paziente_Registarti(cf):
            QMessageBox.critical(self, 'Errore', 'Paziente è gia presente')
            return
        QMessageBox.critical(self, 'Errore', 'Paziente è gia presente')
        paziente.aggiungi_Paziente(nome, cognome, cf, dataNascita, luogoDiNascita, sesso, telefono, residenza)
        self.callback()
        self.close()
