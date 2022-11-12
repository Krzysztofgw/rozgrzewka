# zad 1 Napisz klase ktora posiada metody klasowe wytwarzajace poszczegolne obiekty (Kolo, Kwadrat, Kula, Szescian)
# zad 2 Kazdy z tych obiektow ma miec sprecyzowane dane go dotyczace: objetosc, bok, wysokosc, metoda obliczajaca pole
# zad 3 Napisz podstawowe testy jednostkowe
# zad 4 calosc wrzuc do repozytorium GIT i przeslij link
import math


class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    @property
    def pole(self):
        return round(self.bok * self.bok, 2)

    @property
    def wysokosc(self):
        return self.bok


class Szescian:
    def __init__(self, bok):
        self.bok = bok

    @property
    def pole(self):
        return round(6 * self.bok * self.bok, 2)

    @property
    def wysokosc(self):
        return self.bok

    @property
    def objetosc(self):
        return round(self.bok ** 3, 2)


class Kolo:
    def __init__(self, promien):
        self.promien = promien

    @property
    def pole(self):
        return round(math.pi * self.promien ** 2, 2)


class Kula:
    def __init__(self, promien):
        self.promien = promien

    @property
    def pole(self):
        return round(4 * math.pi * self.promien ** 2, 2)

    @property
    def objetosc(self):
        return round( 4 / 3 * math.pi * self.promien ** 3, 2)


class Obiekty:
    @classmethod
    def kolo(cls, promien):
        return Kolo(promien)

    @classmethod
    def kwadrat(cls, bok):
        return Kwadrat(bok)

    @classmethod
    def kula(cls, promien):
        return Kula(promien)

    @classmethod
    def szescian(cls, bok):
        return Szescian(bok)


