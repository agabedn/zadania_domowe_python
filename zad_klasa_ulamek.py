"""
1. Napisz jak najwygodniejszą w użyciu klasę Ulamek. Z niezbędnych funkcjonalności:

    - wypisywanie (print(ulamek))

    - stworzenie ułamka z zerowym mianownikiem powinno być niemożliwe (wyjątek przy próbie ustawienia na 0)

    - jak najwięcej operatorów arytmetycznych. W szczególności: +, -(również __neg__()), *, /, +=, -=, *=, /= działające zarówno

        dla działań z innymi ułamkami jak i z liczbami całkowitymi (int). Gdzie ma to sens operacje powinny działać

        nawet jeżeli po lewej stronie działania jest wartość niebędąca ułamkiem (np. 3 * ulamek)

    - operatory logiczne: <, <=, >, >=, ==, != działające dla porówniań ułamka z ułamkiem, ułamka z intem i inta z ułamkiem

    - ułamek po każdej operacji powinien być w postaci nieskracalnej (tzn. 1/4 + 1/4 powinno dać w wyniku ułamek 1/2 a nie 2/4)
"""


from math import gcd
class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
        self.spr_mian()
        self._skrac()

    def _skrac(self):
        dzielnik = gcd(self.licznik,self.mianownik)
        self.licznik = int(self.licznik / dzielnik)
        self.mianownik = int(self.mianownik / dzielnik)


    def spr_mian(self):
        # print('spr_mian')
        if self.mianownik == 0:
           raise ZeroDivisionError
    def __str__(self):
        if self.licznik == self.mianownik:
            return "1"
        return f'{self.licznik}/{self.mianownik}'

    # def post_nieskr(self):
    #     if self.mianownik % self.licznik == 0:
    #
    #     pass

    def __add__(self, other):
        licznik_n = 0
        mianownik_n = 0
        licznik_n= ((self.licznik * other.mianownik)+(other.licznik*self.mianownik))
        mianownik_n =(self.mianownik*other.mianownik)
        nowy_ulamek = Ulamek(licznik_n, mianownik_n)
        return nowy_ulamek

    def __sub__(self, other):
        licznik_n = 0
        mianownik_n = 0
        licznik_n = ((self.licznik * other.mianownik) - (other.licznik * self.mianownik))
        mianownik_n = (self.mianownik * other.mianownik)
        nowy_ulamek = Ulamek(licznik_n, mianownik_n)
        return nowy_ulamek


    def __mul__(self, other):
        licznik_n = 0
        mianownik_n =0
        #nowy_ulamek = Ulamek()
        if type(other) == Ulamek:
            licznik_n= self.licznik*other.licznik
            mianownik_n= self.mianownik*other.mianownik

        if type(other) == int:
            licznik_n = self.licznik*other
            mianownik_n = self.mianownik
        nowy_ulamek = Ulamek(licznik_n,mianownik_n)
        return nowy_ulamek

    def __divmod__(self, other):
        licznik_n = 0
        mianownik_n = 0
        licznik_n = self.licznik * other.mianownik
        mianownik_n = self.mianownik * other.licznik
        nowy_ulamek  = Ulamek(licznik_n,mianownik_n)
        return nowy_ulamek

    def __iadd__(self, other):
        licznik_n = 0
        mianownik_n = 0
        licznik_n = self.licznik + self.licznik
        mianownik_n = self.mianownik
        nowy_ulamek = Ulamek(licznik_n, mianownik_n)
        return nowy_ulamek
    def __isub__(self, other):
        # licznik_n = 0
        # mianownik_n = 0
        # licznik_n = self.licznik - self.licznik
        # mianownik_n = self.mianownik - self.mianownik
        # nowy_ulamek = Ulamek(licznik_n, mianownik_n)
        return 0
    def __imul__(self, other):
        licznik_n = 0
        mianownik_n = 0
        # nowy_ulamek = Ulamek()
        if type(other) == Ulamek:
            licznik_n = self.licznik * other.licznik
            mianownik_n = self.mianownik * other.mianownik

        if type(other) == int:
            licznik_n = self.licznik * other
            mianownik_n = self.mianownik
        nowy_ulamek = Ulamek(licznik_n, mianownik_n)
        return nowy_ulamek

    def __idiv__(self, other):
        licznik_n = 0
        mianownik_n = 0
        licznik_n = self.licznik * other.mianownik
        mianownik_n = self.mianownik * other.licznik
        nowy_ulamek = Ulamek(licznik_n, mianownik_n)
        return nowy_ulamek



    def __lt__(self, other):
        # if type(other) == int:
        #     liczba1 = float(other)
        #     liczba2 = self.licznik/self.mianownik
        #     return liczba2 <liczba1
        # else:
            licznik_a = self.licznik * other.mianownik
            licznik_b = other.licznik * self.mianownik
            return licznik_a < licznik_b

    def __le__(self, other):
        licznik_a = self.licznik * other.mianownik
        licznik_b = other.licznik * self.mianownik
        return licznik_a <= licznik_b
    def __eq__(self, other):
        licznik_a = self.licznik * other.mianownik
        licznik_b = other.licznik * self.mianownik
        return licznik_a == licznik_b
    def __ne__(self, other):
        licznik_a = self.licznik * other.mianownik
        licznik_b = other.licznik * self.mianownik
        return licznik_a != licznik_b
    def __gt__(self, other):
        licznik_a = self.licznik * other.mianownik
        licznik_b = other.licznik * self.mianownik
        return licznik_a > licznik_b
    def __ge__(self, other):
        licznik_a = self.licznik * other.mianownik
        licznik_b = other.licznik * self.mianownik
        return licznik_a >= licznik_b








x = Ulamek(2,4)
y = Ulamek(1,4)
z = 2
print(f'{x} + {y} = {x+y} ')
print(f'{x} - {y} = {x.__sub__(y)}')
print(f'{x} * {z} = {x.__mul__(z)}')
print(f'{x} / {y} = {x.__divmod__(y)}')

print(y<x)
print(x<=y)
print(x==y)
print(x!=y)
print(x>=y)
print(x>y)
print(x.__iadd__(x))
print(x.__isub__(x))
print(x.__imul__(x))
print(x.__idiv__(x))
# print(z.__add__(y))