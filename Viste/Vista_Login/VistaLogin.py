import os.path
import pickle

from PyQt6.QtGui import QPixmap,QColor
from PyQt6.QtWidgets import QWidget, QMessageBox, QGraphicsDropShadowEffect
from PyQt6 import uic
from Viste.Vista_Amministratore.VistaAmministratore import VistaAmministratore
from Viste.Vista_Infermiere.VistaInfermiere import VistaInfermiere
from Viste.Vista_Medico.VistaMedico import VistaMedico
from PyQt6.QtGui import QFont

class VistaLogin(QWidget):
    def __init__(self, parent=None):
        super(VistaLogin, self).__init__(parent)
        uic.loadUi('Viste/Vista_Login/vistaLogin.ui', self)
        pixmap = QPixmap("Viste/Vista_Login/BackGroundLogin.png")
        self.ref.setPixmap(pixmap)
        font = QFont("Arial",30)
        font.setBold(True)
        font_= QFont("Arial",12)
        font_.setBold(True)
        self.label.setFont(font)
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setColor(QColor(0, 0, 0, 65))  # Colore: nero, opacità: 180
        shadow_effect.setOffset(2, 2)  # Offset orizzontale e verticale
        shadow_effect.setBlurRadius(30)  # Raggio di sfocatura
        shadow_effect1= QGraphicsDropShadowEffect()
        shadow_effect1.setColor(QColor(0, 0, 0, 65))  # Colore: nero, opacità: 180
        shadow_effect1.setOffset(2, 2)  # Offset orizzontale e verticale
        shadow_effect1.setBlurRadius(30)  # Raggio di sfocatura
        shadow_effect2 = QGraphicsDropShadowEffect()
        shadow_effect2.setColor(QColor(0, 0, 0, 100))  # Colore: nero, opacità: 180
        shadow_effect2.setOffset(2, 2)  # Offset orizzontale e verticale
        shadow_effect2.setBlurRadius(30)  # Raggio di sfocatura
        self.lineEdit_Username.setGraphicsEffect(shadow_effect)
        self.lineEdit_Password.setGraphicsEffect(shadow_effect1)
        self.ButtonLogin.setFont(font_)
        self.ButtonLogin.setGraphicsEffect(shadow_effect2)
        self.ButtonLogin.clicked.connect(self.goviste)

    def goviste(self):
        username_inserito = self.lineEdit_Username.text()
        password_inserito = self.lineEdit_Password.text()

        if self.controllo_login_amministratore(username_inserito,password_inserito):
            self.vista_amministratore=VistaAmministratore()
            self.vista_amministratore.show()
            return
        else:
            if self.controllo_login_infermiere(username_inserito,password_inserito):
                self.vista_infermiere = VistaInfermiere(username_inserito)
                self.vista_infermiere.show()
            else :
                if self.controllo_login_medico(username_inserito,password_inserito):
                    self.vista_medico = VistaMedico(username_inserito)
                    self.vista_medico.show()
                else:
                    QMessageBox.critical(self,'ERRORE','Username o Password errati')

    def controllo_login_amministratore(self,username,password):
        if os.path.isfile('Dati_sistema/Amministratore.pickle') :
            with open('Dati_sistema/Amministratore.pickle','rb') as f :
                amministratori=dict(pickle.load(f))
                if str(amministratori.get("username"))==username and str(amministratori.get("password"))==password:
                    return True
                else:
                    return False

    def controllo_login_infermiere(self, username, password):
        if os.path.isfile('Dati_sistema/Infermieri.pickle'):
            with open('Dati_sistema/Infermieri.pickle', 'rb') as f:
                infermiere=dict(pickle.load(f))
                for infermiere in infermiere.values():
                    if str(infermiere.username) == username and str(infermiere.password) == password:
                        return True
                return False

    def controllo_login_medico(self, username, password):
        if os.path.isfile('Dati_sistema/Medici.pickle'):
            with open('Dati_sistema/Medici.pickle', 'rb') as f:
                medico=dict(pickle.load(f))
                for medico in medico.values():
                    if str(medico.username) == username and str(medico.password) == password:
                        return True
                return False



