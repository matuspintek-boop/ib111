from turtle import forward, left, right
from math import sin, tan, radians


def arrow(width, height, angle):
    half_height = float(height) / 2
    half_angle = float(angle) / 2
    nose_width = half_height / tan(radians(half_angle))
    nose_hypot = half_height / sin(radians(half_angle))

    forward(width - nose_width)
    left(90)
    forward(float(height) / 4)

    right(90 + half_angle)
    forward(nose_hypot)
    right(180 - angle)
    forward(nose_hypot)
    right(90 + half_angle)

    forward(float(height) / 4)
    left(90)
    forward(width - nose_width)
    right(90)
    forward(half_height)
    right(90)
