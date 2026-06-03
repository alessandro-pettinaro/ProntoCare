import datetime
import os.path
import pickle
from unittest import TestCase

from Personale.Infermiere import Infermiere


class TestGestioneInfermieri(TestCase):

    def test_add_infermiere(self):
        self.infermiere = Infermiere()
        self.infermiere.aggiungi_Infermiere("laura","bianchi","PER23SDE234A","indermiere","luara11","binchi11",
                                            datetime.datetime(1989, 10, 20),"f")
        infermiere= None
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermiere = pickle.load(f)
        self.assertIsNotNone(infermiere)
        self.assertIn("PER23SDE234A", infermiere)

    def test_rimuovi_infermiere(self):
        infermieri = None
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermieri = pickle.load(f)
        self.assertIsNotNone(infermieri)
        self.assertIn("PER23SDE234A", infermieri)
        self.infermieri = Infermiere().ricerca_Infermiere_CF("PER23SDE234A")
        self.infermieri.rimuovi_Infermiere()
        if os.path.isfile('Dati_Sistema/Infermieri.pickle'):
            with open('Dati_Sistema/Infermieri.pickle', 'rb') as f:
                infermieri = pickle.load(f)
        self.assertIsNotNone(infermieri)
        self.assertNotIn("PER23SDE234A", infermieri)


