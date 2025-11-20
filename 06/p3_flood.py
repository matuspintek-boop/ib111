from ib111 import week_06  # noqa

# «Flood fill» je algoritmus z oblasti rastrové grafiky, který
# vyplní souvislou jednobarevnou plochu novou barvou. Postupuje
# tak, že nejdříve na novou barvu obarví pozici, na které začíná,
# dále se pokusí obarvit její sousedy (pozice jiné než cílové barvy
# se neobarvují), a podobně pokračuje se sousedy těchto sousedů,
# atd. Zastaví se, dojde-li na okraj obrázku, nebo narazí na pixel,
# který nemá žádné nové stejnobarevné sousedy.
#
# Sousední pixely uvažujeme pouze ve čtyřech směrech, tj. ne
# diagonálně.

# Napište proceduru, která na vstupu dostane plochu reprezentovanou
# obdélníkovým seznamem seznamů (délky všech vnitřních seznamů jsou
# stejné), počáteční pozici (je zaručeno, že se bude jednat o platné
# souřadnice), a cílovou barvu, na kterou mají být vybrané pozice
# přebarveny.

Position = tuple[int, int]
Area = list[list[int]]


# function returns all neightbours with same color as start_possition
def get_neightbours(current: Position, area: Area,
                    base_color: int) -> set[Position]:

    output: set[Position] = set()
    x, y = current

    if x > 0:
        if area[x-1][y] == base_color:
            output.add((x-1, y))
    if x < len(area) - 1:
        if area[x+1][y] == base_color:
            output.add((x+1, y))
    if y < len(area[0]) - 1:
        if area[x][y+1] == base_color:
            output.add((x, y+1))
    if y > 0:
        if area[x][y-1] == base_color:
            output.add((x, y-1))

    return output


# recursive usage
def flood_fill(area: Area, start: Position, colour: int) -> None:
    x, y = start

    base_color: int = area[x][y]

    if base_color == colour:
        return

    area[x][y] = colour

    neightbours: set[Position] = get_neightbours(start, area, base_color)

    for neightbour in neightbours:

        flood_fill(area, neightbour, colour)


def main() -> None:
    check_flood([[0, 0]], (0, 0), 0, [[0, 0]])
    check_flood([[0]], (0, 0), 1, [[1]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 3), 2, [[0, 0, 2, 2, 2, 0]])
    check_flood([[0, 0, 1, 1, 1, 0]], (0, 0), 2, [[2, 2, 1, 1, 1, 0]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [5, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [5, 5, 8, 8]])
    check_flood([[1, 2, 3, 4], [1, 1, 1, 1], [2, 2, 2, 1], [1, 5, 1, 1]],
                (1, 1), 8,
                [[8, 2, 3, 4], [8, 8, 8, 8], [2, 2, 2, 8], [1, 5, 8, 8]])


def check_flood(area: Area, start: Position,
                new_colour: int, expected_result: Area) -> None:
    flood_fill(area, start, new_colour)
    assert area == expected_result


if __name__ == '__main__':
    main()
