import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from Paziente.Paziente import Paziente
from Viste.Vista_Infermiere.Vista_Gestisci_Paziente.Vista_Info_Paziente.VistaModificaPaziente import VistaModificaPaziente
from Servizi.Prenotazione import Prenotazione
from Servizi.Ricovero import Ricovero

class VistaInfoPaziente(QWidget):
        def __init__(self, paziente, elimina_callback):
            super(VistaInfoPaziente, self).__init__()
            self.elimina_callback = elimina_callback
            uic.loadUi('Viste/Vista_Infermiere/Vista_Gestisci_Paziente/Vista_Info_Paziente/VistaInfoPazientiMedico.ui', self)
            pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
            pixmap1 = QPixmap("Viste/Vista_Infermiere/IconaPazientiom.png")
            self.Back.setPixmap(pixmap)
            self.LogoPazienti.setPixmap(pixmap1)
            info = {}  # informazioni del Infermiere
            if isinstance(paziente,Paziente):
                info = paziente.get_Info_Paziente()
            self.Nome.setText(str(info['nome']))
            self.Cognome.setText(str(info['cognome']))
            self.Sesso.setText(str(info['sesso']))
            self.DataDiNascita.setText(str(info['dataDiNascita']))
            self.CittaDiNascita.setText(str(info['luogoDiNascita']))
            self.CodiceFiscale.setText(str(info['cf']))
            self.Residenza.setText(str(info['residenza']))
            self.Cellulare.setText(str(info['telefono']))
            self.Prenotazione.setText(str(self.prenotazione_paziente(paziente)))
            self.Ricovero.setText(str(self.ricovero_paziente(paziente)))


        def prenotazione_paziente(self,paziente):
            self.prenotazione=Prenotazione()
            self.prenotazione_paziente=self.prenotazione.ricerca_Prenotazione_CF(paziente.cf)
            if self.prenotazione_paziente:
                nome = f" {self.prenotazione_paziente.dataPrenotazione}"
                return nome
            else :
                x=f"non prenotato"
                return x

        def ricovero_paziente(self,paziente):
            self.ricovero=Ricovero()
            self.ricovero_paz=self.ricovero.ricerca_Ricovero_CF(paziente.cf)
            if self.ricovero_paz:
                nome = f"ricoverato"
                return nome
            else :
                x=f"non ricoverato"
                return x




