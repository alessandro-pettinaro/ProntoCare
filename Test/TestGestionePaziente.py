import datetime
import os.path
import pickle
from unittest import TestCase

from Paziente.Paziente import Paziente


class TestGestionePaziente(TestCase):

    def test_add_paziente(self):
        self.paziente = Paziente()
        self.paziente.aggiungi_Paziente("Alessio","Rossi","PERRE34EDF1G", datetime.datetime(1989, 10, 20),
                                        "roma","M","3245678221","roma")
        pazienti= None
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        self.assertIsNotNone(pazienti)
        self.assertIn("PERRE34EDF1G", pazienti)

    def test_rimuovi_paziente(self):
        pazienti = None
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        self.assertIsNotNone(pazienti)
        self.assertIn("PERRE34EDF1G", pazienti)
        self.pazienti = Paziente().ricerca_Paziente_CF("PERRE34EDF1G")
        self.pazienti.rimuovi_Paziente()
        if os.path.isfile('Dati_Sistema/Pazienti.pickle'):
            with open('Dati_Sistema/Pazienti.pickle', 'rb') as f:
                pazienti = pickle.load(f)
        self.assertIsNotNone(pazienti)
        self.assertNotIn("PERRE34EDF1G", pazienti)


