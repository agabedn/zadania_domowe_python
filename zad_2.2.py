"""
Napisz program, który wczytuje liczbę całkowitą,
a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
```

    *

  * * *

* * * * *

```
"""
zmienna = ''
liczba_calkowita = int(input('Podaj liczbe całkowitą: '))
j = 0
for i in range(1, liczba_calkowita +1):
    print((('*')*i + ('*')*j).center(liczba_calkowita * 2))
    i += 1
    j += 1