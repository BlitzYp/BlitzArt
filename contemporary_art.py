import turtle
from random import randint

if __name__ == "__main__":
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    t.penup()
    SCREEN_WIDTH = turtle.window_width() - 500
    SCREEN_HEIGHT = turtle.window_height() - 450
    t.setx(SCREEN_WIDTH)
    t.sety(-SCREEN_HEIGHT)
    t.speed("fastest")
    for _ in range(int(SCREEN_HEIGHT / 45)):
        t.setx(SCREEN_WIDTH)
        for _ in range(int(SCREEN_WIDTH / 45)):
            if randint(0, 1):
                t.fillcolor((randint(0, 255), randint(0, 255), randint(0, 255)))
                t.dot(100, (randint(0, 255), randint(0, 255), randint(0, 255)))
                t.setx(t.xcor() - 100)
        t.sety(t.ycor() + 100)
    turtle.mainloop()