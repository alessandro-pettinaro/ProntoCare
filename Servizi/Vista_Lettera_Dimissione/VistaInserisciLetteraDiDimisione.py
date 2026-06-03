import datetime
from PyQt6 import uic
from PyQt6.QtGui import  QPixmap
from PyQt6.QtWidgets import QMessageBox, QWidget
from Paziente.Documenti.LetteraDiDimissione import LetteraDiDimisione

class VistaInserisciLetteraDiDimmisione(QWidget):
    def __init__(self,paziente):
        super(VistaInserisciLetteraDiDimmisione, self).__init__()
        uic.loadUi('Servizi/Vista_Lettera_Dimissione/VistaLetteraDiDimissioni.ui', self)
        pixmap = QPixmap("Servizi/VIsta_Prenotazioni/Vista_Info_Prenotazione/Back.png")
        pixmap1 = QPixmap("Servizi/Vista_Lettera_Dimissione/IconaLetteraDiDimissione.png")
        self.Back.setPixmap(pixmap)
        self.LogoLettarDiDimissione.setPixmap(pixmap1)
        self.Nome.setText(str(paziente.nome))
        self.Cognome.setText(str(paziente.cognome))
        self.lineEdit_Data.setText(str(datetime.datetime.now()))
        self.ButtonRegistra.clicked.connect(lambda :self.aggiungi_Lettera(paziente))

    def aggiungi_Lettera(self,paziente):
        controllo=str(self.textEditCicloDiCure.toPlainText())

        if len(controllo) == 0 :
            QMessageBox.critical(self, 'Errore', 'Inserisci Controllo da effetuare')
            return
        self.letteraDiDimmisione=LetteraDiDimisione()
        self.letteraDiDimmisione.create_lettera(paziente,self.letteraDiDimmisione.numero_lettere(),controllo,datetime.datetime.now())
        self.close()


