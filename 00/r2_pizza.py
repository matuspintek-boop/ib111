from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, \
    setheading, done, delay, speed


# † Nakreslete kruhovou výseč („dílek pizzy“) se středovým úhlem
# zadaným (v stupních) parametrem ‹angle› a délkou strany ‹side›.

def pizza(side, angle):
    pass


def main():
    delay(0)
    speed(1)
    pizza(70, 65)

    penup()
    setheading(0)
    forward(150)
    pendown()

    pizza(100, 25)

    done()


if __name__ == "__main__":
    main()
