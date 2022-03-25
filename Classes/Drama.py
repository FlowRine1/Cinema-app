from Classes.Film import Film

class Drama(Film):

    def __init__(self, titlu, durata, varsta_minima):
        super().__init__(titlu, durata)
        self.varsta_minima = varsta_minima

    def eroare_durata(self):
        super().eroare_durata()

