import os
import pickle
import datetime

from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from Paziente.Documenti.Referto import Referto
from Servizi.Ricovero import Ricovero
from Servizi.Vista_Lettera_Dimissione.VistaInserisciLetteraDiDimisione import VistaInserisciLetteraDiDimmisione
from Servizi.Prenotazione import Prenotazione
from Servizi.Ricovero import Ricovero


class VistaVisita(QWidget):
    def __init__(self, parent=None):
        super(VistaVisita, self).__init__(parent)
        self.paziente_da_visitare=self.visita_prenotazione_paziente()
        uic.loadUi('Viste/Vista_Medico/Vista_Visita/VistaVisitaPazienti.ui', self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Viste/Vista_Medico/Vista_Visita/IconaVisitaomb.png")
        self.Back.setPixmap(pixmap)
        self.LogoVisita.setPixmap(pixmap1)
        self.Nome.setText(str(self.paziente_da_visitare.paziente.nome))
        self.Cognome.setText(str(self.paziente_da_visitare.paziente.cognome))
        a = ""
        if str(self.paziente_da_visitare.codiceDiEmergenza) == "1":
            a = "Rosso"
        if str(self.paziente_da_visitare.codiceDiEmergenza) == "2":
            a = "Giallo"
        if str(self.paziente_da_visitare.codiceDiEmergenza) == "3":
            a = "Verde"
        self.CodiceDiEmergenza.setText(a)
        self.textEdit.setText(str(self.paziente_da_visitare.sintomi))

        self.ButtonRicovera.clicked.connect(lambda :self.go_ricovera(self.paziente_da_visitare.paziente,self.paziente_da_visitare))
        self.ButtonDimetti.clicked.connect(lambda :self.go_dimisioni(self.paziente_da_visitare.paziente,self.paziente_da_visitare))


    def lista_prenotazioni(self):
        with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as file:
            my_dict = pickle.load(file)
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1].codiceDiEmergenza))
        with open('Dati_Sistema/Prenotazioni.pickle', 'wb') as file:
            pickle.dump(sorted_dict, file)
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.prenotazione.extend(current.values())

    def visita_prenotazione_paziente(self):
        self.prenotazione = []
        self.lista_prenotazioni()
        self.visita=self.prenotazione[0]
        return self.visita

    def numero_Referti(self):
        i=0
        if os.path.isfile('Dati_Sistema/Referti.pickle'):
            with open('Dati_Sistema/Referti.pickle', 'rb') as f:
                paziente = dict(pickle.load(f))
                for paziente in paziente.keys():
                    i=i+1
            return i
        else:
            return i


    def aggiungi_Referto(self,paziente,codice):
        diagnosi=self.textEdit_2.toPlainText()
        if len(diagnosi) == 0:
            QMessageBox.critical(self, 'Errore', 'Inserisci Diagnosi')
            return False
        self.referto=Referto()
        self.referto.create_referto(paziente,self.numero_Referti(),codice,diagnosi,datetime.datetime.now())
        return True



    def go_ricovera(self,paziente,prenotazione):
        notifica=QMessageBox.question(self, "Sei sicuro?", "Vuoi ricoverare il paziente?")
        if notifica==QMessageBox.StandardButton.Yes:
                if self.aggiungi_Referto(paziente,prenotazione.codiceDiEmergenza):
                    self.ricovero=Ricovero()
                    if self.ricovero.verifica_disponibilita():
                       diagnosi=str(self.textEdit_2.toPlainText())
                       self.ricovero.aggiungi_Ricovero(paziente,datetime.datetime.now(),diagnosi)
                    else :
                        QMessageBox.critical(self, 'Errore', 'Posti letti terminati,abbiamo inoltrato una richiesta di ricovero del paziente alla struttura sanitaria più vicina  ')
                    self.elimina_prenotazione(prenotazione)

    def go_dimisioni(self,paziente,prenotazione): #dimissioni del paziente
        if self.aggiungi_Referto(paziente,prenotazione.codiceDiEmergenza):
            self.vista_letteraDimissione=VistaInserisciLetteraDiDimmisione(paziente)
            self.vista_letteraDimissione.show()
            self.elimina_prenotazione(prenotazione)



    def elimina_prenotazione(self,prenotazione):
        if isinstance(prenotazione, Prenotazione):
            prenotazione.rimuovi_Prenotazione(prenotazione.paziente.cf)
        self.close()

