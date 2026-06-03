import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QMessageBox
from Viste.Vista_Medico.VistaListaPazientiM import VistaListaPazientiM
from Servizi.VIsta_Prenotazioni.VIstaListaPrenotazioniM import VistaListaPrenotazioniM
from Servizi.VIsta_Prenotazioni.VIstaListaPrenotazioni import VistaListaPrenotazioni
from Viste.Vista_Medico.Vista_Visita.VistaVisita import VistaVisita
from Viste.Vista_Medico.Vista_Ricoveri.VistaListaRicoveri import VistaListaRicoveri
from Personale.Medico import Medico
from Viste.Vista_Medico.Vista_Documenti.VistaDocumenti import VistaDocumenti
class VistaMedico(QWidget):
    def __init__(self,username):
        super(VistaMedico,self).__init__()
        uic.loadUi('Viste/Vista_Medico/VistaMenùMedico.ui', self)
        pixmap = QPixmap("Viste/Vista_Infermiere/Back.png")
        pixmap1 = QPixmap("Viste/Vista_Infermiere/LogoNome.png")
        aggiorno=VistaListaPrenotazioni
        aggiorno.update_pr
        self.Back.setPixmap(pixmap)
        self.ButtonVisita.clicked.connect(self.go_vista_visita)
        self.ButtonVisita.setIcon(QIcon('Viste/Vista_Medico/MenuVisitaPiccolo.png'))
        self.ButtonRicoveri.clicked.connect(self.go_vista_ricoveri)
        self.ButtonRicoveri.setIcon(QIcon('Viste/Vista_Medico/MenuRicoveriPiccolo.png'))
        self.ButtonPazienti.clicked.connect(self.go_vista_paziente)
        self.ButtonPazienti.setIcon(QIcon('Viste/Vista_Medico/MenuPazientiPiccolo.png'))
        self.ButtonPrenotazioni.clicked.connect(self.go_vista_prenotazioni)
        self.ButtonPrenotazioni.setIcon(QIcon('Viste/Vista_Medico/MenuPrenotazioniPiccolo.png'))
        self.ButtonDocumenti.setIcon(QIcon('Viste/Vista_Medico/MenuDocumentiPiccolo.png'))
        self.ButtonDocumenti.clicked.connect(self.go_vista_documenti)
        self.ButtonLogout.setIcon(QIcon('Viste/Vista_Infermiere/LogoutBianco.png'))
        self.ButtonLogout.clicked.connect(self.go_logout)
        self.LogoNome.setPixmap(pixmap1)
        medico = self.nome_medico(username)
        nome = medico.nome
        cognome=medico.cognome
        self.Welcome.setText("Benvenuto,"+" "+nome+" "+cognome)

    def lista_prenotazioni(self):
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.prenotazione.extend(current.values())

    def visita_prenotazione_paziente(self): #prenotazione del paziente da visitare
        self.prenotazione = []
        self.lista_prenotazioni()
        try:
            self.visita=self.prenotazione[0]
            return self.visita
        except:
            return

    def go_vista_visita(self):
        self.prenotazione=self.visita_prenotazione_paziente()
        if self.prenotazione!=None:
            self.vista_visita = VistaVisita()
            self.vista_visita.show()
        else:
            QMessageBox.critical(self, 'Errore', 'Non ci sono pazienti da visitare')


    def go_vista_ricoveri(self):
        self.vistaListaRicoveri=VistaListaRicoveri()
        self.vistaListaRicoveri.show()

    def go_logout(self):
            self.close()


    def go_vista_prenotazioni(self):
        self.vista_prenotazioni=VistaListaPrenotazioniM()
        self.vista_prenotazioni.show()

    def go_vista_paziente(self):
        self.vist_pazienti=VistaListaPazientiM()
        self.vist_pazienti.show()

    def go_vista_documenti(self):
        self.vist_doc = VistaDocumenti()
        self.vist_doc.show()

    def nome_medico(self,username):
        medico=Medico()
        a=medico.ricerca_Medico_username(username)
        return a


