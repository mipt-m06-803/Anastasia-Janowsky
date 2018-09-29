import turtle
import math
a = int(input('Vvedite radius okruzhnosti '))
for i in range(360):
    x = (2 * a * math.cos(math.radians(i))) - (a * math.cos(math.radians(2*i)))
    y = (2 * a * math.sin(math.radians(i))) - (a * math.sin(math.radians(2*i)))
    turtle.goto(x, y)
