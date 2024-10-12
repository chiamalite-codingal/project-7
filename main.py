import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(300,300)

pencil = turtle.Turtle()

for loop in range(4):
    pencil.forward(100)
    pencil.left(90)
    pencil.forward(100)
    pencil.left(90)
    pencil.forward(100)
    pencil.left(90)
    pencil.forward(100)
    turtle.done()