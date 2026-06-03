import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from Paziente.Documenti.Referto import Referto
from Viste.Vista_Medico.Vista_Documenti.Vista_Lista_Referti.VistaInfoReferto import VistaInfoReferto


class VistaListaReferti(QWidget):
    def __init__(self):
        super(VistaListaReferti,self).__init__()
        uic.loadUi('Viste/Vista_Medico/Vista_Documenti/Vista_Lista_Referti/VistaListaRefertiMedico.ui', self)
        self.ButtonApri.clicked.connect(self.go_info_referto)
        self.update_pr()

    def load_Referti(self):  # carichiamo dentro la lista dei pazienti

        if os.path.isfile('Dati_Sistema/Referti.pickle'):
            with open('Dati_Sistema/Referti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.referti.extend(current.values())

    def update_pr(self):
        self.referti = []
        self.load_Referti()
        listview_model = QStandardItemModel(self.listView)
        for referto in self.referti:
            item = QStandardItem()
            nome = f"{referto.paziente.nome} {referto.paziente.cognome} - {type(referto).__name__} {referto.codice}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.listView.setModel(listview_model)

    def go_info_referto(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            cod = int(selected.split("-")[1].strip().split(" ")[1])
            referto =Referto().ricerca_referto_COD(cod)
            self.vista_info = VistaInfoReferto(referto)
            self.vista_info.show()
        except IndexError:
            return

        