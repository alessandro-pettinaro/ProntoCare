import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from Servizi.VIsta_Prenotazioni.Vista_Info_Prenotazione.VistaInfoPrenotazione import VistaInfoPrenotazioni
from Servizi.Prenotazione import Prenotazione


class VistaListaPrenotazioni(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPrenotazioni, self).__init__(parent)
        uic.loadUi('Servizi/VIsta_Prenotazioni/VistaListaPazientiPrenotazioni.ui', self)
        self.update_pr()
        self.ButtonApri.clicked.connect(self.go_info_prenotazione)


    def load_Prenotazioni(self):  # carichiamo dentro la lista dei pazienti
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as file:
                my_dict = dict(pickle.load(file))
            sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1].codiceDiEmergenza))
            with open('Dati_Sistema/Prenotazioni.pickle', 'wb') as file:
                pickle.dump(sorted_dict, file)
            if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
                with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    self.prenotazioni.extend(current.values())

    def update_pr(self):
        self.prenotazioni = []
        self.load_Prenotazioni()
        listview_model = QStandardItemModel(self.listView)
        for prenotazione in self.prenotazioni:
            item = QStandardItem()
            nome = f"{prenotazione.paziente.nome} {prenotazione.paziente.cognome} - {type(prenotazione).__name__} {prenotazione.paziente.cf}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.listView.setModel(listview_model)

    def go_info_prenotazione(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            cf = str(selected.split("-")[1].strip().split(" ")[1])
            prenotazione = None
            if tipo == "Prenotazione":
                prenotazione =Prenotazione().ricerca_Prenotazione_CF(cf)
            self.vista_info = VistaInfoPrenotazioni(prenotazione,elimina_callback=self.update_pr)
            self.vista_info.show()
        except IndexError:
            return


