import unittest
import rozgrzewka


class TestRozgrzewka(unittest.TestCase):

    def test_kolo_pole(self):
        self.assertEqual(rozgrzewka.Obiekty.kolo(1).pole, 3.14)
        self.assertEqual(rozgrzewka.Obiekty.kolo(5).pole, 78.54)
        self.assertEqual(rozgrzewka.Obiekty.kolo(10).pole, 314.16)

    def test_kula_pole(self):
        self.assertEqual(rozgrzewka.Obiekty.kula(1).pole, 12.57)
        self.assertEqual(rozgrzewka.Obiekty.kula(5).pole, 314.16)
        self.assertEqual(rozgrzewka.Obiekty.kula(10).pole, 1256.64)

    def test_kula_objetosc(self):
        self.assertEqual(rozgrzewka.Obiekty.kula(1).objetosc, 4.19)
        self.assertEqual(rozgrzewka.Obiekty.kula(5).objetosc, 523.6)
        self.assertEqual(rozgrzewka.Obiekty.kula(10).objetosc, 4188.79)

    def test_kwadrat_pole(self):
        self.assertEqual(rozgrzewka.Obiekty.kwadrat(1).pole, 1)
        self.assertEqual(rozgrzewka.Obiekty.kwadrat(5).pole, 25)
        self.assertEqual(rozgrzewka.Obiekty.kwadrat(10).pole, 100)

    def test_szescian_pole(self):
        self.assertEqual(rozgrzewka.Obiekty.szescian(1).pole, 6)
        self.assertEqual(rozgrzewka.Obiekty.szescian(5).pole, 150)
        self.assertEqual(rozgrzewka.Obiekty.szescian(10).pole, 600)

    def test_szescian_objetosc(self):
        self.assertEqual(rozgrzewka.Obiekty.szescian(1).objetosc, 1)
        self.assertEqual(rozgrzewka.Obiekty.szescian(5).objetosc, 125)
        self.assertEqual(rozgrzewka.Obiekty.szescian(10).objetosc, 1000)
