from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget
from Viste.Vista_Infermiere.Vista_Gestisci_Paziente.VistaListaPazienti import VistaListaPazienti
from Servizi.VIsta_Prenotazioni.VIstaListaPrenotazioni import VistaListaPrenotazioni
from Personale.Infermiere import Infermiere
class VistaInfermiere(QWidget):
    def __init__(self,username):
        super(VistaInfermiere, self).__init__()
        uic.loadUi('Viste/Vista_Infermiere/VistaMenuInfermieri.ui', self)
        pixmap = QPixmap("Viste/Vista_Infermiere/Back.png")
        pixmap1=QPixmap("Viste/Vista_Infermiere/LogoNome.png")
        self.FrameBianco.setPixmap(pixmap)
        self.ButtonPazienti.clicked.connect(self.go_vista_gestisci_pazienti)
        self.ButtonPazienti.setIcon(QIcon("Viste/Vista_Infermiere/MenuInfermieriPazientiPiccolo.png"))
        self.ButtonPrenotazioni.setIcon(QIcon("Viste/Vista_Infermiere/MenuInfermieriPrenotazioniPiccolo.png"))
        self.ButtonPrenotazioni.clicked.connect(self.go_vista_gestisci_prenotazioni)
        self.ButtonLogout.setIcon(QIcon('Viste/Vista_Infermiere/LogoutBianco.png'))
        self.ButtonLogout.clicked.connect(self.go_logout)
        self.LogoNome.setPixmap(pixmap1)
        infermiere=self.nome_infermiere(username)
        nome=infermiere.nome
        cognome=infermiere.cognome
        self.Welcome.setText("Benvenuto, "+nome+" "+cognome)
    def go_vista_gestisci_pazienti(self):
        self.vista_lista_pazienti=VistaListaPazienti()
        self.vista_lista_pazienti.show()

    def go_vista_gestisci_prenotazioni(self):
        self.vista_lista_prenotazioni=VistaListaPrenotazioni()
        self.vista_lista_prenotazioni.show()

    def go_logout(self):
        self.close()

    def nome_infermiere(self,username):
        infermiere=Infermiere()
        a=infermiere.ricerca_Infermiere_username(username)
        return a

