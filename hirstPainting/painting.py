import turtle
import random
from turtle import *
class Painting:
    def __init__(self, colours, row, number_of_dots):
        self.colours = colours
        self.rows = row
        self.number_of_dots = number_of_dots

    def painting(self):
        turtle.colormode(255)
        tim = Turtle()
        tim.speed("fastest")
        tim.penup()
        tim.hideturtle()
        tim.setheading(225)
        tim.forward(300)
        tim.setheading(0)

        for dot_count in range(1, self.number_of_dots+1):
            tim.dot(20, random.choice(self.colours))
            tim.fd(50)

            if dot_count%10 == 0:
                tim.setheading(90)
                tim.forward(50)
                tim.setheading(180)
                tim.forward(500)
                tim.setheading(0)

        screen = Screen()
        screen.exitonclick()