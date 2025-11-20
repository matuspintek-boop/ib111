from ib111 import week_00  # noqa
from turtle import forward, left, right, penup, pendown, done, setheading


# Nakreslete obrys vlajky s klínem vlevo (viz obrázky níže).
# Parametry ‹width› a ‹height› (kladná reálná čísla) označují šířku,
# resp. výšku vlajky. Parametr ‹triangle_ratio› (reálné číslo mezi 0
# a 1 včetně) označuje, do jaké části šířky vlajky má zasahovat její
# klín.

def flag(width, height, triangle_ratio):
    pass


def main():
    flag(150, 100, 0.5)

    penup()
    setheading(0)
    forward(200)
    right(90)
    forward(125)
    left(90)
    pendown()

    flag(100, 150, 0.3)
    done()


if __name__ == "__main__":
    main()
