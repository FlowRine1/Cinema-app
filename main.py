from core.AppCore import *

if __name__ == "__main__":
    """
    COMENZI:
    adauga_drama <titlu> <durata> <varsta>
    adauga_animatie <titlu> <durata> <limba_dublare>
    afisare - afiseaza toate filmele
    afisare_animatii
    alege_film
    salveaza_filme <nume_fisier>
    exit : iesirea din aplicatie
    
    -in cazul animatiilor nedublate, nu se va specifica nicio limba de dublare. 
    -in cazul salvarii fisierului, NU se va specifica si extensia documentului in care se va face salvarea.
    Aceasta este by default .txt
    """
    while True:
        comanda = input("Introduceti o comanda: ").split()
        if comanda[0] == "adauga_drama":
            try:
                adauga_drama(comanda)
            except ValueError as e:
                print(repr(e))
                print("Introduceti o valoare a duratei mai mica de 180 de minute!")
        elif comanda[0] == "adauga_animatie":
            try:
                adauga_animatie(comanda)
            except ValueError as e:
                print(repr(e))
                print("Introduceti o valoare a duratei mai mica de 180 de minute!")
        elif comanda[0] == "afisare":
            afisare()
        elif comanda[0] == "afisare_animatii":
            afisare_animatii()
        elif comanda[0] == "alege_film":
            alege_film()
        elif comanda[0] == "salveaza_filme":
            try:
                salveaza_filme(comanda[1])
                print("Filmele au fost salvate cu succes!")
            except IndexError:
                print("Nu ati introdus numele fisierului unde se doreste sa se faca salvarea!")
        elif comanda[0] == "exit":
            break
        else:
            print("Comanda nu este valida!")