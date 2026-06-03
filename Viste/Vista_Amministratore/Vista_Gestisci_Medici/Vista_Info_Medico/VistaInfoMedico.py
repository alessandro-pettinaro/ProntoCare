from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from Personale.Infermiere import Infermiere
from Viste.Vista_Amministratore.Vista_Gestisci_Medici.Vista_Info_Medico.VistaModificaMedici import VistaModificaMedico
from Personale.Medico import Medico


class VistaInfoMedico(QWidget):
    def __init__(self, medico, elimina_callback):
        super(VistaInfoMedico, self).__init__()
        self.elimina_callback = elimina_callback
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Medici/Vista_Info_Medico/VistaInfoMedico.ui', self)
        pixmap = QPixmap("Viste/Vista_Amministratore/IconaMedico.png")
        self.LogoMedici.setPixmap(pixmap)
        info = {}  # informazioni del Infermiere
        if isinstance(medico,Medico):
            info = medico.get_Info_Medico()
        self.Nome.setText(str(info['nome']))
        self.Cognome.setText(str(info['cognome']))
        self.CodiceFiscale.setText(str(info['cf']))
        self.Username.setText(str(info['username']))
        self.Sesso.setText(str(info['sesso']))
        self.DataDiNascita.setText(str(info['dataDiNascita']))
        self.Password.setText(str(info['password']))


        self.ButtonModifica.clicked.connect(lambda: self.go_vista_modifica(medico))
        self.ButtonElimina.clicked.connect(lambda: self.go_elimina(medico))

    def go_vista_modifica(self, medico):
        self.close()
        self.vista_modifica = VistaModificaMedico(medico, elimina_callback=self.elimina_callback)
        self.vista_modifica.show()

    def go_elimina(self, medico):
        notifica = QMessageBox.question(self, "Sei sicuro?", "Vuoi eliminare il medico?")
        if notifica == QMessageBox.StandardButton.Yes:
            if isinstance(medico, Medico):
                medico.rimuovi_Medico()
            self.elimina_callback()
            self.close()

