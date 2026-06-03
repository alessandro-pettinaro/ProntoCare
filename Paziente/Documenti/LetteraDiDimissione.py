import datetime
import os
import pickle
from Paziente.Paziente import Paziente

class LetteraDiDimisione:
    def __init__(self):
        self.paziente = Paziente()
        self.codice = 0
        self.controlliDaEffetuare = ""
        self.dataDimissione = datetime.datetime(1970, 1, 1, 0, 0)


    def create_lettera(self, paziente, codice, controlliDaEffetuare, dataDimissione):
        self.paziente = paziente
        self.codice = codice
        self.controlliDaEffetuare = controlliDaEffetuare
        self.dataDimissione = dataDimissione
        letteraDiDimisione = {}
        if os.path.isfile('Dati_Sistema/LettereDiDimisioni.pickle'):
            with open('Dati_Sistema/LettereDiDimisioni.pickle', 'rb') as f:
                letteraDiDimisione = pickle.load(f)
        letteraDiDimisione[codice] = self
        with open('Dati_Sistema/LettereDiDimisioni.pickle', 'wb') as f:
            pickle.dump(letteraDiDimisione, f, pickle.HIGHEST_PROTOCOL)

    def info_lettera(self):
        return {
            "paziente": self.paziente,
            "codice": self.codice,
            "controlliDaEffetuare": self.controlliDaEffetuare,
            "dataDimissione": self.dataDimissione
        }

    def ricerca__NC(self, nome, cognome):
        if os.path.isfile('Dati_Sistema/LettereDiDimisioni.pickle'):
            with open('Dati_Sistema/LettereDiDimisioni.pickle', 'rb') as f:
                letteraDiDimisione = dict(pickle.load(f))
                for letteraDiDimisione in letteraDiDimisione.values():
                    if letteraDiDimisione.paziente.nome == nome and letteraDiDimisione.paziente.cognome == cognome:
                        return letteraDiDimisione
                return None
        else:
            return None

    def numero_lettere(self):
        i=0
        if os.path.isfile('Dati_Sistema/LettereDiDimisioni.pickle'):
            with open('Dati_Sistema/LettereDiDimisioni.pickle', 'rb') as f:
                paziente = dict(pickle.load(f))
                for paziente in paziente.keys():
                    i=i+1
            return i
        else:
            return i

    def ricerca_referto_COD(self, codice):
        if os.path.isfile('Dati_Sistema/LettereDiDimisioni.pickle'):
            with open('Dati_Sistema/LettereDiDimisioni.pickle', 'rb') as f:
                letteraDiDimisione = dict(pickle.load(f))
                return letteraDiDimisione.get(codice, None)
        else:
            return None