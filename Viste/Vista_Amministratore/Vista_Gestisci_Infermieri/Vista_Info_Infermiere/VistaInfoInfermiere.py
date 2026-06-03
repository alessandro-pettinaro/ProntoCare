from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QMessageBox
from  Personale.Infermiere import Infermiere
from Viste.Vista_Amministratore.Vista_Gestisci_Infermieri.Vista_Info_Infermiere.VistaModificaInfermiere import VistaModificaInfermiere
from Viste.Vista_Amministratore.Vista_Gestisci_Infermieri.Vista_Inserisci_Infermiere.VistaInserisciInfermieri import VistaInserisciInfermieri
class VistaInfoInfermiere(QWidget):
    def __init__(self,infermiere,elimina_callback):
        super(VistaInfoInfermiere,self).__init__()
        self.elimina_callback = elimina_callback
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Infermieri/Vista_Info_Infermiere/vista_info.ui',self)
        pixmap = QPixmap("Viste/Vista_Amministratore/IconaInfermiere.png")
        info={} #informazioni del Infermiere
        if isinstance(infermiere,Infermiere):
            nome=f"Infermiere{infermiere.cf}"
            info=infermiere.get_Info_Infermiere()
        self.Nome.setText(str(info['nome']))
        self.Cognome.setText(str(info['cognome']))
        self.CodiceFiscale.setText(str(info['cf']))
        self.Username.setText(str(info['username']))
        self.Password.setText(str(info['password']))
        self.Sesso.setText(str(info['sesso']))
        self.DataDiNascita.setText(str(info['dataDiNascita']))
        self.LogoInfermieri.setPixmap(pixmap)

        
        self.ButtonModifica.clicked.connect(lambda : self.go_vista_modifica(infermiere))
        self.ButtonElimina.clicked.connect(lambda :self.go_elimina(infermiere))
    
    def go_vista_modifica(self,infermiere):
        self.close()
        self.vista_modifica=VistaModificaInfermiere(infermiere, elimina_callback=self.elimina_callback)
        self.vista_modifica.show()

    def go_elimina(self,infermiere):
        notifica = QMessageBox.question(self, "Sei sicuro?", "Vuoi eliminare l'infermiere?")
        if notifica == QMessageBox.StandardButton.Yes:
            if isinstance(infermiere, Infermiere):
                infermiere.rimuovi_Infermiere()
            self.elimina_callback()
            self.close()





        
        
        

