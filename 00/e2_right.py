from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, penup, pendown, done


# Implementujte proceduru ‹right_triangle›, která vykreslí pravoúhlý
# trojúhelník s odvěsnami o délkách ‹side_a› a ‹side_b›. Můžou se
# vám hodit funkce z modulu ‹math›.

def right_triangle(side_a, side_b):
    pass


def main():
    right_triangle(80, 20)

    right(90)
    penup()
    forward(100)
    pendown()
    right(180)

    right_triangle(60, 60)
    done()


if __name__ == "__main__":
    main()
