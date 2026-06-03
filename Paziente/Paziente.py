import datetime
import os
import pickle

from PyQt6.QtWidgets import QMessageBox


class Paziente:
    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.cf = ""
        self.dataDiNascita = datetime.datetime(1970, 1, 1, 0, 0)
        self.luogoDiNascita=""
        self.sesso=""
        self.telefono=""
        self.residenza=""

    def aggiungi_Paziente(self, nome, cognome, cf,dataDiNascita , luogoDiNascita, sesso,telefono,residenza):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.dataDiNascita= dataDiNascita
        self.luogoDiNascita = luogoDiNascita
        self.sesso = sesso
        self.telefono=telefono
        self.residenza=residenza
        paziente = {}
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                paziente = pickle.load(f)
        paziente[cf] = self
        with open('Dati_Sistema/Pazienti.pickle', 'wb') as f:
            pickle.dump(paziente, f, pickle.HIGHEST_PROTOCOL)

    def get_Info_Paziente(self):
        return {
            "nome": self.nome,
            "cognome": self.cognome,
            "cf": self.cf,
            "dataDiNascita": self.dataDiNascita,
            "luogoDiNascita": self.luogoDiNascita,
            "sesso": self.sesso,
            "telefono":self.telefono,
            "residenza":self.residenza,
        }

    def ricerca_Paziente_NC(self, nome, cognome):
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                paziente = dict(pickle.load(f))
                for paziente in paziente.values():
                    if paziente.nome == nome and paziente.cognome == cognome:
                        return paziente
                return None
        else:
            return None

    def ricerca_Paziente_CF(self, CF):
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                paziente = dict(pickle.load(f))
                return paziente.get(CF, None)
        else:
            return None

    def rimuovi_Paziente(self):
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                paziente = dict(pickle.load(f))
                del paziente[self.cf]
            with open('Dati_Sistema/Pazienti.pickle', 'wb') as f:
                pickle.dump(paziente, f, pickle.HIGHEST_PROTOCOL)
        self.nome = ""
        self.cognome = ""
        self.cf = ""
        self.dataDiNascita = datetime.datetime(1970, 1, 1, 0, 0)
        self.luogoDiNascita = ""
        self.sesso = ""
        self.telefono=""
        self.residenza=""
        del self

    def stato_prenotazione_Paziente(self,paziente):
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as f:
                prenotazione = dict(pickle.load(f))
                if (prenotazione.get(paziente.cf, None)):
                    QMessageBox.critical(self, 'Errore', 'Paziente gia prenotato')
                    return False
                return True
        return True


    def stato_Ricovero_Paziente(self,paziente):
        if os.path.isfile('Dati_Sistema/Ricoveri.pickle'):
            with open('Dati_Sistema/Ricoveri.pickle', 'rb') as f:
                ricoveri = dict(pickle.load(f))
                if (ricoveri.get(paziente.cf, None)):
                    QMessageBox.critical(self, 'Errore', 'Paziente è ricoverato,non si può prenotare una visita')
                    return False
                return True
        return True


    def verifica_paziente_Registarti(self,cf):
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                pazienti = dict(pickle.load(f))
                if (pazienti.get(cf, None)):
                    return False
                return True
        return True



