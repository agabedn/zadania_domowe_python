"""
Program, który odczytuje trzy liczby,
sprawdza czy liczby te mogą stanowić boki trójkąta (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?),
a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.

Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).

Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:


```
import math

x = math.sqrt(10)

```
"""
import math

#pole_trojkata = None
#polowa_obwodu = None
pole = None

print(f'Podaj trzy liczby, w kolejności: a, b, c')
a = int(input())
b = int(input())
c = int(input())
print(f'Podaleś takie liczby: a = {a} b = {b} c = {c}')

if a + b > c and a + c > b and b + c > a:
    print('Z podanych liczb można obliczyć pole trójkąta')
    polowa_obwodu= (a+b+c) / 2
    #print(polowa_obwodu)
    pole = (polowa_obwodu*((polowa_obwodu-a)*(polowa_obwodu-b)*(polowa_obwodu-c)))
    #print(pole)
    pole_trojkata = math.sqrt(pole)
    print(f'Pole trójkąta wynosi: {pole_trojkata}')
else:
    print('Z podanych liczb nie można zbudowć trójkąta')