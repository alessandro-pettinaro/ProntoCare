import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget, QMessageBox

from Servizi.Ricovero import Ricovero
from Viste.Vista_Medico.Vista_Ricoveri.Vista_Info_Ricovero.VistaInfoRicovero import VistaInfoRicovero
from Servizi.Vista_Lettera_Dimissione.VistaInserisciLetteraDiDimisione import VistaInserisciLetteraDiDimmisione

class VistaListaRicoveri(QWidget):
    def __init__(self, parent=None):
        super(VistaListaRicoveri, self).__init__(parent)
        uic.loadUi('Viste/Vista_Medico/Vista_Ricoveri/VistaListaRicoveri-2.ui', self)
        self.update()
        self.ButtonApri.clicked.connect(self.go_info_ricovero)
        self.ButtonInserisci.clicked.connect(self.go_dimissioni)


    def load_Ricoveri(self):  # carichiamo dentro la lista dei pazienti
        if os.path.isfile('Dati_Sistema/Ricoveri.pickle'):
            with open('Dati_Sistema/Ricoveri.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.ricoveri.extend(current.values())

    def update(self):
        self.ricoveri = []
        self.load_Ricoveri()
        listview_model = QStandardItemModel(self.listView)
        for ricovero in self.ricoveri:
            item = QStandardItem()
            nome = f"{ricovero.paziente.nome} {ricovero.paziente.cognome} - {type(ricovero).__name__} {ricovero.paziente.cf}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.listView.setModel(listview_model)

    def go_info_ricovero(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            cf = str(selected.split("-")[1].strip().split(" ")[1])
            medico = None
            if tipo == "Ricovero":
                ricovero = Ricovero().ricerca_Ricovero_CF(cf)
            self.vista_info = VistaInfoRicovero(ricovero)
            self.vista_info.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def go_dimissioni(self):
        self.ricovero=Ricovero()
        try:
            selected = self.listView.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            cf = str(selected.split("-")[1].strip().split(" ")[1])
            self.ricoveri=Ricovero()
            if tipo == "Ricovero":
                self.ricovero = Ricovero().ricerca_Ricovero_CF(cf)
            response=QMessageBox.question(self, "Sei sicuro?", "Vuoi dimettere il paziente?")
            if response==QMessageBox.StandardButton.Yes:
                self.ricoveri.rimuovi_Ricovero(cf)
                self.vista_lettera_dimissione=VistaInserisciLetteraDiDimmisione(self.ricovero.paziente)
                self.vista_lettera_dimissione.show()
                self.close()
            if response==QMessageBox.StandardButton.No:
                return

        except IndexError:
            print("INDEX ERROR")
            return


