import datetime
import os
import pickle
from Paziente.Paziente import Paziente


class Ricovero :
    def __init__(self):
        self.paziente=Paziente()
        self.dataRicovero=datetime.datetime(1970, 1, 1, 0, 0)
        self.diagnosi=""

    def aggiungi_Ricovero(self,paziente,dataRicovero,diagnosi):
        self.paziente=paziente
        self.dataRicovero=dataRicovero
        self.diagnosi=diagnosi
        ricovero = {}
        if os.path.isfile('Dati_Sistema/Ricoveri.pickle'):
            with open('Dati_Sistema/Ricoveri.pickle', 'rb') as f:
                ricovero = pickle.load(f)
        ricovero[paziente.cf] = self
        with open('Dati_Sistema/Ricoveri.pickle', 'wb') as f:
            pickle.dump(ricovero, f, pickle.HIGHEST_PROTOCOL)

    def get_Info_Ricovero(self):
       return  {
           "paziente":self.paziente,
           "dataRicovero":self.dataRicovero,
           "diagnosi":self.diagnosi
       }

    def ricerca_Ricovero_CF(self,cf):
        if os.path.isfile('Dati_Sistema/Ricoveri.pickle'):
            with open('Dati_Sistema/Ricoveri.pickle', 'rb') as f:
                ricovero = dict(pickle.load(f))
                return ricovero.get(cf, None)
        else:
            return None

    def rimuovi_Ricovero(self,cf):
        if os.path.isfile('Dati_Sistema/Ricoveri.pickle'):
            with open('Dati_Sistema/Ricoveri.pickle', 'rb') as f:
                ricoveri = dict(pickle.load(f))
                del ricoveri[cf]
            with open('Dati_Sistema/Ricoveri.pickle', 'wb') as f:
                pickle.dump(ricoveri, f, pickle.HIGHEST_PROTOCOL)
        self.paziente =None
        self.dataRicovero = datetime.datetime(1970, 1, 1, 0, 0)
        del self

    def numero_ricoveri(self):
        i=0
        if os.path.isfile('Dati_Sistema/Ricoveri.pickle'):
            with open('Dati_Sistema/Ricoveri.pickle', 'rb') as f:
                paziente = dict(pickle.load(f))
                for paziente in paziente.keys():
                    i=i+1
            return i
        else:
            return i
    def verifica_disponibilita(self):
        ricovero = Ricovero()
        if ricovero.numero_ricoveri() <50:
            return True
        else :
            return False



