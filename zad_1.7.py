"""
Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena. Wyświetl odpowiedni komunikat.

Przykład:

Co chcesz kupić? - ziemniaki

Podaj cenę towaru - 5

Podaj ilość towaru - 10

Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
"""
towar = input('Co chcesz kupic? - ')
cena_towaru = int(input('Podaj cene towaru - '))
ilosc_towaru = int(input('Podaj ilość towaru - '))

print(f'Za towar czyli: {towar}, który chcesz kupić, zapłacisz {cena_towaru*ilosc_towaru} zł')