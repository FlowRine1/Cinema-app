from Classes.Film import Film

class Animatie(Film):

    def __init__(self, titlu, durata, limba_dublaj):
        super().__init__(titlu, durata)
        self.limba_dublaj = limba_dublaj

    def returneaaza_limba_dublaj(self):
        return self.limba_dublaj

    def eroare_durata(self):
        super().eroare_durata()

