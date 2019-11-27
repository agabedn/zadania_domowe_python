"""
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1, wtorek to dzień 2 itp.).
Ma też podać, ile dni będzie trwała naprawa.

Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.
"""

dzien_oddania_butow = input('W który dzień tygodnia oddałeś buty do szewca?: ')
dzien_oddania_butow = dzien_oddania_butow.lower()
dzien_naprawy = 0

if dzien_oddania_butow == 'poniedziałek':
    dzien_naprawy =1
elif dzien_oddania_butow == 'wtorek':
    dzien_naprawy = 2
elif dzien_oddania_butow == 'środa':
    dzien_naprawy = 3
elif dzien_oddania_butow == 'czwartek':
    dzien_naprawy = 4
elif dzien_oddania_butow == 'piątek':
    dzien_naprawy = 5
#elif dzien_oddania_butow == 'sobota':
#    dzien_naprawy = 6
#elif dzien_oddania_butow =='niedziela':
#    dzien_naprawy = 7
elif dzien_oddania_butow == 'sobota' or dzien_oddania_butow == 'niedziela':
    print('W soboty i niedzielę szewc jest zamknięty')
    exit()
else:
    print('Nie ma takiego dnia w tygodniu')
    exit()
dlugosc_naprawy = int(input('Ile dni ma trwać naprawa: '))
dzien_odbioru = ((dzien_naprawy + dlugosc_naprawy) % 5)
#print(dzien_odbioru)

if dzien_odbioru == 1:
    print('Buty do odbioru będą w poniedzialek')
elif dzien_odbioru == 2:
    print('Buty do odbioru będą we wtorek')
elif dzien_odbioru == 3:
    print('Buty do odbioru będą w sroda')
elif dzien_odbioru == 4:
    print('Buty do odbioru będą w czwartek')
elif dzien_odbioru == 5:
    print('Buty do odbioru będą w piątek')
elif dzien_odbioru == 6:
    print('Buty do odbioru będą w poniedziałek')
elif dzien_odbioru == 7:
    print('Buty do odbioru będą w poniedziałek')
elif dzien_odbioru == 0:
    print('Buty do odbioru będą w poniedziałek')