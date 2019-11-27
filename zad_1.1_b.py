"""
Potem napisz program, który prosi użytkownika (przez `input()`),
żeby podał, ile kosztuje kilo ziemniaków i ile kilo chce kupić.
 Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki.
"""
kilo_ziemniakow = int(input('Ile kosztuje 1 kg ziemniakow: '))
ilosc_ziemniakow = int(input('Ile kg ziemniaków chcesz kupić?: '))
print(f'Za taką ilość ziemniaków {ilosc_ziemniakow} kg, będziesz musiał zapłacić {kilo_ziemniakow*ilosc_ziemniakow} zł')