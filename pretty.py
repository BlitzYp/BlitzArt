import turtle
from random import randint

if __name__ == "__main__":
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor("black")
    t.pencolor()
    t.speed("fastest")
    for _ in range(200):
        t.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
        t.circle(150)
        t.left(5)
    turtle.mainloop()