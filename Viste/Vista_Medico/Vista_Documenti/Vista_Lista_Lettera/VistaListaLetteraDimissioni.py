import os
import pickle

from PyQt6 import uic
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QWidget
from Paziente.Documenti.LetteraDiDimissione import LetteraDiDimisione
from Viste.Vista_Medico.Vista_Documenti.Vista_Lista_Lettera.VistaInfoLettera import VistaInfoLettera


class VistaListaLetteraDimissioni(QWidget):
    def __init__(self):
        super(VistaListaLetteraDimissioni,self).__init__()
        uic.loadUi('Viste/Vista_Medico/Vista_Documenti/Vista_Lista_Lettera/VistaListaLetteraDiDimissioneMedico.ui', self)
        self.update_pr()
        self.ButtonApri.clicked.connect(self.go_info_lettera)

    def load_Lettere(self):  # carichiamo dentro la lista dei pazienti

        if os.path.isfile('Dati_Sistema/LettereDiDimisioni.pickle'):
            with open('Dati_Sistema/LettereDiDimisioni.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.lettere.extend(current.values())

    def update_pr(self):
        self.lettere = []
        self.load_Lettere()
        listview_model = QStandardItemModel(self.listView)
        for lettera in self.lettere:
            item = QStandardItem()
            nome = f"{lettera.paziente.nome} {lettera.paziente.cognome} - {type(lettera).__name__} {lettera.codice}"
            item.setText(nome)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.listView.setModel(listview_model)

    def go_info_lettera(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            cf = int(selected.split("-")[1].strip().split(" ")[1])
            referto = LetteraDiDimisione().ricerca_referto_COD(cf)
            self.vista_info = VistaInfoLettera(referto, elimina_callback=self.update_pr)
            self.vista_info.show()
        except IndexError:
            return

