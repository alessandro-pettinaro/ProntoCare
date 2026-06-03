from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from Servizi.Prenotazione import Prenotazione


class VistaInfoPrenotazioni(QWidget):
    def __init__(self, prenotazione, elimina_callback):
        super(VistaInfoPrenotazioni, self).__init__()
        self.elimina_callback = elimina_callback
        uic.loadUi('Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/VistaInfoPrenotaPazienti.ui',self)
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
        self.label.setText(str(info['sintomi']))
        self.LogoPrenotazioni.setPixmap(pixmap1)
        self.ButtonElimina.clicked.connect(lambda :self.go_elimina(prenotazione))



    def go_elimina(self,prenotazione):
        notifica = QMessageBox.question(self, "Sei sicuro?", "Vuoi eliminare la prenotazione?")
        if notifica == QMessageBox.StandardButton.Yes:
            if isinstance(prenotazione, Prenotazione):
                prenotazione.rimuovi_Prenotazione(prenotazione.paziente.cf)
            self.elimina_callback()
            self.close()