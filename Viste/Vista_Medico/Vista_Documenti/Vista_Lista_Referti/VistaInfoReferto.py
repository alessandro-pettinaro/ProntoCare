from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget
from Paziente.Documenti.Referto import Referto

class VistaInfoReferto(QWidget):
    def __init__(self, referto):
        super(VistaInfoReferto, self).__init__()
        uic.loadUi('Viste/Vista_Medico/Vista_Documenti/Vista_Lista_Referti/VistaReferti.ui',self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Viste/Vista_Medico/Vista_Documenti/Vista_Lista_Referti/IconaReferto-1.png")
        self.Back.setPixmap(pixmap)
        self.LogoPrenotazioni.setPixmap(pixmap1)
        self.Nome.setText(str(referto.paziente.nome))
        self.Cognome.setText(referto.paziente.cognome)
        a = ""
        if int(referto.codiceDiEmergenza) == 1:
            a = "Rosso"
        if int(referto.codiceDiEmergenza) == 2:
            a = "Giallo"
        if int(referto.codiceDiEmergenza) == 3:
            a = "Verde"
        self.CodiceDiEmergenza.setText(a)
        self.textEditDiagnosi.setText(str(referto.diagnosi))
        self.lineEdit_Data.setText(str(referto.dataReferto))




