from turtle import forward, right


def pentagon(side):
    for i in range(5):
        forward(side)
        right(360.0 / 5)
