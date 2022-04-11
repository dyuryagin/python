# import colorgram
#
# colors = colorgram.extract('image.jpg', 15)
# colors_list = []
#
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors_list.append(color_tuple)
#
# print(colors_list)
import random
from turtle import Turtle, Screen


colors_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66)]


screen = Screen()
screen.setup(500, 500)
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
screen.colormode(255)


tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.setposition(15, 15)
tim.hideturtle()


for step in range(15, 500, 50):
    tim.setposition(15, step)
    for _ in range(0, 10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)





screen.exitonclick()
