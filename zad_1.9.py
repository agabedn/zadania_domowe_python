"""
Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.
"""
i=1
while i <= 100:
    print(i)
    i+=1
    if i >= 3 and i % 3 == 0:
        print(f'Fizz {i}')
    elif i >= 5 and i % 5 == 0:
        print(f'Buzz {i}')
    elif i >=15 and i % 15 == 0:
        print(f'FizzBuzz {i}')
