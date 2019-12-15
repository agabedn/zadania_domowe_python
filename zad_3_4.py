"""Napisz
dekorator
`crazy_case`, który
co
drugą
literę
w
słowie
będzie
zamieniał
na
dużą.

​

```python
"""
def crazy_case(funkcja_do_udekorowania):

   def wrapper(*args, **kwargs):
        wynik = funkcja_do_udekorowania(*args, **kwargs)
        wynik = wynik.lower()
        nowy_string = ''
        dlugosc = len(wynik)
        indeks = 0
        parzysta = (dlugosc % 2 == 0)
        if not parzysta:
            wynik += ('!')

        while indeks < len(wynik):
            nowy_string += wynik[indeks] + wynik[indeks+1].upper()
            indeks+=2
        nowy_string = nowy_string[:-1]

        return nowy_string
   return wrapper
#print(zmiana_napisu('Ala ma kota'))



@crazy_case
def powiedz_ala():
    return 'Ala ma kota'


print(powiedz_ala())  # aLa mA KoTa