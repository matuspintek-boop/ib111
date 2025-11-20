from turtle import forward, left
from math import pi


def pizza(side, angle):
    forward(side)
    left(90)
    for i in range(angle):
        forward(2 * pi * side / 360)
        left(1)
    left(90)
    forward(side)
