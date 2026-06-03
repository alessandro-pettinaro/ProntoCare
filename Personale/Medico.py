import os.path
import pickle
import datetime

class Medico:
    def __init__(self):
        self.nome=""
        self.cognome=""
        self.cf=""
        self.ruolo=""
        self.username=""
        self.password=""
        self.sesso = ""
        self.dataDiNascita = datetime.datetime(1970, 1, 1, 0, 0)

    def aggiungi_Medico(self,nome,cognome,cf,ruolo,username,password,sesso,dataDiNascita):
        self.nome=nome
        self.cognome=cognome
        self.cf=cf
        self.ruolo=ruolo
        self.username=username
        self.password=password
        self.sesso=sesso
        self.dataDiNascita=dataDiNascita
        medico={}
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle','rb') as f:
                medico=pickle.load(f)
        medico[cf]=self
        with open('Dati_Sistema/Medici.pickle','wb') as f:
            pickle.dump(medico,f,pickle.HIGHEST_PROTOCOL)
            
    def get_Info_Medico(self):
        return {
           "nome":self.nome,
           "cognome":self.cognome,
           "cf":self.cf,
           "ruolo":self.ruolo,
           "username":self.username,
           "password":self.password,
            "sesso": self.sesso,
            "dataDiNascita": self.dataDiNascita
        }
            

    def ricerca_medico_NC(self,nome,cognome):
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle','rb') as f:
                medico=dict(pickle.load(f))
                for medico in medico.values():
                    if medico.nome==nome and medico.cognome==cognome:
                        return medico
                return None
        else:
            return  None

    def ricerca_Medico_CF(self, CF):
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle', 'rb') as f:
                medico = dict(pickle.load(f))
                return medico.get(CF, None)
        else:
            return None


    def rimuovi_Medico(self):
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle','rb') as f:
                medico=dict(pickle.load(f))
                del medico[self.cf]
            with open('Dati_Sistema/Medici.pickle','wb') as f:
                pickle.dump(medico,f,pickle.HIGHEST_PROTOCOL)
        self.nome = ""
        self.cognome = ""
        self.cf = ""
        self.ruolo = ""
        self.username = ""
        self.password = ""
        self.sesso = ""
        self.dataDiNascita = ""
        del self

    def ricerca_Medico_username(self,username):
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle', 'rb') as f:
                medico = dict(pickle.load(f))
                for medico in medico.values():
                    if medico.username == username:
                        return medico
                return None
        else:
            return None
