"""
2. Wyobraźmy sobie robota, który może poruszać się naprzód i obracać w lewo lub prawo.

    Napisz klasę Robot, która będzie przechowywała informację o położeniu robota na płaszczyźnie oraz

    kierumku w jakim jest zwrócony (N - północ, S - południe, E - wschód, W - zachód).

    Klasa powinna udostępniać metodę wykonaj() przyjmującą jako argument ciąg instrukcji złożony z liter

    N, P, L oznaczających odpowiednio: Naprzód, Prawo, Lewo.

    Znaczenie instrukcji:

     - Naprzód - przemieszcza robota krok w kierunku, w którym obecnie jest zwrócony (przykładowo krok na wschód

        powoduje zmianę współrzędnych z (x, y) na (x + 1, y)

     - Prawo - obraca robota o 90 stopni w prawo

     - Lewo - obraca robota o 90 stopni w lewo

    Wywołanie metody wykonaj() powinno przemieścić robota zgodnie z przekazanymi instrukcjami.

    Przykład:

    początkowe położenie robota: (0, 0), zwrot: N

    ciąg instrukcji: NNPNLNPP

    końcowe położenie robota: (1, 3), zwrot: S
"""
class Robot:
    def __init__(self):
        self.polozenie_x = 0
        self.polozenie_y = 0
        self.kierunek = 'N'
    def __str__(self):
        return f'({self.polozenie_x}, {self.polozenie_y}), zwrot {self.kierunek}'

    def naprzod(self):
        if self.kierunek == 'N':
            self.polozenie_y +=1
        if self.kierunek == 'S':
            self.polozenie_y -=1
        if self.kierunek == 'E':
            self.polozenie_x +=1
        if self.kierunek == 'W':
            self.polozenie_x -=1
    def w_prawo(self):
        if self.kierunek == 'N':
            self.kierunek = 'E'
        elif self.kierunek == 'S':
            self.kierunek = 'W'
        elif self.kierunek == 'E':
            self.kierunek = 'S'
        elif self.kierunek == 'W':
            self.kierunek = 'N'
    def w_lewo(self):
        if self.kierunek == 'N':
            self.kierunek = 'W'
        elif self.kierunek == 'S':
            self.kierunek = 'E'
        elif self.kierunek == 'E':
            self.kierunek = 'N'
        elif self.kierunek == 'W':
            self.kierunek = 'S'

    def wykonaj(self, instrukcja):

        for komenda in instrukcja:
            if komenda == 'L':
                self.w_lewo()
            if komenda == 'P':
                self.w_prawo()
            if komenda == 'N':
                self.naprzod()

robot = Robot()
instrukcje = 'NNPNLNPP'
print(f'polozenie poczatkowe: {robot}')
print(f'ciag instrukcji : {instrukcje}')
robot.wykonaj(instrukcje)
print(f'polozenie koncowe: {robot}')