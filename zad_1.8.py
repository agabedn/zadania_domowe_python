"""
Zakładamy, że 1 ludzki rok, to 5 lat psich.
Za pomocą konsoli wczytaj imię i wiek psa.
Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
Przykład:

Podaj imię psa - Burek

Podaj wiek psa - 3

Gdyby Burek był człowiekiem, miałby 15 lat.
"""
print('***** Kalkulator lat psich *****')

imie_psa = input('Podaj imie psa - ')
wiek_psa = int(input('Podaj wiek psa - '))

print(f'Gdyby {imie_psa} był człowiekime, miałby {wiek_psa * 5} lat.')