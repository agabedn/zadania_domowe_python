import turtle

bogdan = turtle.Turtle()
licznik_gora = 5
licznik_dol = 1
forward = [40,200,40,200,40,160,80,160,80,120,120,120,120,80,160,80,160,40,200,40,200]
for x in forward:
    bogdan.forward(x)
    bogdan.left(90)

turtle.done()