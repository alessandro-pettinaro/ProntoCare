from PyQt6 import uic
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor, QPixmap
from PyQt6.QtWidgets import QWidget, QProgressBar, QGraphicsDropShadowEffect
from Viste.Vista_Login.VistaLogin import VistaLogin


class VistaLoading(QWidget):
    def __init__(self):
            super().__init__()
            uic.loadUi("Viste/Vista_Loading/VistaLoading.ui", self)
            pixmap = QPixmap("Viste/Vista_Loading/LogoProntoSoccorso.png")

            pixmap1=pixmap.scaled(pixmap.width()*2,pixmap.height())
            self.Logo.setPixmap(pixmap1)
            self.progress_bar = QProgressBar(self)
            self.progress_bar.setTextVisible(False)
            self.progress_bar.setGeometry(280, 400, 200, 6)
            self.progress_bar.alignment()
            self.Logo.setPixmap(pixmap)


            shadow_effect = QGraphicsDropShadowEffect()
            shadow_effect.setColor(QColor(0, 0, 0, 150))  # Colore: nero, opacità: 180
            shadow_effect.setOffset(0, 0)  # Offset orizzontale e verticale
            shadow_effect.setBlurRadius(30)  # Raggio di sfocatura
            self.progress_bar.setGraphicsEffect(shadow_effect)

            self.progress_bar.setStyleSheet("""
                QProgressBar {
                    border: 0px solid black;
                    background-color: rgb(174, 178, 189);
                    border-radius: 3px;
                }
                QProgressBar::chunk {
                    background-color: #e6ebef;
                    border-radius: 3px;
                }
            """)

            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_progress)
            self.timer.start(25)
            self.progress_value = 0

    def update_progress(self):
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()
            self.vista_login=VistaLogin()
            self.vista_login.show()
            self.close()
