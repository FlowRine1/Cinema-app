class Film(object):

    def __init__(self, titlu, durata):
        self.titlu = titlu
        self.durata = durata

    def eroare_durata(self):
        if int(self.durata) > 180:
            raise ValueError("Durata filmelor trebuie sa fie de cel mult 180 de minute!")


