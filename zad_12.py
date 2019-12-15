"""
Napisz program, który posortuje liczby w liście przy wykorzystaniu
algorytmu "sortowanie przez wybieranie".
"""
lista = [2,5,6,3,4,8,9,0]

i = 0
print(lista)
while i < len(lista):
    #print(i,"while")
    indeks_min = None
    for znak in range(i, len(lista)):
        if indeks_min is None or lista[znak] < lista[indeks_min]:
            indeks_min = znak
    #print((f'zmienia elementy lista[i]{lista[i]} lista[indeks_min]{lista[indeks_min]}'))
    lista[i], lista[indeks_min] = lista[indeks_min], lista[i]
    i += 1


print(lista)