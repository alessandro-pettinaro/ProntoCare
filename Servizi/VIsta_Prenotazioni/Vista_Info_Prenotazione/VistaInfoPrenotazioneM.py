from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from Servizi.Prenotazione import Prenotazione


class VistaInfoPrenotazioniM(QWidget):
    def __init__(self, prenotazione):
        super(VistaInfoPrenotazioniM, self).__init__()
        uic.loadUi('Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/VistainfoPrenotaPazienti_Medico.ui',self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/IconaPrenotazioneomb.png")
        self.Back.setPixmap(pixmap)
        self.LogoPrenotazioni.setPixmap(pixmap1)
        info = {}  # informazioni del Infermiere
        if isinstance(prenotazione, Prenotazione):
            info = prenotazione.get_Info_Prenotazione()
        self.Nome.setText(str(prenotazione.paziente.nome))
        self.Cognome.setText(str(prenotazione.paziente.cognome))
        a=""
        if str(info['codiceDiEmergenza'])=="1":
            a="Rosso"
        if str(info['codiceDiEmergenza'])=="2":
            a="Giallo"
        if str(info['codiceDiEmergenza'])=="3":
            a="Verde"
        self.CodiceDiEmergenza.setText(a)
        self.Prognosi.setText(str(info['sintomi']))
        self.LogoPrenotazioni.setPixmap(pixmap1)
