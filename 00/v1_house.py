from ib111 import week_00  # noqa
from turtle import forward, penup, pendown, done, setheading


# Nakreslete domeček „jedním tahem“ (viz obrázky níže). Obdélníková
# část domečku má šířku ‹width› a výšku ‹height› (kladná reálná
# čísla), úhel špičky střechy je ‹roof_angle› stupňů (v rozsahu 1 až
# 179).

def house(width, height, roof_angle):
    pass


def main():
    house(150, 100, 75)

    penup()
    setheading(0)
    forward(100)
    pendown()

    house(100, 150, 30)
    done()


if __name__ == "__main__":
    main()
