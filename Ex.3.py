import turtle
import math
a = int(input('Vvedite radius okruzhnosti '))
for i in range(180):
    x = (2 * a * math.cos(i)) - (a * math.cos(2*i))
    y = (2 * a * math.sin(i)) - (a * math.sin(2*i))
    turtle.goto(x, y)
