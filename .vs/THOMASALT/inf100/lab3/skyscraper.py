from uib_inf100_graphics.simple import *

ant = input("Hvor mange vinduer skal toget ha? ")
eta = input("Hvor mange vinduer skal toget ha? ")


def tegnsky(ant, eta):
    eta = int(eta)
    ant = int(ant)
    startx = 10
    starty = 10
    dist = 5
    høyde = 10
    bredde = 5

    canvas.create_rectangle(startx, starty, ((ant + 1) * 10) + dist, ((eta + 1) * 15))
    for g in range(eta):
        for i in range(ant):
            canvas.create_rectangle(
                startx + dist + (i * 10),
                starty + dist + (g * 15),
                startx + dist + bredde + (i * 10),
                starty + dist + høyde + (g * 15),
            )

    display(canvas)


tegnsky(ant, eta)
