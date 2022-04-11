from turtle import Turtle, Screen
from random import choice,randint

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(1)
timmy.speed(1000)

angle = 0

while angle != 360:
    timmy.right(1)
    timmy.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.circle(100)
    angle += 1






screen.exitonclick()






