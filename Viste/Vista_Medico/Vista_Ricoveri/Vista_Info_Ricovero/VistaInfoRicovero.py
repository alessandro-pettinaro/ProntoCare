from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget


class VistaInfoRicovero(QWidget):
    def __init__(self, ricovero):
        super(VistaInfoRicovero,self).__init__()
        uic.loadUi('Viste/Vista_Medico/Vista_Ricoveri/Vista_Info_Ricovero/VistainfoRicovero.ui', self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Viste/Vista_Medico/Vista_Ricoveri/Vista_Info_Ricovero/LogoRicoveri.png")
        self.Back.setPixmap(pixmap)
        self.LogoRicovero.setPixmap(pixmap1)
        self.Nome.setText(str(ricovero.paziente.nome))
        self.Cognome.setText(str(ricovero.paziente.cognome))
        self.Diagnosi.setText(str(ricovero.diagnosi))
        self.DataRicovero.setText(str(ricovero.dataRicovero))