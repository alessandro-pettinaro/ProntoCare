import datetime
import os
import pickle


class GestoreBackup:
    def __init__(self, ora,minuti):
        self.ora = ora
        self.minuti=minuti

    def backup(self):
            now = datetime.datetime.now()
            if now.hour == self.ora and now.minute== self.minuti:
                self.copy_data()
    def copy_data(self):
        self.copy_amministratore()
        self.copy_pazienti()
        self.copy_infermieri()
        self.copy_lettere()
        self.copy_medici()
        self.copy_prenotazioni()
        self.copy_referti()
        self.copy_ricoveri()

    def copy_pazienti(self):
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):

                with open('Dati_Sistema/Pazienti.pickle', 'rb') as file_origine:
                    dati_origine = pickle.load(file_origine)

                with open('Backup/Dati_Backup/Pazienti_Backup.pickle', 'wb') as file_destinazione:
                    pickle.dump(dati_origine, file_destinazione)

    def copy_infermieri(self):
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as file_origine:
                dati_origine = pickle.load(file_origine)

            with open('Backup/Dati_Backup/Infermieri_Backup.pickle', 'wb') as file_destinazione:
                pickle.dump(dati_origine, file_destinazione)

    def copy_medici(self):
        if os.path.isfile('Dati_Sistema/Medici.pickle'):
            with open('Dati_Sistema/Medici.pickle', 'rb') as file_origine:
                dati_origine = pickle.load(file_origine)

            with open('Backup/Dati_Backup/Medici_Backup.pickle', 'wb') as file_destinazione:
                pickle.dump(dati_origine, file_destinazione)


    def copy_prenotazioni(self):
        if os.path.isfile('Dati_Sistema/Prenotazioni.pickle'):
            with open('Dati_Sistema/Prenotazioni.pickle', 'rb') as file_origine:
                dati_origine = pickle.load(file_origine)

            with open('Backup/Dati_Backup/Prenotazioni_Backup.pickle', 'wb') as file_destinazione:
                pickle.dump(dati_origine, file_destinazione)


    def copy_referti(self):
        if os.path.isfile('Dati_Sistema/Referti.pickle'):
            with open('Dati_Sistema/Referti.pickle', 'rb') as file_origine:
                dati_origine = pickle.load(file_origine)

            with open('Backup/Dati_Backup/Referti_Backup.pickle', 'wb') as file_destinazione:
                pickle.dump(dati_origine, file_destinazione)

    def copy_lettere(self):
        if os.path.isfile('Dati_Sistema/LettereDiDimisioni.pickle'):
            with open('Dati_Sistema/LettereDiDimisioni.pickle', 'rb') as file_origine:
                dati_origine = pickle.load(file_origine)

            with open('Backup/Dati_Backup/LettereDiDimisioni_Backup.pickle', 'wb') as file_destinazione:
                pickle.dump(dati_origine, file_destinazione)

    def copy_amministratore(self):
        if os.path.isfile('Dati_Sistema/Amministratore.pickle'):
            with open('Dati_Sistema/Amministratore.pickle', 'rb') as file_origine:
                dati_origine = pickle.load(file_origine)

            with open('Backup/Dati_Backup/Amministratore_Backup.pickle', 'wb') as file_destinazione:
                pickle.dump(dati_origine, file_destinazione)

    def copy_ricoveri(self):
        if os.path.isfile('Dati_Sistema/Ricoveri.pickle'):
            with open('Dati_Sistema/Ricoveri.pickle', 'rb') as file_origine:
                dati_origine = pickle.load(file_origine)

            with open('Backup/Dati_Backup/Ricoveri_Backup.pickle', 'wb') as file_destinazione:
                pickle.dump(dati_origine, file_destinazione)



