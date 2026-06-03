import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from Paziente.Paziente import Paziente
from Viste.Vista_Infermiere.Vista_Gestisci_Paziente.Vista_Info_Paziente.VistaInfoPaziente import VistaInfoPaziente
from Viste.Vista_Infermiere.Vista_Gestisci_Paziente.Vista_Inserisci_Paziente.VistaInserisciPaziente import VistaInserisciPaziente
from Servizi.VIsta_Prenotazioni.VIsta_Inserisci_Prenotazione.VistaInserisciPrenotazione import VistaInserisciPrenotazione

class VistaListaPazientiM(QWidget):
    def __init__(self, parent=None):
        super(VistaListaPazientiM, self).__init__(parent)
        uic.loadUi('Viste/Vista_Medico/VistaListaPazientiMedico.ui', self)
        self.update_p()
        self.ButtonApri.clicked.connect(self.go_info_paziente)

    def load_Pazienti(self):  # carichiamo dentro la lista dei pazienti
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.pazienti.extend(current.values())

    def update_p(self):
        self.pazienti = []
        self.load_Pazienti()
        listview_model = QStandardItemModel(self.listView)
        for paziente in self.pazienti:
            item = QStandardItem()
            nome = f"{paziente.nome} {paziente.cognome} - {type(paziente).__name__} {paziente.cf}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.listView.setModel(listview_model)

    def go_info_paziente(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            tipo = selected.split("-")[1].strip().split(" ")[0]
            cf = str(selected.split("-")[1].strip().split(" ")[1])
            paziente = None
            if tipo == "Paziente":
                paziente =Paziente().ricerca_Paziente_CF(cf)
            self.vista_info = VistaInfoPaziente(paziente,elimina_callback=self.update_p)
            self.vista_info.show()
        except IndexError:
            return

