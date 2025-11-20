from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, \
    setheading, done, speed
import math


# Nakreslete rovnoramenný lichoběžník s délkami základen
# ‹base_length› a ‹top_length› a výškou ‹height› (lichoběžník je
# čtyřúhelník s jednou dvojicí rovnoběžných stran – základen –
# spojených rameny, které jsou obecně různoběžné).

def trapezoid(base_length, top_length, height):
    difference = float(base_length - top_length) / 2
    arm_length = math.sqrt(height**2 + difference**2)
    base_angle = math.degrees(math.acos(difference/arm_length))

    forward(base_length)
    left(180-base_angle)
    forward(arm_length)
    left(base_angle)
    forward(top_length)
    left(base_angle)
    forward(arm_length)


def main():
    speed(4)
    trapezoid(100, 70, 70)

    penup()
    setheading(0)
    forward(150)
    pendown()

    trapezoid(120, 30, 35)

    done()


if __name__ == "__main__":
    main()
