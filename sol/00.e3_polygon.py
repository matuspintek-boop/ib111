from turtle import forward, right


def polygon(sides, length):
    for i in range(sides):
        forward(length)
        right(360.0 / sides)
