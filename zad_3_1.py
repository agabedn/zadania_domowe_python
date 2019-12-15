"""
### Zadanie 3.1 Funkcje liczbowe

Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,

2. `max` - zwraca większą z dwóch liczb,

3. `srednia` - oblicza średnią z dwóch liczb,

4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)

podpowiedź: wartość PI jest dostępna jako `Math.PI`

5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.

6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.

7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile

8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

​
"""

import math

def stopy_na_metry(odleglosc: float) -> float:
    metry = round(odleglosc/3.2808)
    return metry


def max(liczba: int, liczba2: int)-> int:
    if liczba >liczba2:
        return liczba
    else:
        return liczba2

def srednia(lista: list)->float:
    suma_liczb = 0
    for element in lista:
        suma_liczb = suma_liczb + element
        srednia = suma_liczb / len(lista)

    return round(srednia,2)


def pole_kola(promien: int) -> float:

    pi = 3.1415
    pole = pi*(promien**2)
    pole = round(pole,3)
    return pole

def bmi(wzrost:float,  waga:int)->float:
    bmi = float(waga / (wzrost ** 2))
    bmi = round(bmi,2)
    return bmi


def pole_trojkata(a: int, b: int, c: int) -> float:

    if a + b > c and a + c > b and b + c > a:
        pole = (((a + b + c) / 2) * ((((a + b + c) / 2) - a) * (((a + b + c) / 2) - b) * (((a + b + c) / 2) - c)))
        pole_trojkata = math.sqrt(pole)

        return round(pole_trojkata,2)
    else:
        raise TypeError("Z podanych liczb nie obliczysz pola trójkata")

def mile_na_km(km : float) -> float:
    mile = km * 0.621
    return  round(mile,2)

def km_na_mile(mile: float) -> float:
    km = mile * 1.6
    return round(km,2)




def test_stopy_na_metry():
    assert stopy_na_metry(40) == 12

def test_max():
    assert max(34, 56) == 56

def test_pole_kola():
    assert pole_kola(3) == 28.274

def test_bmi():
    assert bmi(1.70, 60) == 20.76

def test_pole_trojkata():
    assert pole_trojkata(3,4,5) == 6.0


def test_mile_na_km():
    assert mile_na_km(5) == 3.1

def test_km_na_mile():
    assert km_na_mile(4) == 6.4

def test_srednia():
    assert srednia([2,3,4,5,6]) == 4.0


print(pole_kola(3))
print(bmi(1.70, 60))
print(pole_trojkata(3,4,5))
print(mile_na_km(5))
print(km_na_mile(4))
print(srednia([2,3,4,5,6]))

print('Podaj wzrost i wage')
wzrost = float(input())
waga = int(input())
print(bmi(wzrost, waga))
