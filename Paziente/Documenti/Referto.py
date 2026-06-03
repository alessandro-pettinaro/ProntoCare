import os
import pickle
import datetime
from Paziente.Paziente import Paziente
from Servizi import Prenotazione
class Referto:
    def __init__(self):
        self.paziente=Paziente()
        self.codice=0
        self.codiceDiEmergenza=0
        self.diagnosi=""
        self.dataReferto=datetime.datetime(1970, 1, 1, 0, 0)

    def create_referto(self,paziente,codice,codiceDiEmergenza,diagnosi,dataReferto):
        self.paziente=paziente
        self.codice=codice
        self.codiceDiEmergenza=codiceDiEmergenza
        self.diagnosi=diagnosi
        self.dataReferto=dataReferto
        referto = {}
        if os.path.isfile('Dati_Sistema/Referti.pickle'):
            with open('Dati_Sistema/Referti.pickle', 'rb') as f:
                referto = pickle.load(f)
        referto[codice] = self
        with open('Dati_Sistema/Referti.pickle', 'wb') as f:
            pickle.dump(referto, f, pickle.HIGHEST_PROTOCOL)

    def info_referto(self):
        return {
            "paziente": self.paziente,
            "codice": self.codice,
            "diagnosi": self.diagnosi,
            "dataReferto": self.dataReferto,
            "codiceDiEmergenza":self.codiceDiEmergenza
                }

    def ricerca_referto_NC(self,nome,cognome):
        if os.path.isfile('Dati_Sistema/Referti.pickle'):
            with open('Dati_Sistema/Referti.pickle', 'rb') as f:
                referto = dict(pickle.load(f))
                for referto in referto.values():
                    if referto.paziente.nome == nome and referto.paziente.cognome == cognome:
                        return referto
                return None
        else:
            return None

    def ricerca_referto_COD(self,cod):
        if os.path.isfile('Dati_Sistema/Referti.pickle'):
            with open('Dati_Sistema/Referti.pickle', 'rb') as f:
                referto = dict(pickle.load(f))
                for referto in referto.values():
                    if referto.codice == cod:
                        return referto
                return print("no")
        else:
            return None
