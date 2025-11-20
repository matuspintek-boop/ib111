from turtle import forward, left
from math import sqrt, degrees, asin


def right_triangle(side_a, side_b):
    hypotenuse = sqrt(side_a ** 2 + side_b ** 2)
    beta = degrees(asin(side_b / hypotenuse))

    forward(side_a)
    left(180 - beta)
    forward(hypotenuse)
    left(180 - (90 - beta))
    forward(side_b)
