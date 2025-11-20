
from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed


# Napište program, který nakreslí „plot“ o délce ‹length› pixelů,
# složený z prken (obdélníků) o šířce ‹plank_width› a výšce
# ‹plank_height›. Přesahuje-li poslední prkno požadovanou délku
# plotu, ořežte jej tak, aby měl plot přesně délku ‹length›.
# Zamyslete se nad rozdělením vykreslování do několika samostatných
# procedur. Při kreslení se vám také může hodit while cyklus.

def forsta(height, width):
    for i in range(2):
        forward(height)
        right(90)
        forward(width)
        right(90)
    right(90)
    forward(width)
    left(90)

def fence(length, plank_width, plank_height):
    left(90)
    total = 0
    while total < length:
        rest = length - total
        if (rest >= plank_width):
            forsta(plank_height, plank_width)
        else:
            forsta(plank_height, rest)
            return
        total += plank_width


def main():
    speed(4)
    fence(140, 40, 100)
    done()


if __name__ == "__main__":
    main()
