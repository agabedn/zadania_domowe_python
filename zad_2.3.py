"""
Napisz program, który odczytuje od użytkownika wiele liczb.

Program powinien wyliczyć i na końcu wypisać następujące statystyki:

- liczba podanych liczb (ile sztuk),

- suma,

- średnia,

- minimum

- maksimum
"""
liczby = []
print('Podaj liczby, jeżeli będziesz chciał skończyć wpisz: koniec')
suma = 0
minimum = None
maximum = None
while True:
    liczba = input()
    if liczba == 'koniec':
        break
    else:
        liczby.append(liczba)
        continue
for znak in liczby:
    suma = int(znak) + suma
# minimum i maximum
for znak in liczby:
    if minimum is None or znak < minimum:
        minimum = znak
    if maximum is None or znak > maximum:
        maximum = znak


print(liczby)
print(f'Wprowadziłeś {len(liczby)} liczby')
print(f'Suma wprowadzonych liczb: {suma}')
print(f'Srednia z wprowadzonych liczb to: {suma/len(liczby)}')
print(f'Najmniejsza wprowadzona liczba to: {minimum}')
print(f'Największa wprowadzona liczba to: {maximum}')