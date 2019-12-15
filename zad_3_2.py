"""
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
Logikę obliczania liczby dni wydziel do osobnej funkcji.

**Wersja A**

Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

**Wersja B (trudniejsza)**

Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.

"""



def miesiace_roku(miesiac_podany: str) -> int:
    miesiace = {
        'styczeń': 31,
        'luty': 28,
        'marzec': 31,
        'kwiecień': 30,
        'maj': 31,
        'czerwiec': 30,
        'lipiec': 31,
        'sierpień': 31,
        'wrzesień': 30,
        'pażdziernik': 31,
        'listopad': 30,
        'grudzień': 31,

    }
    if miesiac_podany not in miesiace:
        print(f'Nie ma takiego miesiąca')
        exit()
    if miesiac_podany == 'luty':
        rok = int(input('Podaj rok:'))
        if rok % 4 == 0 and  rok % 100 != 0:
            miesiace[miesiac_podany] = 29

    print(f'Miesiąc który podałeś: {miesiac_podany} ma {miesiace[miesiac_podany] } dni')

miesiac_podany_przez_uzytkownika = str(input('Podaj miesiąc: '))
miesiac_podany_przez_uzytkownika = miesiac_podany_przez_uzytkownika.lower()
miesiace_roku(miesiac_podany_przez_uzytkownika)