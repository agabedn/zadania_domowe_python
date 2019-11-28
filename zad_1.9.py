"""
Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.
"""
for i in range(1, 101):
    print(i)
    if i % 3 == 0:
        print(f'Fizz')
    if i % 5 == 0:
        print('Buzz')
    if i % 15 == 0:
        print('FizzBuzz')
    i += 1