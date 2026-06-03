from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget
from Viste.Vista_Medico.Vista_Documenti.Vista_Lista_Referti.VistaListaReferti import VistaListaReferti
from Viste.Vista_Medico.Vista_Documenti.Vista_Lista_Lettera.VistaListaLetteraDimissioni import VistaListaLetteraDimissioni

class VistaDocumenti(QWidget):
    def __init__(self):
        super(VistaDocumenti,self).__init__()
        uic.loadUi('Viste/Vista_Medico/Vista_Documenti/VistaMenuDocumenti.ui', self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        self.FrameBianco.setPixmap(pixmap)
        self.ButtonLettera.setIcon(QIcon('Viste/Vista_Medico/Vista_Documenti/button_lettera_di_dimissione.png'))
        self.ButtonLettera.clicked.connect(self.go_lettera)
        self.ButtonReferto.setIcon(QIcon('Viste/Vista_Medico/Vista_Documenti/Menureferto.png.png'))
        self.ButtonReferto.clicked.connect(self.go_referti)

    def go_referti(self):
        self.vistaListaRicoveri = VistaListaReferti()
        self.vistaListaRicoveri.show()

    def go_lettera(self):
        self.vistaListaRicoveri = VistaListaLetteraDimissioni()
        self.vistaListaRicoveri.show()

