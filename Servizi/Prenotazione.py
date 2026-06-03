import os
import pickle
import datetime
from Paziente.Paziente import Paziente

class Prenotazione:
    def __init__(self):
        self.paziente=Paziente()
        self.codiceDiEmergenza=0
        self.sintomi=""
        self.dataPrenotazione=datetime.datetime(1970, 1, 1, 0, 0)

    def aggiungi_Prenotazione(self, paziente, codiceDiEmergenza, sintomi, dataPrenotazione):
        self.paziente = paziente
        self.codiceDiEmergenza = codiceDiEmergenza
        self.sintomi = sintomi
        self.dataPrenotazione = dataPrenotazione
        prenotazione = {}
        cf= paziente.cf
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as f:
                prenotazione = pickle.load(f)
        prenotazione[cf] = self
        with open('Dati_Sistema/Prenotazioni.pickle','wb') as f:
            pickle.dump(prenotazione, f, pickle.HIGHEST_PROTOCOL)

    def get_Info_Prenotazione(self):
       return  {
           "paziente":self.paziente,
           "codiceDiEmergenza":self.codiceDiEmergenza,
           "sintomi":self.sintomi,
           "dataPrenotazione":self.dataPrenotazione
       }

    def ricerca_Prenotazione_CF(self,cf):
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as f:
                prenotazione = dict(pickle.load(f))
                return prenotazione.get(cf, None)
        else:
            return None

    def rimuovi_Prenotazione(self,cf):
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as f:
                prenotazione = dict(pickle.load(f))
                del prenotazione[cf]
            with open('Dati_Sistema/Prenotazioni.pickle', 'wb') as f:
                pickle.dump(prenotazione, f, pickle.HIGHEST_PROTOCOL)
        self.paziente =None
        self.codiceDiEmergenza =0
        self.sintomi = ""
        self.dataDiNascita = datetime.datetime(1970, 1, 1, 0, 0)
        del self
