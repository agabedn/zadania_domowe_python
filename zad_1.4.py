"""
Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić. Zasady są takie:

- nieletni (poniżej 18 roku życia) płacą 100 zł za noc

- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:

	- 200 zł za noc, jeśli nocują jedną noc

	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy

	- 150 zł za noc, jeśli nocują pięć lub więcej nocy

- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki

Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy,
zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.
"""
print('****** OPłATA HOTELOWA ******')

wiek = int(input('Podaj swój wiek: '))
ilosc_nocy = int(input('Ile nocy spędzisz w hotelu?: '))
cena_pobytu = None
procent = None
if wiek <18 :
    cena_pobytu = ilosc_nocy * 100
    print(f'Za {ilosc_nocy} noce spedzone w hotelu zapłacisz {cena_pobytu}')
elif wiek >=18 and wiek <65:
    if ilosc_nocy ==1:
        cena_pobytu = 200
        print(f'Za {ilosc_nocy} noce spedzone w hotelu zapłacisz {cena_pobytu}')
    elif ilosc_nocy >=2 and ilosc_nocy < 5:
        cena_pobytu = ilosc_nocy * 180
        print(f'Za {ilosc_nocy} noce spedzone w hotelu zapłacisz {cena_pobytu}')
    elif ilosc_nocy >= 5:
        cena_pobytu = ilosc_nocy *150
        print(f'Za {ilosc_nocy} noce spedzone w hotelu zapłacisz {cena_pobytu}')
else:
    if wiek > 65 or wiek == 65:
        if ilosc_nocy == 1:
            procent = ((10 / 100) * 200)
            cena_za_noc = 200 - procent
            cena_pobytu = (ilosc_nocy * cena_za_noc)
            print(f'Za {ilosc_nocy} noce spedzone w hotelu zapłacisz {cena_pobytu}')
        elif ilosc_nocy >=2 and ilosc_nocy < 5:
            procent = ((10/100)* 180)
            cena_za_noc = 180 - procent
            cena_pobytu = (ilosc_nocy * cena_za_noc)
            print(f'Za {ilosc_nocy} noce spedzone w hotelu zapłacisz {cena_pobytu}')
        elif ilosc_nocy >= 5:
            procent = ((10/100)* 150)
            cena_za_noc = 150 - procent
            cena_pobytu = (ilosc_nocy * cena_za_noc)
            print(f'Za {ilosc_nocy} noce spedzone w hotelu zapłacisz {cena_pobytu}')

