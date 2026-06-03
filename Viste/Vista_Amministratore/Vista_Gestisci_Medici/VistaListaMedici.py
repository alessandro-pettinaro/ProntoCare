import os.path
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget

from Viste.Vista_Amministratore.Vista_Gestisci_Medici.VIsta_Inserisci_Medico.VistaInserisciMedico import VistaInserisciMedico
from Viste.Vista_Amministratore.Vista_Gestisci_Medici.Vista_Info_Medico.VistaInfoMedico import VistaInfoMedico
from Personale.Medico import Medico


class VistaListaMedici(QWidget):
    def __init__(self, parent=None):
        super(VistaListaMedici, self).__init__(parent)
        uic.loadUi('Viste/Vista_Amministratore/Vista_Gestisci_Medici/VistaListaMedici.ui', self)
        self.update()
        self.ButtonInserisci.clicked.connect(self.go_inserisci_medico)
        self.ButtonApri.clicked.connect(self.go_info_medico)

    def load_Medici(self):
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.medici.extend(current.values())

    def update(self):
        self.medici = []
        self.load_Medici()
        listview_model = QStandardItemModel(self.listView)
        for medico in self.medici:
            item = QStandardItem()
            nome = f"{medico.nome} {medico.cognome} - {type(medico).__name__} {medico.cf}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.listView.setModel(listview_model)

    def go_inserisci_medico(self):
        self.inserisci_medico = VistaInserisciMedico(callback=self.update)
        self.inserisci_medico.show()

    def go_info_medico(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            cf = str(selected.split("-")[1].strip().split(" ")[1])
            medico = None
            if tipo == "Medico":
                infermiere = Medico().ricerca_Medico_CF(cf)
            self.vista_info = VistaInfoMedico(infermiere, elimina_callback=self.update)
            self.vista_info.show()
        except IndexError:
            print("INDEX ERROR")
            return

