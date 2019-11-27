"""
Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić. Niech program policzy i wyświetli,
ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
"""
kilo_ziemniakow = int(input('Ile kosztuje 1 kg ziemniakow: '))
ilosc_ziemniakow = int(input('Ile kg ziemniaków chcesz kupić?: '))
kilo_bananow = int(input('Ile kosztuje 1 kg bananów: '))
ilosc_bananow = int(input('Ile kg bananów chcesz kupić: '))
banany = kilo_bananow*ilosc_bananow
ziemniaki = kilo_ziemniakow*ilosc_ziemniakow
print(f'Za taką ilość ziemniaków {ilosc_ziemniakow} kg, będziesz musiał zapłacić {ziemniaki} zł')
print(f'Za taką ilość bananów {ilosc_bananow} kg, będziesz musiał zapłacić {banany} zł')

if ziemniaki > banany:
    print('Za ziemniaki trzeba będzie zapłacić więcej.')
else:
    print('Za banany trzeba zapłacić więcej niż za ziemniaki.')