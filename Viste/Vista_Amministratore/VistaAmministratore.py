from PyQt6 import uic
from PyQt6.QtGui import QIcon, QTransform, QPixmap
from PyQt6.QtWidgets import QWidget
from Viste.Vista_Amministratore.Vista_Gestisci_Infermieri.VistaListaInfermieri import VistaListaInfermieri
from Viste.Vista_Amministratore.Vista_Gestisci_Medici.VistaListaMedici import VistaListaMedici

class VistaAmministratore(QWidget):
    def __init__(self ,parent=None):
        super(VistaAmministratore, self).__init__(parent)
        uic.loadUi('Viste/Vista_Amministratore/vista_admin.ui', self)
        pixmap = QPixmap("Viste/Vista_Amministratore/BackGroundAmministratore.png")
        self.FrameBianco.setPixmap(pixmap)

        self.ButtonInfermieri.setIcon(QIcon('Viste/Vista_Amministratore/IconaInfermiere.png'))
        self.ButtonInfermieri.clicked.connect(self.go_vista_lista_infermieri)
        self.ButtonLogout.setIcon(QIcon('Viste/Vista_Amministratore/Logout sinistra.png'))
        self.ButtonLogout.clicked.connect(self.go_logout)


        self.ButtonMedici.setIcon(QIcon('Viste/Vista_Amministratore/IconaMedico.png'))

        self.ButtonMedici.clicked.connect(self.go_vista_lista_medici)

    def go_vista_lista_infermieri(self):
        self.vista_lista_infermieri = VistaListaInfermieri()
        self.vista_lista_infermieri .show()

    def go_vista_lista_medici(self):
        self.vista_lista_medici = VistaListaMedici()
        self.vista_lista_medici.show()

    def go_logout(self):
        self.close()