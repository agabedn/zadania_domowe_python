"""
Napisz trzy programy, które dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypiszą współczynnik BMI,
oraz podsumowanie informujące o stanie/zaleceniach.
(Informacje o BMI: wzór, interpretację wyników, proszę znaleźć samodzielnie).
Programy mają różnić się sposobem interakcji z użytkownikiem.
"""
# BMI = masa/(wzrost)**2
# <18 - niedowaga
# 18-24-waga normalna
# 25-30 -nadwaga
# 30-35 - otyłość 1 stopien
# 35-40 - otyłość 2 stopień
# 40 < - otyłość 3 stopień

print('Kalkulator BMI')
wzrost = float(input('Podaj swój wzrost w metrach:'))
waga = float(input('Podaj swoją wagę:'))

bmi = float(waga /(wzrost ** 2))
bmi = round(bmi)

print(f'Twoje BMI to: {bmi}')

if bmi <18:
    print('Masz niedowagę, zjedz coś natychmiast!!!')
elif(bmi >=18 and bmi<25):
    print('Twoja waga jest super, tak trzymaj!!!')
elif(bmi >=25 and bmi <30):
    print('Masz lekką nadwagę, to jeszcze nie tragedia, nie jedz batoników przed snem!!')
elif(bmi >=30 and bmi <35):
    print('Uwaga!!, twoja waga jest odrobinę za duża pora na cwiczenia, mogą być brzuszki i pajacyki')
else:
    #bmi >=35:
    print('Skorzystaj z porad dietetyka!')