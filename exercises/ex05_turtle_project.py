"""TODO: Describe your scene program."""
__author__ = "730656379"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """Pulls all the elements together."""
    picture: Turtle = Turtle()
    cloud(picture, 30, 350, 150)          
    cloud(picture, 30, 100, 300)
    cloud(picture, 45, -300, 0)
    cloud(picture, 40, 50, 250)
    cloud(picture, 40, -250, 175)
    cloud(picture, 35, -250, 230)
    picture.penup()
    picture.color("white")
    picture.begin_fill()
    picture.pencolor("black")
    picture.pendown()
    rectangle(picture, -175, -375, 300, 400)
    rectangle(picture, 0, -365, 100, 50)
    roof(picture, 225, -75)
    picture.end_fill()
    window(picture, 100, -250)
    window(picture, -100, -250)
    picture.speed(0)
    picture.hideturtle()


def rectangle(turtle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draws the rectangles in the drawing."""
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
    """Draws the roof of the house."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(150)
    turtle.forward(230)
    turtle.left(60)
    turtle.forward(230)
    turtle.setheading(0.0)


def cloud(turtle: Turtle, size: float, x: float, y: float) -> None:
    """Trying to make a cloud using circles."""
    turtle.setheading(0) 
    turtle.penup()   
    turtle.fillcolor(245, 242, 242)
    turtle.pencolor(245, 242, 242)
    turtle.begin_fill()
    turtle.goto(x, y)
    turtle.pendown()
    i: int = 0
    while i < 5:
        if i == 4:
            turtle.left(90)
            turtle.forward(35)
            turtle.circle(size)
        turtle.begin_fill()
        turtle.circle(size)
        turtle.forward(20)
        turtle.left(90)
        turtle.end_fill()
        i = 1 + i          
    turtle.end_fill()


def window(turtle: Turtle, x: float, y: float) -> None:
    """Uses the rectangle function to draw windows."""
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
if __name__ == "__main__":
    main()

done()