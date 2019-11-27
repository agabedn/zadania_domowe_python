"""
Założenia:

	- 0-6   - wiek przedszkolny - cena biletu: 0

	- 7-17  - wiek szkolny      - cena biletu: 2.28

	- 18-64 - wiek dorosły      - cena biletu: 3.80

	- +65   - wiek emerytalny   - cena biletu: 1.90

Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.

Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
"""
wiek = int(input('Podaj wiek osoby kupującej bilet: '))
ilosc_biletow = int(input('Ile biletów chcesz kupić?: '))

if wiek <=6:
    print('Wchodzisz za darmo')
elif wiek >= 7 and wiek <= 17:
    print(f'Za {ilosc_biletow} bilety zapłacisz: {ilosc_biletow * 2.28} zł')
elif wiek >=18 and wiek <=64:
    print((f'Za {ilosc_biletow} bilety zapłacisz: {ilosc_biletow * 3.80} zł'))
else:
    wiek >=65
    print((f'Za {ilosc_biletow} bilety zapłacisz: {ilosc_biletow * 1.90} zł'))