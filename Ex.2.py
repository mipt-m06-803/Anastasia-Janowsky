import turtle
X=int(input('How many steps must a turtle walk down? '))
turtle.goto(0, 0)
turtle.shape('turtle')
turtle.circle(X)
turtle.penup()
turtle.goto(0, -(2*X))
turtle.pendown()
turtle.circle(X)
