from ib111 import week_00  # noqa
from turtle import forward, backward, left, right, done, speed


# Implementujte proceduru ‹spiral›, která vykreslí čtyřhrannou
# spirálu s ‹rounds› otočeními (počet otočení říká, kolik hran
# musíme překročit, vydáme-li se ze středu spirály po přímce
# libovolným směrem). Parametr ‹step› pak udává počet pixelů,
# o který se hrany postupně prodlužují.

def draw_spiral(current, step):
    for i in range(4):
        forward(current)
        right(90)
        current += step
    return current

def spiral(rounds, step):
    current = step
    for i in range(rounds):
        current = draw_spiral(current, step)


def main():
    speed(5)
    spiral(5, 10)
    done()


if __name__ == "__main__":
    main()
