from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget
from Paziente.Documenti.LetteraDiDimissione import LetteraDiDimisione

class VistaInfoLettera(QWidget):
    def __init__(self, lettera, elimina_callback):
        super(VistaInfoLettera, self).__init__()
        self.elimina_callback = elimina_callback
        uic.loadUi('Viste/Vista_Medico/Vista_Documenti/Vista_Lista_Lettera/VistaInfoLetteraDiDimissioni.ui',self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Viste/Vista_Medico/Vista_Documenti/Vista_Lista_Lettera/IconaLetteraDiDimissione.png")
        self.Back.setPixmap(pixmap)
        self.LogoLettarDiDimissione.setPixmap(pixmap1)
        self.Nome.setText(str(lettera.paziente.nome))
        self.Cognome.setText(lettera.paziente.cognome)
        self.lineEdit_Data.setText(str(lettera.dataDimissione))
        self.CicloDiCure.setText(str(lettera.controlliDaEffetuare))