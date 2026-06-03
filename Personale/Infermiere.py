import os
import pickle
import datetime


class Infermiere:
    def __init__(self):
        self.nome = ""
        self.cognome = ""
        self.cf = ""
        self.ruolo = ""
        self.username = ""
        self.password = ""
        self.sesso=""
        self.dataDiNascita = datetime.datetime(1970, 1, 1, 0, 0)

    def aggiungi_Infermiere(self, nome, cognome, cf, ruolo, username, password,dataDiNascita,sesso):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.ruolo = ruolo
        self.username = username
        self.password = password
        self.dataDiNascita=dataDiNascita
        self.sesso=sesso
        infermiere = {}
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermiere = pickle.load(f)
        infermiere[cf] = self
        with open('Dati_Sistema/Infermieri.pickle', 'wb') as f:
            pickle.dump(infermiere, f, pickle.HIGHEST_PROTOCOL)

    def get_Info_Infermiere(self):
       return  {
           "nome":self.nome,
           "cognome":self.cognome,
           "cf":self.cf,
           "ruolo":self.ruolo,
           "username":self.username,
           "password":self.password,
           "sesso":self.sesso,
           "dataDiNascita": self.dataDiNascita
       }

    def ricerca_Infermiere_NC(self, nome, cognome):
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermiere = dict(pickle.load(f))
                for infermiere in infermiere.values():
                    if infermiere.nome == nome and infermiere.cognome == cognome:
                        return infermiere
                return None
        else:
            return None


    def rimuovi_Infermiere(self):
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermiere = dict(pickle.load(f))
                del infermiere[self.cf]
            with open('Dati_Sistema/Infermieri.pickle', 'wb') as f:
                pickle.dump(infermiere, f, pickle.HIGHEST_PROTOCOL)
        self.nome = ""
        self.cognome = ""
        self.cf = ""
        self.ruolo = ""
        self.username = ""
        self.password = ""
        self.sesso=""
        self.dataDiNascita=""
        del self
   

    def ricerca_Infermiere_CF(self, CF):
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermiere = dict(pickle.load(f))
                return infermiere.get(CF, None)
        else:
            return None

    def ricerca_Infermiere_username(self,username):
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermiere = dict(pickle.load(f))
                for infermiere in infermiere.values():
                    if infermiere.username == username:
                        return infermiere
                return None
        else:
            return None
