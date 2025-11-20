from ib111 import week_07  # noqa
from math import radians, tan, sqrt

# V této úloze budete programovat třídu ‹Tortoise›, která se chová
# podobně jako želva, kterou jsme používali v kapitole B. Rozdílem
# bude, že naše želva nebude kreslit na obrazovku, ale pouze počítat
# své aktuální souřadnice. Souřadnice želvy jsou po každém kroku
# celočíselné, ale výpočty provádějte na hodnotách typu ‹float›,
# které po každém kroku zaokrouhlíte zabudovanou funkcí ‹round›.

# Všechny kreslící metody želvy budou vracet odkaz na vlastní
# instanci, aby bylo lze volání pohodlně řetězit (viz použití
# v testech).

Point = tuple[int, int]


class Tortoise:

    # Želva je po vytvoření otočena v kladném směru osy ⟦y⟧ t.j. „na
    # sever“ a nachází se v bodě ‹initial_point›.

    def __init__(self, initial_point: Point) -> None:
        self.coordinates = initial_point
        self.orientation = 0

    # Metoda ‹forward› posune želvu vpřed o vzdálenost ‹distance›.

    def move(self, distance: int, direction: bool) -> 'Tortoise':
        x, y = self.coordinates

        # urcenie mutiplkatora pre mser pohybu
        direction_multiplicator: int = 1 if direction else -1

        if self.orientation == 0:
            y += direction_multiplicator * distance
        elif self.orientation == 180:
            y -= direction_multiplicator * distance
        elif self.orientation == 90:
            x += direction_multiplicator * distance
        elif self.orientation == 270:
            x -= direction_multiplicator * distance
        else:
            angle = radians(self.orientation)
            tangens = abs(tan(angle))

            # multiplikatory pre smer pohybu v x a y osy
            x_multiplcator = 1 if self.orientation < 180 else -1
            x_multiplcator *= direction_multiplicator
            y_multiplicator = 1 if self.orientation < 90 \
                or self.orientation > 270 else -1
            y_multiplicator *= direction_multiplicator

            # vychádzame z pytagorovej vety a^2 + b^2 = c^2
            # tangens nam udava pomer protilahlej strany ku prilahlej (x, y)
            # dokopy mozme teda povedat za ak x = napr. 1,5 =>
            # => (abs(1,5) + 1)*a^2 = c^2
            # z toho a = sqrt(c^2)/ sqrt(tangens^2 + 1)
            # mame potrebne udaje z ktorych uz lahko dopocitame koordinaty

            a = sqrt(distance**2/(tangens**2 + 1))

            x += round(x_multiplcator*tangens*a)

            y += round(y_multiplicator*a)

        self.coordinates = (x, y)

        return self

    def forward(self, distance: int) -> 'Tortoise':
        return self.move(distance, True)

    # Metoda ‹backward› ji posune naopak vzad, opět o vzdálenost
    # ‹distance›.

    def backward(self, distance: int) -> 'Tortoise':
        return self.move(distance, False)

    # Metody ‹left› a ‹right› želvu otočí o počet stupňů daný
    # parametrem ‹angle›. Metoda ‹left› proti, a metoda ‹right› po
    # směru hodinových ručiček.

    def left(self, angle: int) -> 'Tortoise':
        self.orientation -= angle
        if self.orientation < 0:
            self.orientation += 360

        return self

    def right(self, angle: int) -> 'Tortoise':
        self.orientation += angle
        if self.orientation >= 360:
            self.orientation -= 360

        return self

    # Konečně (čistá) metoda ‹position› vrátí aktuální pozici želvy.

    def position(self) -> Point:
        return self.coordinates


def main() -> None:
    turtle = Tortoise((0, 0))
    turtle.forward(5)
    assert turtle.position() == (0, 5)
    turtle.right(90).forward(5)
    assert turtle.position() == (5, 5)
    assert turtle.right(90).forward(3).position() == (5, 2)
    assert turtle.right(90).forward(5).position() == (0, 2)
    assert turtle.right(90).backward(2).position() == (0, 0)
    assert turtle.position() == (0, 0)

    turtle.forward(10).left(180).forward(15)
    assert turtle.position() == (0, -5)
    turtle.left(45).forward(2)
    assert turtle.position() == (1, -6)
    turtle.left(15).forward(4)
    assert turtle.position() == (4, -8)


if __name__ == "__main__":
    main()
