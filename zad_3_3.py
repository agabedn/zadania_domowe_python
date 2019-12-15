"""
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

```

lista_liczb = [10, 20, 30, 40]

wynik = suma(lista_liczb)

```
- `suma(liczby)` - zwraca sumę liczb z listy `liczby`

- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`

- `max(liczby)` – zwraca największą wartość z listy `liczby`

- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta

- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`

- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma

- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`

- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`

- `wypisz_podzielne(tab, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`

- `pierwsza_podzielna(tab, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma

- `ile_wiekszych(tab, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`

- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma

​
"""

def suma(liczby : list) -> int:
    suma_liczb = 0
    for element in liczby:
        suma_liczb += element

    return suma_liczb

def srednia(liczby: list) -> float:

    srednia = suma(liczby)/len(liczby)
    return srednia

def max(liczby: list) -> int:
    element_max = None
    for element, wartosc in enumerate(liczby):
        if element_max is None or wartosc > liczby[element_max]:
            element_max = element
            max_element = liczby[element]
    return max_element

def roznica_min_max(liczby: list) -> float:
    if liczby == []:
        #print('0')
        return None
    element_max = None
    element_min = None
    for element, wartosc in enumerate(liczby):
        if element_max is None or wartosc > liczby[element_max]:
            element_max = element
        if element_min is None or wartosc < liczby[element_min]:
            element_min = element
    roznica = liczby[element_max] - liczby[element_min]
    # print(f'max w liście to : {liczby[element_max]}')
    # print(f'min w liście to : {liczby[element_min]}')
    #print(f'Różnica min i max z tablicy to: {liczby[element_max] - liczby[element_min]}')
    return roznica

def wypisz_wieksze_liczby(liczby: list, x: int) ->list:
    wieksze_od_x = list()
    for element, wartosc in enumerate(liczby):
        if wartosc > x:
            wieksze_od_x.append(wartosc)
    return wieksze_od_x
            #print(f'Liczby większe od {x} to {wartosc}')



def pierwsza_wieksza(liczby: list, x: int) ->int:
    for element, wartosc in enumerate(liczby):
        if wartosc > x:
            return wartosc

def suma_wiekszych(liczby: list, x: int) -> int:
    suma = 0
    for element, wartosc in enumerate(liczby):
        if wartosc > x:
            suma  = wartosc + suma
    return suma

def ile_wiekszych(liczby: list, x: int)->int:
    licznik_wiekszych = 0
    for element, wartosc in enumerate(liczby):
        if wartosc > x:
            licznik_wiekszych +=1
    return licznik_wiekszych

def wypisz_podzielne(liczby: list, x: int) ->list:
    podzielne = list()
    for element, wartosc in enumerate(liczby):
        if wartosc % x == 0:
            podzielne.append(wartosc)
            #print(liczby[element])
    return  podzielne

def pierwsza_podzielna(liczby:list, x: int) -> int:
    for element, wartosc in enumerate(liczby):
        if wartosc % x == 0:
            return wartosc
        if wartosc % x == 0:
            return None

# def ile_wiekszych(liczby: list, x: int) -> int:
#     licznik = 0
#     for element, wartosc in enumerate(liczby):
#         if liczby[element] > x:
#             licznik +=1
#     return licznik

def znajdz_wspolny(liczby1:list, liczby2:list)->int:
    zmienna = 0
    for element in liczby1:
        for element2 in liczby2:
            if element == element2:
                return element
    #return set(liczby1) & set(lista_liczb2)

def test_suma():
    assert suma([3, 20, 30, 40, 50]) == 143

def test_srednia():
    assert srednia([1, 20, 4, 45, 60]) == 26.0

def test_max():
    assert max([3, 20, 30, 40, 50]) == 50

def test_roznica_min_i_max():
    assert roznica_min_max([3, 20, 30, 40, 50]) == 47

def test_wypisz_wieksze_liczby():
    assert wypisz_wieksze_liczby([3, 20, 30, 40, 50], 20) == [30, 40, 50]

def test_pierwsza_wieksza():
    assert pierwsza_wieksza([3, 20, 30, 40, 50], 20) == 30

def test_suma_wiekszych():
    assert suma_wiekszych([3, 20, 30, 40, 50], 28)== 120

def test_wypisz_odzielne():
    assert wypisz_podzielne([3, 20, 30, 40, 50], 4) == [20, 40]

def test_pierwsza_podzielna():
    assert pierwsza_podzielna([3, 20, 30, 40, 50], 1) == 3

def test_ile_wiekszych():
    assert ile_wiekszych([3, 20, 30, 40, 50], 20 ) == 3

def test_znajdz_wspolny():
    assert znajdz_wspolny([3, 20, 30, 40, 50], [1, 20, 4, 45, 60]) == 20



lista_liczb = [3, 20, 30, 40, 50]
lista_liczb2 = [1, 20, 4, 45, 60]
print(suma(lista_liczb))
print(srednia(lista_liczb2))
print(max(lista_liczb))
print(roznica_min_max(lista_liczb))
print(wypisz_wieksze_liczby(lista_liczb, 4))
print(pierwsza_wieksza(lista_liczb, 10))
print(suma_wiekszych(lista_liczb, 23))
print(ile_wiekszych(lista_liczb, 20))
print(wypisz_podzielne(lista_liczb, 4))
print(pierwsza_podzielna(lista_liczb, 1))
print(znajdz_wspolny(lista_liczb, lista_liczb2))