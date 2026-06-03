import os.path
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from Personale.Infermiere import Infermiere
from Viste.Vista_Amministratore.Vista_Gestisci_Infermieri.Vista_Inserisci_Infermiere.VistaInserisciInfermieri import VistaInserisciInfermieri
from Viste.Vista_Amministratore.Vista_Gestisci_Infermieri.Vista_Info_Infermiere.VistaInfoInfermiere import VistaInfoInfermiere

class VistaListaInfermieri(QWidget):
    def __init__(self,parent=None):
        super(VistaListaInfermieri, self).__init__(parent)
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Infermieri/VistaMenuListaInfermieri.ui', self)
        self.update()
        self.ButtonInserisci.clicked.connect(self.go_inserisci_infermieri)
        self.ButtonApri.clicked.connect(self.go_info_infermieri)



    def load_Infermieri(self): #carichiamo dentro la lista gli infermieri
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle','rb') as f:
                current=dict(pickle.load(f))
                self.infermieri.extend(current.values())
    
    def update(self):
        self.infermieri=[]
        self.load_Infermieri()
        self.listView_model = QStandardItemModel(self.listView)
        for infermieri  in self.infermieri:
            item = QStandardItem()
            nome = f"{infermieri.nome} {infermieri.cognome} - {type(infermieri).__name__} {infermieri.cf}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listView_model.appendRow(item)
        self.listView.setModel(self.listView_model)

    def go_inserisci_infermieri(self):
        self.inserisci_infermieri=VistaInserisciInfermieri(callback=self.update)
        self.inserisci_infermieri.show()

    def go_info_infermieri(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            cf = str(selected.split("-")[1].strip().split(" ")[1])
            infermiere = None
            if tipo == "Infermiere":
                infermiere = Infermiere().ricerca_Infermiere_CF(cf)
            self.vista_info = VistaInfoInfermiere(infermiere,elimina_callback=self.update)
            self.vista_info.show()
        except IndexError:
            print("INDEX ERROR")
            return


