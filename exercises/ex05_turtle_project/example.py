from turtle import Turtle, colormode, done
colormode(255)

def main() -> None:
    picture: Turtle = Turtle()
    picture.color("white")
    picture.begin_fill()
    picture.pencolor("black")
    rectangle(picture, -175, -375, 300, 400)
    rectangle(picture, 0, -365, 100, 50)
    roof(picture, 225, -75)
    picture.end_fill()
    window(picture, 100, -250)
    window(picture, -100, -250)
    picture.speed(0)

def rectangle(turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    i: int = 0
    while i < 2:
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        i += 1

def roof(turtle: Turtle, x: float, y: float) -> None:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(150)
    turtle.forward(230)
    turtle.left(60)
    turtle.forward(230)
    turtle.setheading(0.0)

def rectangle(turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0.0)
    turtle.pendown()
    i: int = 0
    while i < 2:
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)
        i += 1

def window(turtle: Turtle, x: float, y: float) -> None:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    rectangle(turtle, x, y, 50, 50)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.back(25)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)


main()

done()
