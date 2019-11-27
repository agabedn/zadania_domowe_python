"""
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.

Nawiasem mówiąc technika wyszukiwania oparta o "podpowiedzi" za dużo/za mało nazywa się bisekcją
i pełni w informatyce bardzo ważną rolę. Umiejętnie ją stosując powinno się te zagadki rozwiązywać w 9-10 próbach (bo 2^10=1024).
"""
from random import randint
liczba = randint(0, 999)
i = 0
j = 0
#print(liczba)
#liczba_zgadywana = int(input('Zgadnij liczbe z zakresu od 0 - 999 : '))

while True:
    liczba_zgadywana = int(input('Zgadnij liczbe z zakresu od 0 - 999 : '))
    if liczba_zgadywana == liczba:
        print('Zgadłes')
        break
    elif liczba_zgadywana > liczba:
        print('Liczba jest mniejsza')
        i+=1
        continue
    elif liczba_zgadywana < liczba:
        print('Liczba jest większa')
        j+=1
        continue


print(f'Odgadłeś za {i + j } razem')