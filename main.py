import multiprocessing
import sys
import threading

from PyQt6.QtCore import QCoreApplication, QTimer
from PyQt6.QtWidgets import QApplication
from Viste.Vista_Loading.VistaLoading import VistaLoading
from Backup.GestoreBackup import GestoreBackup


if __name__ == '__main__':

   app = QApplication(sys.argv)
   vistaloading = VistaLoading()
   vistaloading.show()
   backup = GestoreBackup(12, 32)
   backup.backup()
   timer = QTimer()
   timer.start(60000)
   timer.timeout.connect(backup.backup)
   sys.exit(app.exec())





