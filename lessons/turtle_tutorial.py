from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -90)
leo.pendown()

leo.fillcolor(32, 67, 93)
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = 1 + i

leo.end_fill()

leo.speed(50)
leo.hideturtle()

bob: Turtle = Turtle()

bob.penup()
bob.goto(-150, -90)
bob.pendown()

bob.fillcolor(50, 37, 100)
leo.begin_fill()

i: int = 0
while (i < 3):
    bob.forward(300)
    bob.left(120)
    i = 1 + i

bob.end_fill()

bob.speed(100)
bob.hideturtle()

done()