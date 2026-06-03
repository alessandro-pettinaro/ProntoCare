import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMessageBox, QWidget
from Servizi.Prenotazione import Prenotazione
from Paziente.Paziente import Paziente
import datetime

class VistaInserisciPrenotazione(QWidget):
    def __init__(self,paziente,callback):
        super(VistaInserisciPrenotazione, self).__init__()
        uic.loadUi("Servizi/VIsta_Prenotazioni/VIsta_Inserisci_Prenotazione/VistaPrenotaPazienti.ui",self)
        self.ButtonPrenota.clicked.connect(lambda :self.aggiungi_Prenotazione(paziente))
        self.ButtonAnnulla.clicked.connect(self.close)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/IconaPrenotazioneomb.png")
        self.Back.setPixmap(pixmap)
        self.LogoPrenotazioni.setPixmap(pixmap1)
        self.callback = callback

    def aggiungi_Prenotazione(self,paziente):
        a=str(self.comboBox.currentText())
        sintomi =str(self.textEdit.toPlainText())
        codiceDiEmergenza=0
        if a=="Verde":
            codiceDiEmergenza=3
        if a=="Giallo":
            codiceDiEmergenza=2
        if a=="Rosso":
            codiceDiEmergenza=1

        if len(sintomi) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Sintomi')
            return
        paz=Paziente
        if paz.stato_prenotazione_Paziente(self,paziente):
            f=1
        else:
            return
        if paz.stato_Ricovero_Paziente(self,paziente):
            f=1
        else:
            return
        prenotazione = Prenotazione()
        prenotazione.aggiungi_Prenotazione(paziente,codiceDiEmergenza,sintomi,datetime.datetime.now())
        self.callback
        self.close()
