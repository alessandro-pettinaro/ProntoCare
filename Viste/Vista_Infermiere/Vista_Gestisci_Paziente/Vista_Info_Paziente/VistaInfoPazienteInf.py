import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from Paziente.Paziente import Paziente
from Viste.Vista_Infermiere.Vista_Gestisci_Paziente.Vista_Info_Paziente.VistaModificaPaziente import VistaModificaPaziente
from Servizi.Prenotazione import Prenotazione
from Servizi.Ricovero import Ricovero

class VistaInfoPazienteInf(QWidget):
        def __init__(self, paziente, elimina_callback):
            super(VistaInfoPazienteInf, self).__init__()
            self.elimina_callback = elimina_callback
            uic.loadUi('Viste/Vista_Infermiere/Vista_Gestisci_Paziente/Vista_Info_Paziente/VistaInfoPazientiInf.ui', self)
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

            self.ButtonModifica.clicked.connect(lambda: self.go_vista_modifica(paziente))
            self.ButtonElimina.clicked.connect(lambda: self.go_elimina(paziente))

        def go_vista_modifica(self, paziente):
            self.close()
            self.vista_modifica = VistaModificaPaziente(paziente, elimina_callback=self.elimina_callback)
            self.vista_modifica.show()

        def go_elimina(self, paziente):
            notifica = QMessageBox.question(self, "Sei sicuro?", "Vuoi eliminare il paziente?")
            if notifica == QMessageBox.StandardButton.Yes:
                if isinstance(paziente, Paziente):
                    paziente.rimuovi_Paziente()
                self.elimina_callback()
                self.close()


        def prenotazione_paziente(self,paziente):
            self.prenotazione = Prenotazione()
            self.prenotazione_paziente = self.prenotazione.ricerca_Prenotazione_CF(paziente.cf)
            if self.prenotazione_paziente:
                nome = f"prenotato "
                return nome
            else:
                x = f"non prenotato"
                return x

        def ricovero_paziente(self,paziente):
            self.ricovero = Ricovero()
            self.ricovero_paz = self.ricovero.ricerca_Ricovero_CF(paziente.cf)
            if self.ricovero_paz:
                nome = f"ricoverato"
                return nome
            else:
                x = f"non ricoverato"
                return x




