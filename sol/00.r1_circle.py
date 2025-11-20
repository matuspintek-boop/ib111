from turtle import forward, left, penup, pendown
from math import pi, sin


def circle(radius):
    penup()
    forward(radius)
    left(90)
    pendown()
    sides = 180

    for i in range(sides):
        forward(2 * sin(pi / sides) * radius)
        left(360.0 / sides)

    penup()
    left(90)
    forward(radius)
    pendown()
