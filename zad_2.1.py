"""
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej).
Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
"""
from random import randint

a = randint(0,99)
b = randint(0,99)

#print (a+b)
print(f'Ile wynosi suma {a} i {b} : ')
wynik = int(input())
suma= a + b

while True:
    if suma == wynik:
        print('Dobrze obliczyłeś')
        break
    else:
        print('Żle obliczyleś, podaj sume liczb jeszcze raz')
        wynik = int(input())
        continue
