from Classes.Drama import Drama
from Classes.Animatie import Animatie
from Classes.Cinematograf import Cinematograf
import random

lista_drama = list()
lista_animatie = list()
film_animatie = ''

def adauga_drama(cmd):
    global lista_drama
    drama_dict = {}
    try:
        drama_dict['titlu'] = cmd[1]
        try:
            drama_dict['durata'] = int(cmd[2])
        except ValueError:
            print("Durata trebuie sa fie un numar!")
            return 0
        try:
            drama_dict['varsta'] = int(cmd[3])
        except ValueError:
            print("Varsta trebuie sa fie un numar!")
            return 0
    except IndexError:
        print("Nu ati introdus toate caracteristicile specifice dramei!")
        return 0
    film_drama = Drama(drama_dict['titlu'], drama_dict['durata'], drama_dict['varsta'])
    film_drama.eroare_durata()
    lista_drama.append(film_drama)
    print("Drama a fost adaugata cu succes!")
    return lista_drama

def adauga_animatie(cmd):
    global lista_animatie, film_animatie
    animatie_dict = {}
    try:
        animatie_dict['titlu'] = cmd[1]
        try:
            animatie_dict['durata'] = int(cmd[2])
        except ValueError:
            print("Durata trebuie sa fie un numar!")
            return 0
        if len(cmd) == 4:
            animatie_dict['limba'] = cmd[3]
            film_animatie = Animatie(animatie_dict['titlu'], animatie_dict['durata'], animatie_dict['limba'])
        elif len(cmd) == 3:
            film_animatie = Animatie(animatie_dict['titlu'], animatie_dict['durata'], "")
    except IndexError:
        print("Nu ati introdus toate caracteristicile specifice animatiei!")
        return 0
    film_animatie.eroare_durata()
    lista_animatie.append(film_animatie)
    print("Animatia a fost aduagata cu succes!")
    return lista_animatie

def afisare():
    global lista_animatie, lista_drama
    for film_drama in lista_drama:
        print(f"titlu: {film_drama.titlu}, durata: {film_drama.durata} minute,"
              f" varsta minima: {film_drama.varsta_minima} ani")
    for film_animatie in lista_animatie:
        print(f"titlu: {film_animatie.titlu}, durata: {film_animatie.durata} minute,"
              f" limba dublaj: {film_animatie.limba_dublaj}")

def afisare_animatii():
    global lista_animatie
    for film_animatie in lista_animatie:
        print(f"titlu: {film_animatie.titlu}, durata: {film_animatie.durata} minute,"
              f" limba dublaj: {film_animatie.limba_dublaj}")

def alege_film():
    global lista_animatie
    global lista_drama
    filme = Cinematograf(lista_drama + lista_animatie)
    try:
        film_random = random.choice(filme.lista_filme)
    except IndexError:
        print("Lista de filme este goala!")
        return 0
    if film_random in lista_drama:
        print(f"Un film random pentru tine: {film_random.titlu}, durata: {film_random.durata} minute,"
              f" varsta minima: {film_random.varsta_minima} ani")
    elif film_random in lista_animatie:
        print(f"Un film random pentru tine: {film_random.titlu}, durata: {film_random.durata},"
              f" varsta minima: {film_random.limba_dublaj}")

def salveaza_filme(nume_fisier):
    global lista_animatie, lista_drama
    filme = Cinematograf(lista_drama + lista_animatie)
    with open(file=nume_fisier, mode="wt") as fisier_filme:
        for film in filme.lista_filme:
            if film in lista_drama:
                fisier_filme.write(f"Titlu: {film.titlu}, durata: {film.durata} minute,"
                                   f" varsta minima: {film.varsta_minima} ani\n")
            elif film in lista_animatie:
                fisier_filme.write(f"Titlu: {film.titlu}, durata: {film.durata},"
                                   f" limba dublaj: {film.limba_dublaj}\n")